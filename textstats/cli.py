"""Validate named-file arguments and render complete text or JSON counts."""

import argparse
import json
import sys
from collections.abc import Sequence

from .io import count_file


def main(argv: Sequence[str] | None = None) -> int:
    """Run the named-file CLI; argparse exits for help or invalid usage.

    Args:
        argv: Explicit arguments, or None to use process arguments.

    Returns:
        Zero after emitting exactly one line of successful text or JSON counts; one
        for named-file read/decode failures, with a diagnostic on stderr.

    Validation precedes acquisition. Expected OSError and UnicodeDecodeError
    failures identify the input without emitting partial counts or a traceback.
    """
    parser = argparse.ArgumentParser(prog="textstats", allow_abbrev=False,
                                     description="Count lines and words in a UTF-8 file.")
    parser.add_argument("--json", action="store_true", help="emit JSON counts")
    parser.add_argument("--keep-bom", action="store_true", help="retain a leading BOM")
    parser.add_argument("input", metavar="INPUT", help="named UTF-8 input file")
    args = parser.parse_args(argv)
    try:
        stats = count_file(args.input, strip_bom=not args.keep_bom)
    except (OSError, UnicodeDecodeError) as error:
        print(f"textstats: {args.input!r}: {error}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps({"lines": stats.lines, "words": stats.words}))
    else:
        print(f"lines={stats.lines} words={stats.words}")
    return 0
