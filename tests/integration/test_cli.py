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
        for args in [(), ("one", "two"), ("--unknown", "one"), ("--jsn", "one")]:
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

class TextOnlyModuleTests(unittest.TestCase):
    invoke = ModuleCliTests.invoke

    def test_retained_text_counts_and_bom_cases(self):
        cases = [(b"alpha beta\r\ngamma\r", (2, 3), (2, 3)),
                 (b"", (0, 0), (0, 0)), (b"alpha\n\n", (2, 1), (2, 1)),
                 ("café\u2028tea\n".encode(), (1, 2), (1, 2)),
                 ("\ufeff\n".encode(), (1, 0), (1, 1)),
                 ("\ufeff".encode(), (0, 0), (1, 1)),
                 ("\ufeff\ufeff".encode(), (1, 1), (1, 1))]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.txt"
            for data, stripped, retained in cases:
                path.write_bytes(data)
                for options, counts in [((), stripped), (("--keep-bom",), retained)]:
                    with self.subTest(data=data, options=options):
                        run = self.invoke(*options, path)
                        self.assertEqual((run.returncode, run.stdout, run.stderr),
                                         (0, f"lines={counts[0]} words={counts[1]}\n", ""))
                        self.assertEqual(path.read_bytes(), data)

    def test_removed_option_and_literal_filename(self):
        for options in (("--json",), ("--json", "--keep-bom"),
                        ("--keep-bom", "--json"), ("--json", "--lines=1:1"),
                        ("--lines", "1:1", "--json")):
            run = self.invoke(*options, "missing")
            self.assertEqual((run.returncode, run.stdout), (2, ""))
            self.assertIn("--json", run.stderr)
            self.assertNotIn("Traceback", run.stderr)
        help_run = self.invoke("--help")
        self.assertEqual(help_run.returncode, 0)
        self.assertNotIn("--json", help_run.stdout)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "--json"
            data = "\ufeffalpha beta\nlast".encode()
            path.write_bytes(data)
            environment = dict(__import__("os").environ)
            environment["PYTHONPATH"] = str(Path.cwd())
            for options, expected in [((), "lines=2 words=3\n"),
                                      (("--lines=2:2",), "lines=1 words=1\n"),
                                      (("--keep-bom",), "lines=2 words=3\n")]:
                run = subprocess.run([sys.executable, "-m", "textstats", *options, "--", "--json"],
                                     cwd=directory, env=environment, capture_output=True, text=True)
                self.assertEqual((run.returncode, run.stdout, run.stderr), (0, expected, ""))
                self.assertEqual(path.read_bytes(), data)
