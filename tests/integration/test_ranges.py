"""Actual named-file module selection, validation and API regressions."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from textstats import TextStats, count_file

class RangeModuleTests(unittest.TestCase):
    def invoke(self,*args):
        return subprocess.run([sys.executable,'-m','textstats',*args],capture_output=True,text=True,
                              env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})

    def test_supplied_rows_spellings_and_order(self):
        rows=[('alpha beta\nbeta\nlast two','2:3',(2,3)),('alpha beta\nbeta\nlast two','2:99',(2,3)),
              ('alpha beta\nbeta\nlast two','1:1',(1,2)),('alpha beta\nbeta\nlast two','4:99',(0,0)),
              ('a\n\n','2:9',(1,0)),('a\r\nb c\rd\n','2:3',(2,3)),('', '1:9',(0,0)),
              ('\ufeff','1:1',(0,0)),('\ufeff\ufeff','1:1',(1,1)),('a\n\ufeff\n','2:2',(1,1)),
              ('a\u2028b\nlast','1:1',(1,2)),('a\r\n','2:3',(0,0))]
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'sample'
            for text,value,expected in rows:
                data=text.encode();path.write_bytes(data)
                for range_args in (['--lines',value],['--lines='+value]):
                    for options in (range_args,):
                        with self.subTest(text=text,value=value,options=options):
                            run=self.invoke(*options,str(path))
                            self.assertEqual((run.returncode,run.stderr),(0,''))
                            self.assertTrue(run.stdout.endswith('\n'))
                            self.assertEqual(run.stdout,f'lines={expected[0]} words={expected[1]}\n')
                            self.assertEqual(path.read_bytes(),data)
            path.write_bytes(b'alpha beta\nbeta\nlast two')
            self.assertEqual(count_file(path),TextStats(3,5))

    def test_huge_leading_zero_bom_dash_and_failures(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'-sample'
            path.write_bytes('\ufeff\nsecond two\n\ufeff\n'.encode())
            huge='9'*5000
            for value,expected in [('0002:0003','lines=2 words=3\n'),('2:'+huge,'lines=2 words=3\n'),(huge+':'+huge,'lines=0 words=0\n')]:
                run=self.invoke('--lines',value,'--',str(path));self.assertEqual((run.returncode,run.stdout,run.stderr),(0,expected,''))
            for options in (['--keep-bom','--lines=1:1'],['--lines','1:1','--keep-bom']):
                run=self.invoke(*options,str(path));self.assertEqual((run.returncode,run.stderr),(0,''));self.assertEqual(run.stdout,'lines=1 words=1\n')
            path.write_bytes(b'a\nsecond\xff')
            for options in (['--lines=1:1'],['--keep-bom','--lines=1:1']):
                run=self.invoke(*options,str(path));self.assertEqual((run.returncode,run.stdout),(1,''));self.assertIn(str(path),run.stderr);self.assertNotIn('Traceback',run.stderr)
                self.assertEqual(path.read_bytes(),b'a\nsecond\xff')
            for args,status in [(['--lines=1:1',str(path)+'missing'],1),(['--lines=2:1',str(path)+'missing'],2),(['--lines=1:1','--lines','1:2',str(path)],2)]:
                run=self.invoke(*args);self.assertEqual((run.returncode,run.stdout),(status,''));self.assertTrue(run.stderr);self.assertNotIn('Traceback',run.stderr)
