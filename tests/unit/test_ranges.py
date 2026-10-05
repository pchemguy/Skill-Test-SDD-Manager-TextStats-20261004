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
