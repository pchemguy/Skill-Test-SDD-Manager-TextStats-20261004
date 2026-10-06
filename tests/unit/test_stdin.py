"""Borrowed binary stdin success and decoded range composition."""

import contextlib
import io
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from textstats.cli import main


class StdinSuccessTests(unittest.TestCase):
    def test_borrowed_binary_input_and_selection(self):
        cases = [(b'alpha beta\r\ngamma\r', [], 'lines=2 words=3\n'),
                 (b'', [], 'lines=0 words=0\n'),
                 ('café\u2028tea\n'.encode(), [], 'lines=1 words=2\n'),
                 ('\ufeff\n'.encode(), [], 'lines=1 words=0\n'),
                 ('\ufeff\n'.encode(), ['--keep-bom'], 'lines=1 words=1\n'),
                 ('a\n\ufeff\nlast two'.encode(), ['--lines', '2:3'], 'lines=2 words=3\n'),
                 (b'a\r\nb c\rd\n', ['--lines=2:3'], 'lines=2 words=3\n'),
                 (b'a\n\n', ['--lines=2:99'], 'lines=1 words=0\n'),
                 (b'a\n', ['--lines=' + '9'*5000 + ':' + '9'*5000], 'lines=0 words=0\n'),
                 ('\ufeff\ufeff'.encode(), ['--lines=1:1'], 'lines=1 words=1\n')]
        for data, options, expected in cases:
            with self.subTest(options=[option[:60] for option in options], data=data):
                stream = io.BytesIO(data)
                out, err = io.StringIO(), io.StringIO()
                with patch('textstats.cli.sys.stdin', SimpleNamespace(buffer=stream)), \
                     patch('textstats.cli.count_file', side_effect=AssertionError('named-file acquisition')), \
                     patch('textstats.cli._read_text', side_effect=AssertionError('named-file acquisition')), \
                     contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                    status = main([*options, '-'])
                self.assertEqual((status, out.getvalue(), err.getvalue()), (0, expected, ''))
                self.assertFalse(stream.closed)
                self.assertEqual(stream.tell(), len(data))
