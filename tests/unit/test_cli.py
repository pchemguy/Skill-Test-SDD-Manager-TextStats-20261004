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
                           (["--keep-bom"], 2), (["--help"], 0)]:
            with self.subTest(args=args):
                with patch("textstats.cli.count_file", side_effect=AssertionError("acquired")) as acquire:
                    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                        with self.assertRaises(SystemExit) as result:
                            main(args)
                self.assertEqual(result.exception.code, code)
                acquire.assert_not_called()
