"""Required T-001 acceptance: docs/dev/SPEC.md S-1/S-2 and TASKS T-001.

Every expected pair below is a literal chosen from the accepted counting rules.
No acquisition, CLI, future-format or undocumented type/error rule is required.
"""
import contextlib
import io
import unittest
from textstats import TextStats, count_text


class RequiredT001Acceptance(unittest.TestCase):
    def test_required_literals_and_silence(self):
        vectors = [
            ("", True, (0, 0)),
            ("alpha beta", True, (1, 2)),
            ("alpha\n", True, (1, 1)),
            ("\n", True, (1, 0)),
            ("alpha\r\nbeta\rgamma\n", True, (3, 3)),
            ("alpha\n\n", True, (2, 1)),
            (" \t", True, (1, 0)),
            ("alpha\u2028beta", True, (1, 2)),
            ("\ufeff", True, (0, 0)),
            ("\ufeff", False, (1, 1)),
            ("\ufeff\ufeff", True, (1, 1)),
            ("alpha\ufeffbeta", True, (1, 1)),
            ("alpha\u2029beta", True, (1, 2)),
            ("a\v b\f c\x85d\u00a0e", True, (1, 5)),
            ("\r\n\r\n", True, (2, 0)),
            ("\r\n\r", True, (2, 0)),
            ("\ufeff\r\n", True, (1, 0)),
            ("\ufeff\r\n", False, (1, 1)),
            ("\ufeffalpha\ufeff beta", False, (1, 2)),
        ]
        for text, strip_bom, expected in vectors:
            with self.subTest(text=repr(text), strip_bom=strip_bom):
                stdout, stderr = io.StringIO(), io.StringIO()
                with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                    actual = count_text(text, strip_bom=strip_bom)
                self.assertIsInstance(actual, TextStats)
                self.assertEqual((actual.lines, actual.words), expected)
                self.assertIs(type(actual.lines), int)
                self.assertIs(type(actual.words), int)
                self.assertEqual(stdout.getvalue(), "")
                self.assertEqual(stderr.getvalue(), "")
        default_result = count_text("\ufeff")
        self.assertEqual((default_result.lines, default_result.words), (0, 0))

    def test_required_nonnegative_immutable_value(self):
        value = TextStats(2, 3)
        self.assertEqual((value.lines, value.words), (2, 3))
        for field in ("lines", "words"):
            with self.subTest(field=field):
                with self.assertRaises(Exception):
                    setattr(value, field, 4)
        self.assertEqual((value.lines, value.words), (2, 3))
        for args in ((-1, 0), (0, -1), (-1, -1)):
            with self.subTest(args=args):
                with self.assertRaises(Exception):
                    TextStats(*args)


if __name__ == "__main__":
    unittest.main()
