"""Option validation must precede named-file acquisition."""

import contextlib
import importlib.util
import io
import unittest
from unittest.mock import patch


class CliValidationTests(unittest.TestCase):
    def test_usage_errors_and_help_never_acquire(self):
        self.assertIsNotNone(importlib.util.find_spec("textstats.cli"), "command adapter missing")
        from textstats.cli import main
        for args, code in [([], 2), (["one", "two"], 2), (["--unknown", "one"], 2),
                           (["--keep-bom"], 2), (["--json"], 2), (["--json", "one", "two"], 2),
                           (["--json", "--unknown", "one"], 2), (["--help"], 0)]:
            with self.subTest(args=args):
                with patch("textstats.cli.count_file", side_effect=AssertionError("acquired")) as acquire:
                    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                        with self.assertRaises(SystemExit) as result:
                            main(args)
                self.assertEqual(result.exception.code, code)
                acquire.assert_not_called()

class CliFailureTests(unittest.TestCase):
    def test_expected_errors_are_identified_and_atomic(self):
        from textstats.cli import main
        errors = [FileNotFoundError("missing"), PermissionError("denied"),
                  OSError("read failed"), UnicodeDecodeError("utf-8", b"\xff", 0, 1, "invalid byte")]
        for error in errors:
            for options in ([], ["--keep-bom"]):
                with self.subTest(error=type(error), options=options):
                    out, err = io.StringIO(), io.StringIO()
                    with patch("textstats.cli.count_file", side_effect=error):
                        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                            result = main([*options, "input.txt"])
                    self.assertEqual((result, out.getvalue()), (1, ""))
                    self.assertIn("input.txt", err.getvalue())
                    self.assertNotIn("Traceback", err.getvalue())


class RemovedJsonTests(unittest.TestCase):
    def test_removed_option_rejects_before_any_acquisition(self):
        from textstats.cli import main
        for args in (["--json", "missing"], ["--json", "--keep-bom", "missing"],
                     ["--keep-bom", "--json", "missing"],
                     ["--lines", "1:1", "--json", "missing"],
                     ["--json", "--lines=1:1", "missing"]):
            with self.subTest(args=args):
                out, err = io.StringIO(), io.StringIO()
                from textstats import TextStats
                with patch("textstats.cli.count_file", return_value=TextStats(0, 0)) as count, patch("textstats.cli._read_text", return_value="") as read:
                    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                        with self.assertRaises(SystemExit) as result:
                            main(args)
                self.assertEqual(result.exception.code, 2)
                self.assertEqual(out.getvalue(), "")
                self.assertIn("--json", err.getvalue())
                self.assertNotIn("Traceback", err.getvalue())
                count.assert_not_called()
                read.assert_not_called()
