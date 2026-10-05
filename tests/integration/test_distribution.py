"""Run a source archive independently of checkout imports."""

import os
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile
import unittest


class SourceDistributionTests(unittest.TestCase):
    def test_extracted_package_public_docs_and_module_contract(self):
        root = Path(__file__).resolve().parents[2]
        with tempfile.TemporaryDirectory() as directory:
            temporary = Path(directory)
            build = temporary / "build"
            result = subprocess.run(["make", "dist", f"DIST_DIR={build}"],
                                    cwd=root, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            archive = build / "textstats.tar.gz"
            extracted = temporary / "extracted"
            extracted.mkdir()
            with tarfile.open(archive) as source:
                names = source.getnames()
                for required in ("textstats/__init__.py", "textstats/__main__.py",
                                 "README.md", "Makefile", "docs/api.md", "docs/module.md"):
                    self.assertIn(required, names)
                self.assertFalse(any("textstats-run-resources" in name or
                                     "__pycache__" in name or name.startswith("dist/")
                                     for name in names))
                # The archive is produced locally from explicit project paths.
                self.assertFalse(any(Path(name).is_absolute() or ".." in Path(name).parts
                                     for name in names))
                options = {"filter": "data"} if hasattr(tarfile, "data_filter") else {}
                source.extractall(extracted, **options)
            environment = {key: value for key, value in os.environ.items()
                           if key not in ("PYTHONPATH", "PYTHONHOME", "PYTHONSTARTUP")}
            environment.update(PYTHONNOUSERSITE="1", PYTHONDONTWRITEBYTECODE="1")
            identity = subprocess.run(
                [sys.executable, "-c", "import textstats; print(textstats.__file__)"],
                cwd=extracted, env=environment, capture_output=True, text=True)
            self.assertEqual(identity.returncode, 0, identity.stderr)
            self.assertEqual(Path(identity.stdout.strip()).resolve(),
                             extracted / "textstats" / "__init__.py")

            def invoke(*arguments):
                return subprocess.run([sys.executable, "-m", "textstats", *arguments],
                                      cwd=extracted, env=environment,
                                      capture_output=True, text=True)

            path = extracted / "sample.txt"
            for data, options, expected in [
                (b"alpha beta\r\ngamma\r", (), "lines=2 words=3\n"),
                (b"", (), "lines=0 words=0\n"),
                ("café\u2028tea\n".encode(), (), "lines=1 words=2\n"),
                ("\ufeff\n".encode(), (), "lines=1 words=0\n"),
                ("\ufeff\n".encode(), ("--keep-bom",), "lines=1 words=1\n"),
            ]:
                with self.subTest(data=data, options=options):
                    path.write_bytes(data)
                    run = invoke(*options, "sample.txt")
                    self.assertEqual((run.returncode, run.stdout, run.stderr),
                                     (0, expected, ""))
                    self.assertEqual(path.read_bytes(), data)
            path.write_bytes("\ufeffalpha beta\r\nbeta\n\ufefflast two".encode())
            original = path.read_bytes()
            for options, expected in [
                (("--lines", "2:3"), "lines=2 words=3\n"),
                (("--lines=4:99",), "lines=0 words=0\n"),
                (("--lines=1:1",), "lines=1 words=2\n"),
                (("--keep-bom", "--lines=1:1"), "lines=1 words=2\n"),
            ]:
                run = invoke(*options, "sample.txt")
                self.assertEqual((run.returncode, run.stdout, run.stderr), (0, expected, ""))
                self.assertEqual(path.read_bytes(), original)
            path.write_bytes("\ufeff\n".encode())
            for options, words in [(("--lines=1:1",), 0),
                                   (("--lines", "1:1", "--keep-bom"), 1)]:
                run = invoke(*options, "sample.txt")
                self.assertEqual((run.returncode, run.stderr), (0, ""))
                self.assertEqual(run.stdout, f"lines=1 words={words}\n")
            for arguments, status in [(("--lines=2:1", "sample.txt"), 2),
                                      (("--lines=1:1", "--lines", "1:1", "sample.txt"), 2),
                                      (("--lines=1:1", "missing.txt"), 1)]:
                run = invoke(*arguments)
                self.assertEqual((run.returncode, run.stdout), (status, ""))
                self.assertTrue(run.stderr)
                self.assertNotIn("Traceback", run.stderr)
            path.write_bytes(b"valid\nlate\xff")
            run = invoke("--lines=1:1", "sample.txt")
            self.assertEqual((run.returncode, run.stdout), (1, ""))
            self.assertIn("sample.txt", run.stderr)
            self.assertNotIn("Traceback", run.stderr)
            self.assertEqual(path.read_bytes(), b"valid\nlate\xff")
            path.write_bytes(b"alpha\n")
            dash = extracted / "-sample.txt"
            dash.write_bytes(b"alpha\n")
            run = invoke("--lines=1:1", "--", "-sample.txt")
            self.assertEqual((run.returncode, run.stdout, run.stderr), (0, "lines=1 words=1\n", ""))
            help_run = invoke("--help")
            self.assertEqual((help_run.returncode, help_run.stderr), (0, ""))
            self.assertIn("--keep-bom", help_run.stdout)
            self.assertNotIn("--json", help_run.stdout)
            self.assertIn("--lines", help_run.stdout)
            for arguments, status in [(("missing.txt",), 1), ((), 2),
                                      (("--jsn", "sample.txt"), 2)]:
                run = invoke(*arguments)
                self.assertEqual((run.returncode, run.stdout), (status, ""))
                self.assertTrue(run.stderr)
                self.assertNotIn("Traceback", run.stderr)
            missing_json = invoke("--json", "missing.txt")
            self.assertEqual((missing_json.returncode, missing_json.stdout), (2, ""))
            self.assertIn("--json", missing_json.stderr)
            path.write_bytes(b"valid prefix\xff")
            run = invoke("sample.txt")
            self.assertEqual((run.returncode, run.stdout), (1, ""))
            self.assertIn("sample.txt", run.stderr)
            self.assertNotIn("Traceback", run.stderr)
            self.assertEqual(path.read_bytes(), b"valid prefix\xff")
            for options in (("--json",), ("--json", "--keep-bom"), ("--keep-bom", "--json")):
                bad_json = invoke(*options, "sample.txt")
                self.assertEqual((bad_json.returncode, bad_json.stdout), (2, ""))
                self.assertIn("--json", bad_json.stderr)
                self.assertNotIn("Traceback", bad_json.stderr)
                self.assertEqual(path.read_bytes(), b"valid prefix\xff")

            literal = extracted / "--json"
            data = b"alpha beta\nlast"
            literal.write_bytes(data)
            run = invoke("--lines=1:1", "--", "--json")
            self.assertEqual((run.returncode, run.stdout, run.stderr), (0, "lines=1 words=2\n", ""))
            self.assertEqual(literal.read_bytes(), data)
            for options in (("--json",), ("--lines=1:1", "--json"), ("--json", "--keep-bom")):
                run = invoke(*options, "missing.txt")
                self.assertEqual((run.returncode, run.stdout), (2, ""))
                self.assertIn("--json", run.stderr)
