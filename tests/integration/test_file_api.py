"""Named-file success contracts against unchanged real UTF-8 bytes."""

import contextlib
import inspect
import io
from pathlib import Path
import tempfile
import unittest

import textstats


class FileApiTests(unittest.TestCase):
    def test_public_export_and_signature(self):
        self.assertTrue(hasattr(textstats, "count_file"), "count_file public export missing")
        signature = inspect.signature(textstats.count_file)
        self.assertEqual(list(signature.parameters), ["path", "strip_bom"])
        self.assertEqual(signature.parameters["strip_bom"].kind, inspect.Parameter.KEYWORD_ONLY)
        self.assertIs(signature.parameters["strip_bom"].default, True)

    def test_real_files_paths_bom_terminators_and_silence(self):
        self.assertTrue(hasattr(textstats, "count_file"), "count_file public export missing")
        cases = [(b"", (0, 0)), (b"alpha beta", (1, 2)),
                 (b"alpha\r\nbeta\rgamma\n", (3, 3)), (b"\n\n", (2, 0)),
                 ("café\u2028tea".encode(), (1, 2)),
                 ("\ufeff".encode(), (0, 0)), ("\ufeff\ufeff".encode(), (1, 1))]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.txt"
            for data, counts in cases:
                for path_arg in (path, str(path)):
                    with self.subTest(data=data, path_type=type(path_arg)):
                        path.write_bytes(data)
                        out, err = io.StringIO(), io.StringIO()
                        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                            result = textstats.count_file(path_arg)
                        self.assertEqual(result, textstats.TextStats(*counts))
                        self.assertEqual(path.read_bytes(), data)
                        self.assertEqual((out.getvalue(), err.getvalue()), ("", ""))
            path.write_bytes("\ufeff".encode())
            self.assertEqual(textstats.count_file(path, strip_bom=False), textstats.TextStats(1, 1))
