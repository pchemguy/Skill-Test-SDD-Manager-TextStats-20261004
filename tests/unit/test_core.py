"""Contract tests for the public immutable statistics value and text semantics."""

import contextlib
import dataclasses
import inspect
import io
import unittest

import textstats


class StatisticsTests(unittest.TestCase):
    def test_public_statistics_value(self):
        self.assertTrue(hasattr(textstats, "TextStats"), "missing public TextStats export")
        stats = textstats.TextStats(lines=2, words=3)
        self.assertEqual((stats.lines, stats.words), (2, 3))
        self.assertEqual(stats, textstats.TextStats(2, 3))

    def test_fields_are_immutable(self):
        stats = textstats.TextStats(2, 3)
        for field in ("lines", "words"):
            with self.subTest(field=field):
                with self.assertRaises(dataclasses.FrozenInstanceError):
                    setattr(stats, field, 0)
                with self.assertRaises(dataclasses.FrozenInstanceError):
                    delattr(stats, field)

    def test_negative_counts_are_rejected(self):
        for lines, words in ((-1, 0), (0, -1), (-2, -3)):
            with self.subTest(lines=lines, words=words):
                with self.assertRaises(ValueError):
                    textstats.TextStats(lines, words)

    def test_noninteger_counts_are_rejected(self):
        for value in (1.5, "2", None, True):
            for field in ("lines", "words"):
                with self.subTest(value=value, field=field):
                    counts = {"lines": 0, "words": 0, field: value}
                    with self.assertRaises(TypeError):
                        textstats.TextStats(**counts)

    def test_zero_counts_are_valid(self):
        self.assertEqual(textstats.TextStats(0, 0).lines, 0)
        self.assertEqual(textstats.TextStats(0, 0).words, 0)


class TextCountingTests(unittest.TestCase):
    def test_count_text_is_public(self):
        self.assertTrue(hasattr(textstats, "count_text"), "missing public count_text export")

    def test_specification_samples(self):
        samples = (
            ("", True, 0, 0),
            ("alpha beta", True, 1, 2),
            ("alpha\n", True, 1, 1),
            ("\n", True, 1, 0),
            ("alpha\r\nbeta\rgamma\n", True, 3, 3),
            ("alpha\n\n", True, 2, 1),
            (" \t", True, 1, 0),
            ("alpha\u2028beta", True, 1, 2),
            ("\ufeff", True, 0, 0),
            ("\ufeff", False, 1, 1),
            ("\ufeff\ufeff", True, 1, 1),
        )
        for text, strip_bom, lines, words in samples:
            with self.subTest(text=text, strip_bom=strip_bom):
                self.assertEqual(textstats.count_text(text, strip_bom=strip_bom),
                                 textstats.TextStats(lines, words))

    def test_terminator_boundaries(self):
        for text, lines in (("\r\n", 1), ("\r", 1), ("\r\r\n\n", 3),
                            ("a\r\nb", 2), ("a\rb\n\r\nc", 4)):
            with self.subTest(text=text):
                self.assertEqual(textstats.count_text(text).lines, lines)

    def test_unicode_whitespace_is_not_a_line_terminator(self):
        for separator in ("\u0085", "\u00a0", "\u2003", "\u2028", "\u2029", "\v", "\f"):
            with self.subTest(separator=separator):
                self.assertEqual(textstats.count_text("alpha" + separator + "beta"),
                                 textstats.TextStats(1, 2))

    def test_only_one_initial_bom_is_removed(self):
        for text, strip_bom, lines, words in (
            ("\ufeff alpha", True, 1, 1),
            ("\ufeff alpha", False, 1, 2),
            ("\ufeff\ufeff alpha", True, 1, 2),
            ("alpha \ufeff beta", True, 1, 3),
            ("alpha \ufeff beta", False, 1, 3),
            ("\ufeff\n", True, 1, 0),
            ("\ufeff\n", False, 1, 1),
        ):
            with self.subTest(text=text, strip_bom=strip_bom):
                self.assertEqual(textstats.count_text(text, strip_bom=strip_bom),
                                 textstats.TextStats(lines, words))

    def test_default_bom_policy_and_keyword_only_option(self):
        self.assertEqual(textstats.count_text("\ufeff"), textstats.TextStats(0, 0))
        parameter = inspect.signature(textstats.count_text).parameters["strip_bom"]
        self.assertEqual(parameter.kind, inspect.Parameter.KEYWORD_ONLY)
        self.assertIs(parameter.default, True)
        with self.assertRaises(TypeError):
            textstats.count_text("alpha", False)

    def test_api_is_silent_and_input_unchanged(self):
        text = "\ufeffalpha\r\nbeta"
        original = text
        stdout, stderr = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            for strip_bom in (True, False):
                result = textstats.count_text(text, strip_bom=strip_bom)
                self.assertIsInstance(result, textstats.TextStats)
            with self.assertRaises(ValueError):
                textstats.TextStats(-1, 0)
        self.assertEqual(text, original)
        self.assertEqual(stdout.getvalue(), "")
        self.assertEqual(stderr.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
