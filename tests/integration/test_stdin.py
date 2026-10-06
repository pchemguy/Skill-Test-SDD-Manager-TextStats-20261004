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

    def test_complete_decode_failure_is_atomic_for_all_option_orders(self):
        for options in ([], ['--keep-bom'], ['--lines=1:1'],
                        ['--lines', '1:1', '--keep-bom'], ['--keep-bom', '--lines=1:1']):
            run = self.invoke(b'valid\nlate\xff', *options)
            self.assertEqual((run.returncode, run.stdout), (1, b''))
            self.assertIn(b'stdin', run.stderr)
            self.assertNotIn(b'Traceback', run.stderr)

    def test_objective_selection_rows_and_option_orders(self):
        rows = [('alpha beta\nbeta\nlast two', '2:3', (2, 3), (2, 3)),
                ('alpha beta\nbeta\nlast two', '1:1', (1, 2), (1, 2)),
                ('alpha beta\nbeta\nlast two', '4:99', (0, 0), (0, 0)),
                ('a\n\n', '2:9', (1, 0), (1, 0)),
                ('a\r\nb c\rd\n', '2:3', (2, 3), (2, 3)),
                ('', '1:9', (0, 0), (0, 0)),
                ('\ufeff', '1:1', (0, 0), (1, 1)),
                ('\ufeff\ufeff', '1:1', (1, 1), (1, 1)),
                ('a\n\ufeff\n', '2:2', (1, 1), (1, 1)),
                ('a\u2028b\nlast', '1:1', (1, 2), (1, 2)),
                ('a\nb c', '0002:0003', (1, 2), (1, 2)),
                ('a\n', '9'*5000 + ':' + '9'*5000, (0, 0), (0, 0))]
        for text, bounds, stripped, retained in rows:
            for options, counts in [(['--lines', bounds], stripped),
                                    (['--lines=' + bounds], stripped),
                                    (['--keep-bom', '--lines', bounds], retained),
                                    (['--lines=' + bounds, '--keep-bom'], retained)]:
                with self.subTest(text=text, bounds=bounds[:60], options=options[0]):
                    run = self.invoke(text.encode('utf-8'), *options)
                    expected = f'lines={counts[0]} words={counts[1]}\n'.encode()
                    self.assertEqual((run.returncode, run.stdout, run.stderr), (0, expected, b''))

    def test_stdin_usage_failures_have_no_success_output(self):
        for options in (['--lines=1:0'], ['--lines=٢:٣'], ['--lines', '1:1', '--lines=2:3'],
                        ['--json'], ['--lines=1:1', '--json'], ['--unknown']):
            run = self.invoke(b'\xff', *options)
            self.assertEqual((run.returncode, run.stdout), (2, b''))
            self.assertTrue(run.stderr)
            self.assertNotIn(b'Traceback', run.stderr)
