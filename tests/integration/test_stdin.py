"""Actual stdin byte input remains independent of process text locale."""

import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


class StdinModuleTests(unittest.TestCase):
    def invoke(self, data, *options, cwd=None, env=None):
        return subprocess.run([sys.executable, '-m', 'textstats', *options, '-'],
                              input=data, capture_output=True, cwd=cwd, env=env)

    def test_success_bytes_locale_ranges_and_bom(self):
        environment = dict(os.environ, LC_ALL='C', LANG='C', PYTHONUTF8='0', PYTHONCOERCECLOCALE='0')
        cases = [(b'', [], b'lines=0 words=0\n'),
                 (b'alpha beta\r\ngamma\r', [], b'lines=2 words=3\n'),
                 ('café\u2028tea\n'.encode(), [], b'lines=1 words=2\n'),
                 ('\ufeff\n'.encode(), [], b'lines=1 words=0\n'),
                 ('a\n\ufeff\nlast two'.encode(), ['--lines', '2:3'], b'lines=2 words=3\n'),
                 (b'a\r\nb c\rd\n', ['--lines=2:3'], b'lines=2 words=3\n'),
                 (b'a\n', ['--lines=4:99'], b'lines=0 words=0\n')]
        for data, options, expected in cases:
            with self.subTest(data=data, options=options):
                run = self.invoke(data, *options, env=environment)
                self.assertEqual((run.returncode, run.stdout, run.stderr), (0, expected, b''))
        for options in (['--keep-bom', '--lines=1:1'], ['--lines', '1:1', '--keep-bom']):
            run = self.invoke('\ufeff\n'.encode(), *options, env=environment)
            self.assertEqual((run.returncode, run.stdout, run.stderr), (0, b'lines=1 words=1\n', b''))

    def test_literal_dash_file_is_distinct_from_stdin(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / '-'
            original = b'file two\n'
            path.write_bytes(original)
            environment = dict(os.environ, PYTHONPATH=str(Path.cwd()))
            run = subprocess.run([sys.executable, '-m', 'textstats', './-'], input=b'borrowed\n',
                                 cwd=directory, env=environment, capture_output=True)
            self.assertEqual((run.returncode, run.stdout, run.stderr), (0, b'lines=1 words=2\n', b''))
            self.assertEqual(path.read_bytes(), original)
