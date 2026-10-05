"""Acquire complete named-file bytes without newline translation."""

import os

from .core import TextStats, count_text


def count_file(path: str | os.PathLike[str], *, strip_bom: bool = True) -> TextStats:
    """Count a UTF-8 file silently, leaving its bytes unchanged.

    Args:
        path: String or filesystem path to the named input.
        strip_bom: Remove exactly one leading BOM before counting.

    Returns:
        Immutable line/word counts using count_text's CR/LF and Unicode rules.

    Raises:
        OSError: The file cannot be opened or read.
        UnicodeDecodeError: Complete input is not valid UTF-8.

    The owned binary handle closes before counting; no caller stream is owned.
    """
    return count_text(_read_text(path), strip_bom=strip_bom)


def _read_text(path: str | os.PathLike[str]) -> str:
    """Decode complete named-file bytes strictly, closing the owned handle."""
    with open(path, "rb") as source:
        return source.read().decode("utf-8")
