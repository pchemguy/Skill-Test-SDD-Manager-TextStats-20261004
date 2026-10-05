"""Pure whole-input counting and its immutable statistics value."""

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class TextStats:
    """Immutable nonnegative integer line and word counts.

    Args:
        lines: Number of CRLF, CR, or LF terminated lines and final segments.
        words: Number of whitespace-separated words.

    Raises:
        TypeError: A count is not an integer (booleans are rejected).
        ValueError: A count is negative.
    """

    lines: int
    words: int

    def __post_init__(self) -> None:
        for field in ("lines", "words"):
            value = getattr(self, field)
            if type(value) is not int:
                raise TypeError(f"{field} must be an integer")
            if value < 0:
                raise ValueError(f"{field} must be nonnegative")


def count_text(text: str, *, strip_bom: bool = True) -> TextStats:
    """Count a string without modifying it or emitting output.

    Args:
        text: The complete decoded input.
        strip_bom: Remove exactly one leading U+FEFF when true. Interior and
            subsequent BOMs remain ordinary non-whitespace characters.

    Returns:
        Immutable counts. Only CRLF, lone CR, and LF terminate lines; a
        nonempty final unterminated segment adds one line. Empty text has no
        lines, and trailing terminators add no phantom line. Words follow
        Python's Unicode whitespace splitting rules.
    """
    text = _normalize_text(text, strip_bom=strip_bom)
    # Normalizing CRLF first prevents its two characters counting twice.
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = normalized.count("\n")
    if normalized and not normalized.endswith("\n"):
        lines += 1
    return TextStats(lines, len(text.split()))


def _normalize_text(text: str, *, strip_bom: bool = True) -> str:
    """Apply the whole decoded input's BOM policy exactly once."""
    return text[1:] if strip_bom and text.startswith("\ufeff") else text


def _select_lines(text: str, start: int, end: int) -> str:
    """Select inclusive logical lines from already normalized decoded text.

    Preserve contents and CRLF/CR/LF terminators. Unicode separators are
    contents, and a trailing terminator does not create a phantom line.
    """
    selected = []
    offset = 0
    number = 1
    for match in re.finditer(r"\r\n|\r|\n", text):
        if start <= number <= end:
            selected.append(text[offset:match.end()])
        offset = match.end()
        number += 1
        if number > end:
            return "".join(selected)
    if offset < len(text) and start <= number <= end:
        selected.append(text[offset:])
    return "".join(selected)
