"""Validate named-file arguments and render whole-input or selected counts."""

import argparse
import sys
from collections.abc import Sequence

from .io import count_file, _read_text
from .core import _normalize_text, _select_lines, count_text


def _parse_range(value: str) -> tuple[str, str]:
    """Validate unbounded ASCII decimals without integer-string conversion."""
    parts = value.split(":")
    if len(parts) != 2 or any(not p or any(c < "0" or c > "9" for c in p) for p in parts):
        raise argparse.ArgumentTypeError("lines must be positive ASCII START:END")
    start, end = (p.lstrip("0") for p in parts)
    if not start or not end or (len(start), start) > (len(end), end):
        raise argparse.ArgumentTypeError("lines require 1 <= START <= END")
    return start, end


class _SingleRange(argparse.Action):
    """Reject repeated options rather than accepting argparse's last value."""
    def __call__(self, parser, namespace, values, option_string=None):
        if getattr(namespace, self.dest) is not None:
            parser.error("--lines may be specified only once")
        setattr(namespace, self.dest, values)


def _available_endpoint(value: str, text_length: int) -> int:
    """Clamp only to an impossible line past EOF before safe conversion."""
    past_eof = text_length + 1
    limit = str(past_eof)
    return past_eof if (len(value), value) > (len(limit), limit) else int(value)


def main(argv: Sequence[str] | None = None) -> int:
    """Run the named-file CLI; argparse exits for help or invalid usage.

    Args:
        argv: Explicit arguments, or None to use process arguments.

    Returns:
        Zero after emitting exactly one line of successful text counts; one
        for named-file read/decode failures, with a diagnostic on stderr.

    Validation precedes acquisition. Expected OSError and UnicodeDecodeError
    failures identify the input without emitting partial counts or a traceback.
    """
    parser = argparse.ArgumentParser(prog="textstats", allow_abbrev=False,
                                     description="Count lines and words in a UTF-8 file.")
    parser.add_argument("--keep-bom", action="store_true", help="retain a leading BOM")
    parser.add_argument("--lines", type=_parse_range, action=_SingleRange,
                        metavar="START:END", help="select inclusive named-file logical lines")
    parser.add_argument("input", metavar="INPUT", help="named UTF-8 input file")
    args = parser.parse_args(argv)
    try:
        if args.lines is None:
            stats = count_file(args.input, strip_bom=not args.keep_bom)
        else:
            text = _normalize_text(_read_text(args.input), strip_bom=not args.keep_bom)
            start, end = (_available_endpoint(value, len(text)) for value in args.lines)
            stats = count_text(_select_lines(text, start, end), strip_bom=False)
    except (OSError, UnicodeDecodeError) as error:
        print(f"textstats: {args.input!r}: {error}", file=sys.stderr)
        return 1
    print(f"lines={stats.lines} words={stats.words}")
    return 0
