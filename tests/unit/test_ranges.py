"""Decoded selection preserves logical lines and normalizes the BOM once."""
import contextlib
import io
import tempfile
from pathlib import Path
import unittest
from unittest.mock import patch
import textstats
from textstats import TextStats, count_text, count_file
from textstats import core


class SelectionTests(unittest.TestCase):
    def test_selection_contract(self):
        self.assertTrue(hasattr(core, '_select_lines'), 'selection seam missing')
        rows=[('alpha beta\nbeta\nlast two',2,3,'beta\nlast two'),
              ('alpha beta\nbeta\nlast two',2,99,'beta\nlast two'),
              ('alpha beta\nbeta\nlast two',1,1,'alpha beta\n'),
              ('alpha beta\nbeta\nlast two',4,99,''),
              ('a\n\n',2,9,'\n'),('a\r\nb c\rd\n',2,3,'b c\rd\n'),
              ('',1,9,''),('a\u2028b\nlast',1,1,'a\u2028b\n'),
              ('a\n\ufeff\n',2,2,'\ufeff\n'),('a\r\n',2,3,'')]
        for text,start,end,expected in rows:
            with self.subTest(text=text,start=start,end=end):
                self.assertEqual(core._select_lines(text,start,end),expected)

    def test_normalization_once_and_whole_api(self):
        self.assertTrue(hasattr(core, '_normalize_text'), 'normalization seam missing')
        for text,keep,expected in [('\ufeff',False,TextStats(0,0)),('\ufeff',True,TextStats(1,1)),
                                   ('\ufeff\ufeff',False,TextStats(1,1)),('a\n\ufeff\n',False,TextStats(1,1))]:
            normalized=core._normalize_text(text,strip_bom=not keep)
            selected=core._select_lines(normalized,2 if text.startswith('a') else 1,2)
            self.assertEqual(count_text(selected,strip_bom=False),expected)
        self.assertEqual(textstats.__all__,['TextStats','count_text','count_file'])
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'sample'
            data=b'alpha beta\r\ngamma\r'
            path.write_bytes(data)
            out,err=io.StringIO(),io.StringIO()
            with contextlib.redirect_stdout(out),contextlib.redirect_stderr(err):
                self.assertEqual(count_file(path),TextStats(2,3))
            self.assertEqual((out.getvalue(),err.getvalue()),('',''))
            self.assertEqual(path.read_bytes(),data)

class RangeValidationTests(unittest.TestCase):
    def test_invalid_usage_before_either_acquisition(self):
        from textstats.cli import main
        huge='9'*5000
        invalid=['','0:1','1:0','2:1','1:',' :2',':2','+1:2','-1:2','1: 2','1:2 ','١:2','1:２','1:2:3','1.0:2',huge+':1',huge+':'+('8'*5000)]
        arguments=[['--lines='+value,'missing'] for value in invalid]
        arguments += [['--lines'],['--lines','missing'],['--lines','1:2','--lines','2:3','missing'],
                      ['--lines=1:2','--lines=2:3','missing'],['--lines','1:2','--lines=2:3','missing']]
        for args in arguments:
            with self.subTest(args=[a[:50] for a in args]):
                out,err=io.StringIO(),io.StringIO()
                with patch('textstats.cli.count_file',side_effect=AssertionError('acquired')) as whole,patch('textstats.io.open',side_effect=AssertionError('opened')) as opened:
                    with contextlib.redirect_stdout(out),contextlib.redirect_stderr(err):
                        with self.assertRaises(SystemExit) as result:main(args)
                self.assertEqual(result.exception.code,2)
                self.assertEqual(out.getvalue(),'')
                self.assertTrue(err.getvalue())
                self.assertNotIn('Traceback',err.getvalue())
                whole.assert_not_called();opened.assert_not_called()

class RangeResourceTests(unittest.TestCase):
    def test_owned_handle_closes_on_range_success_and_failure(self):
        from textstats.cli import main
        for data,status in [(b'a\r\nb c\r',0),(b'a\nlate\xff',1)]:
            handle=io.BytesIO(data)
            out,err=io.StringIO(),io.StringIO()
            with patch('textstats.io.open',return_value=handle):
                with contextlib.redirect_stdout(out),contextlib.redirect_stderr(err):
                    actual=main(['--lines=1:1','sample'])
            self.assertEqual(actual,status)
            self.assertTrue(handle.closed)
            self.assertEqual(out.getvalue(),'lines=1 words=1\n' if status==0 else '')
        for error in [PermissionError('denied'),OSError('read failed')]:
            out,err=io.StringIO(),io.StringIO()
            with patch('textstats.cli._read_text',side_effect=error):
                with contextlib.redirect_stdout(out),contextlib.redirect_stderr(err):
                    self.assertEqual(main(['--lines=1:1','sample']),1)
            self.assertEqual(out.getvalue(),'');self.assertIn('sample',err.getvalue());self.assertNotIn('Traceback',err.getvalue())
