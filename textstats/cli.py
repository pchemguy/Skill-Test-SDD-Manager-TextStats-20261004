"""Validate named-file arguments and render complete text counts."""

import argparse
from collections.abc import Sequence

from .io import count_file


def main(argv: Sequence[str] | None = None) -> int:
    """Run the named-file CLI; argparse exits for help or invalid usage.

    Args:
        argv: Explicit arguments, or None to use process arguments.

    Returns:
        Zero after emitting exactly one line of successful text counts.

    Validation precedes acquisition. Expected acquisition-error diagnostics
    are completed at the later reliability milestone.
    """
    parser = argparse.ArgumentParser(prog="textstats", allow_abbrev=False,
                                     description="Count lines and words in a UTF-8 file.")
    parser.add_argument("--keep-bom", action="store_true", help="retain a leading BOM")
    parser.add_argument("input", metavar="INPUT", help="named UTF-8 input file")
    args = parser.parse_args(argv)
    stats = count_file(args.input, strip_bom=not args.keep_bom)
    print(f"lines={stats.lines} words={stats.words}")
    return 0
