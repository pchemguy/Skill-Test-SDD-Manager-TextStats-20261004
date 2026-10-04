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
