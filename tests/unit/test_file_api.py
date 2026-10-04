"""Owned success-path file lifecycle."""

import io
import unittest
from unittest.mock import patch

import textstats


class FileLifecycleTests(unittest.TestCase):
    def test_success_closes_owned_handle(self):
        self.assertTrue(hasattr(textstats, "count_file"), "count_file public export missing")
        handle = io.BytesIO(b"one\r\ntwo")
        with patch("builtins.open", return_value=handle):
            self.assertEqual(textstats.count_file("owned"), textstats.TextStats(2, 2))
        self.assertTrue(handle.closed)

class FileFailureTests(unittest.TestCase):
    def test_open_failure_is_silent_and_preserves_exception(self):
        import contextlib
        for strip_bom in (True, False):
            error = PermissionError("unreadable")
            out, err = io.StringIO(), io.StringIO()
            with patch("builtins.open", side_effect=error):
                with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                    with self.assertRaises(PermissionError) as caught:
                        textstats.count_file("owned", strip_bom=strip_bom)
            self.assertIs(caught.exception, error)
            self.assertEqual((out.getvalue(), err.getvalue()), ("", ""))

    def test_read_decode_and_close_failure_are_atomic_and_close_owned_handle(self):
        import contextlib

        class BrokenRead(io.BytesIO):
            def read(self, *args):
                raise OSError("read failed")

        class BrokenClose(io.BytesIO):
            def close(self):
                super().close()
                raise OSError("close failed")

        for strip_bom in (True, False):
            for handle, expected in [(BrokenRead(b"valid"), OSError),
                                     (io.BytesIO(b"valid prefix\n\xff"), UnicodeDecodeError),
                                     (BrokenClose(b"valid"), OSError)]:
                with self.subTest(strip_bom=strip_bom, expected=expected, handle=type(handle)):
                    out, err = io.StringIO(), io.StringIO()
                    with patch("builtins.open", return_value=handle):
                        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                            with self.assertRaises(expected):
                                textstats.count_file("owned", strip_bom=strip_bom)
                    self.assertTrue(handle.closed)
                    self.assertEqual((out.getvalue(), err.getvalue()), ("", ""))
