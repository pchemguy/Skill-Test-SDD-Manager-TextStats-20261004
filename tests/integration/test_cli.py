"""Exercise the actual module entry against real named inputs."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from textstats import count_file


class ModuleCliTests(unittest.TestCase):
    def invoke(self, *args):
        return subprocess.run([sys.executable, "-m", "textstats", *map(str, args)],
                              capture_output=True, text=True)

    def test_named_files_counts_and_api_agreement(self):
        cases = [(b"alpha beta\r\ngamma\r", (2, 3)), (b"", (0, 0)),
                 ("café\u2028tea\n".encode(), (1, 2)),
                 ("\ufeff\n".encode(), (1, 0)), ("\ufeff\ufeff".encode(), (1, 1))]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "normal.txt"
            for data, counts in cases:
                with self.subTest(data=data):
                    path.write_bytes(data)
                    run = self.invoke(path)
                    self.assertEqual((run.returncode, run.stdout, run.stderr),
                                     (0, f"lines={counts[0]} words={counts[1]}\n", ""))
                    self.assertEqual((count_file(path).lines, count_file(path).words), counts)
                    self.assertEqual(path.read_bytes(), data)

    def test_keep_bom_and_dash_prefixed_filename(self):
        # A temporary relative path can begin with '-' to exercise '--'.
        with tempfile.TemporaryDirectory(prefix="-textstats-", dir=".") as directory:
            path = Path(directory) / "bom.txt"
            data = "\ufeff\n".encode()
            path.write_bytes(data)
            for options, output in [((), "lines=1 words=0\n"),
                                    (("--keep-bom",), "lines=1 words=1\n")]:
                run = self.invoke(*options, "--", path)
                self.assertEqual((run.returncode, run.stdout, run.stderr), (0, output, ""))
            self.assertEqual(path.read_bytes(), data)

    def test_help(self):
        run = self.invoke("--help")
        self.assertEqual((run.returncode, run.stderr), (0, ""))
        for word in ("usage:", "INPUT", "--keep-bom"):
            self.assertIn(word, run.stdout)

    def test_invalid_invocations(self):
        for args in [(), ("one", "two"), ("--unknown", "one"), ("--json", "one")]:
            with self.subTest(args=args):
                run = self.invoke(*args)
                self.assertEqual((run.returncode, run.stdout), (2, ""))
                self.assertIn("usage:", run.stderr)
                self.assertNotIn("Traceback", run.stderr)

class ModuleFailureTests(unittest.TestCase):
    invoke = ModuleCliTests.invoke

    def test_expected_file_failures(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bad = root / "bad.txt"
            data = b"valid prefix\r\n\xff"
            bad.write_bytes(data)
            for options in ((), ("--keep-bom",)):
                for path in (root / "missing", root, bad):
                    with self.subTest(path=path, options=options):
                        run = self.invoke(*options, path)
                        self.assertEqual((run.returncode, run.stdout), (1, ""))
                        self.assertIn(str(path), run.stderr)
                        self.assertNotIn("Traceback", run.stderr)
                        self.assertEqual(bad.read_bytes(), data)
