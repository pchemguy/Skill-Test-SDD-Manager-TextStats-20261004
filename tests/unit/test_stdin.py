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


class StdinFailureTests(unittest.TestCase):
    def test_read_and_complete_decode_failures_are_atomic_and_borrowed(self):
        class Unreadable(io.BytesIO):
            def read(self, *args):
                raise OSError('injected read failure')

        for factory in (lambda: Unreadable(b'valid'), lambda: io.BytesIO(b'valid\nlate\xff')):
            for options in ([], ['--keep-bom'], ['--lines=1:1'],
                            ['--lines', '1:1', '--keep-bom'], ['--keep-bom', '--lines=1:1']):
                with self.subTest(options=options):
                    stream = factory()
                    out, err = io.StringIO(), io.StringIO()
                    with patch('textstats.cli.sys.stdin', SimpleNamespace(buffer=stream)), \
                         contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                        status = main([*options, '-'])
                    self.assertEqual((status, out.getvalue()), (1, ''))
                    self.assertIn('stdin', err.getvalue())
                    self.assertNotIn('Traceback', err.getvalue())
                    self.assertFalse(stream.closed)

    def test_invalid_usage_never_reads_either_source(self):
        from unittest.mock import Mock
        invalid = ['', ':1', '1:', '0:1', '1:0', '2:1', '-1:2', '+1:2', '1 :2',
                   '1:2:3', '١:٢', '１:２', '1:2\n', '9'*5000 + ':1']
        arguments = [['--lines=' + value, '-'] for value in invalid]
        arguments += [['--lines', '1:1', '--lines=1:2', '-'],
                      ['--lines=1:1', '--lines', '1:2', '-'],
                      ['--lines', '1:1', '--lines', '1:2', '-'],
                      ['--json', '-'], ['--lines=1:1', '--json', '-'],
                      ['--unknown', '-'], ['-', 'extra'], ['--lines']]
        for args in arguments:
            with self.subTest(args=[arg[:60] for arg in args]):
                stream = Mock()
                stream.read.side_effect = AssertionError('stdin acquired before validation')
                out, err = io.StringIO(), io.StringIO()
                with patch('textstats.cli.sys.stdin', SimpleNamespace(buffer=stream)), \
                     patch('textstats.cli.count_file') as count, patch('textstats.cli._read_text') as read, \
                     contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                    with self.assertRaises(SystemExit) as result:
                        main(args)
                self.assertEqual((result.exception.code, out.getvalue()), (2, ''))
                self.assertTrue(err.getvalue())
                stream.read.assert_not_called()
                count.assert_not_called()
                read.assert_not_called()
