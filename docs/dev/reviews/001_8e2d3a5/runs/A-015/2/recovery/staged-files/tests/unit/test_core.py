"""S-1/S-2 acceptance using independently specified expected counts."""

from contextlib import redirect_stderr, redirect_stdout
from dataclasses import FrozenInstanceError
import inspect
import io
import unittest

from textstats import TextStats, count_text


class TextStatsTests(unittest.TestCase):
    def test_values_are_nonnegative_integers(self):
        stats = TextStats(0, 2)
        self.assertEqual((stats.lines, stats.words), (0, 2))
        self.assertIs(type(stats.lines), int)
        self.assertIs(type(stats.words), int)

    def test_negative_construction_is_rejected(self):
        for counts in [(-1, 0), (0, -1), (-1, -1)]:
            with self.subTest(counts=counts), self.assertRaises(ValueError):
                TextStats(*counts)

    def test_noninteger_fields_are_rejected(self):
        for counts in [(1.5, 0), (0, "2")]:
            with self.subTest(counts=counts), self.assertRaises(TypeError):
                TextStats(*counts)

    def test_fields_cannot_be_changed(self):
        stats = TextStats(1, 2)
        for field in ["lines", "words"]:
            with self.subTest(field=field), self.assertRaises(FrozenInstanceError):
                setattr(stats, field, 9)


class CountTextTests(unittest.TestCase):
    def test_all_spec_sample_rows(self):
        rows = [("", True, 0, 0), ("alpha beta", True, 1, 2),
                ("alpha\n", True, 1, 1), ("\n", True, 1, 0),
                ("alpha\r\nbeta\rgamma\n", True, 3, 3),
                ("alpha\n\n", True, 2, 1), (" \t", True, 1, 0),
                ("alpha\u2028beta", True, 1, 2),
                ("\ufeff", True, 0, 0), ("\ufeff", False, 1, 1),
                ("\ufeff\ufeff", True, 1, 1)]
        for text, strip, lines, words in rows:
            with self.subTest(text=repr(text), strip=strip):
                self.assertEqual(count_text(text, strip_bom=strip), TextStats(lines, words))

    def test_only_cr_and_lf_terminate_lines(self):
        for text, expected in [("\r\n", (1, 0)), ("\r", (1, 0)),
                               ("a\rb", (2, 2)), ("\r\n\r\n", (2, 0)),
                               ("a\r\n\nb", (3, 2)),
                               ("a\v\f\x85\u2029b", (1, 2))]:
            with self.subTest(text=repr(text)):
                self.assertEqual(count_text(text), TextStats(*expected))

    def test_unicode_whitespace_splits_words(self):
        self.assertEqual(count_text("one\u00a0two\u2003三\t四"), TextStats(1, 4))

    def test_bom_policy_preserves_interior_and_second_bom(self):
        for text, strip, expected in [("a\ufeffb", True, (1, 1)),
                                      ("a \ufeff b", True, (1, 3)),
                                      ("\ufeff\ufeff\n", True, (1, 1)),
                                      ("\ufeff\n", False, (1, 1)),
                                      ("\ufeff\n", True, (1, 0))]:
            with self.subTest(text=repr(text), strip=strip):
                self.assertEqual(count_text(text, strip_bom=strip), TextStats(*expected))

    def test_input_is_unchanged(self):
        original = "\ufeffalpha\r\nbeta\r"
        self.assertEqual(count_text(original), TextStats(2, 2))
        self.assertEqual(original, "\ufeffalpha\r\nbeta\r")

    def test_api_calls_are_silent(self):
        stdout, stderr = io.StringIO(), io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            TextStats(0, 0)
            count_text("alpha")
            count_text("\ufeff", strip_bom=False)
            with self.assertRaises(ValueError):
                TextStats(-1, 0)
        self.assertEqual((stdout.getvalue(), stderr.getvalue()), ("", ""))

    def test_strip_bom_is_keyword_only_and_defaults_true(self):
        parameter = inspect.signature(count_text).parameters["strip_bom"]
        self.assertEqual(parameter.kind, inspect.Parameter.KEYWORD_ONLY)
        self.assertIs(parameter.default, True)
        with self.assertRaises(TypeError):
            count_text("", False)
