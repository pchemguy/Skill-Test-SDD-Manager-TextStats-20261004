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

class JsonModuleTests(unittest.TestCase):
    invoke = ModuleCliTests.invoke

    def test_json_counts_types_bom_orders_and_text_default(self):
        import json
        cases = [(b"alpha beta\r\ngamma\r", (2, 3), (2, 3)),
                 (b"", (0, 0), (0, 0)), (b"alpha\n\n", (2, 1), (2, 1)),
                 ("café\u2028tea\n".encode(), (1, 2), (1, 2)),
                 ("\ufeff\n".encode(), (1, 0), (1, 1)),
                 ("\ufeff".encode(), (0, 0), (1, 1)),
                 ("\ufeff\ufeff".encode(), (1, 1), (1, 1))]
        with tempfile.TemporaryDirectory(prefix="-json-", dir=".") as directory:
            path = Path(directory) / "sample.txt"
            for data, stripped, retained in cases:
                path.write_bytes(data)
                for options, counts in [(("--json",), stripped),
                                        (("--json", "--keep-bom"), retained),
                                        (("--keep-bom", "--json"), retained)]:
                    with self.subTest(data=data, options=options):
                        run = self.invoke(*options, "--", path)
                        self.assertEqual((run.returncode, run.stderr), (0, ""))
                        self.assertTrue(run.stdout.endswith("\n"))
                        self.assertEqual(len(run.stdout.splitlines()), 1)
                        value = json.loads(run.stdout)
                        self.assertEqual(value, {"lines": counts[0], "words": counts[1]})
                        self.assertEqual(set(value), {"lines", "words"})
                        self.assertTrue(all(type(v) is int for v in value.values()))
                        text = self.invoke(*[o for o in options if o != "--json"], "--", path)
                        self.assertEqual((text.returncode, text.stdout, text.stderr),
                                         (0, f"lines={counts[0]} words={counts[1]}\n", ""))
                        self.assertEqual(path.read_bytes(), data)

    def test_json_errors_remain_atomic_and_identify_input(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bad = root / "bad.txt"
            bad.write_bytes(b"valid prefix\xff")
            for options in (("--json",), ("--json", "--keep-bom"), ("--keep-bom", "--json")):
                for path in (root / "missing", root, bad):
                    with self.subTest(path=path, options=options):
                        run = self.invoke(*options, path)
                        self.assertEqual((run.returncode, run.stdout), (1, ""))
                        self.assertIn(str(path), run.stderr)
                        self.assertNotIn("Traceback", run.stderr)
            self.assertEqual(bad.read_bytes(), b"valid prefix\xff")
