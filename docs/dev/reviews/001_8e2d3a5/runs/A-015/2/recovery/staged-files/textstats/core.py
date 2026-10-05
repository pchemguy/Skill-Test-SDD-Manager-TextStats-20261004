"""Pure string statistics with no acquisition, rendering or process state."""

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class TextStats:
    """Immutable nonnegative integer line and word totals.

    Attributes:
        lines: Number of CRLF, CR and LF logical lines.
        words: Number of Unicode-whitespace-separated words.

    Raises:
        TypeError: A count is not an integer.
        ValueError: A count is negative.
    """

    lines: int
    words: int

    def __post_init__(self) -> None:
        for name, value in (("lines", self.lines), ("words", self.words)):
            if not isinstance(value, int):
                raise TypeError(f"{name} must be an integer")
            if value < 0:
                raise ValueError(f"{name} must be nonnegative")


def count_text(text: str, *, strip_bom: bool = True) -> TextStats:
    """Count a whole string silently, leaving the caller's input unchanged.

    CRLF is one terminator; lone CR and LF also terminate lines. A nonempty
    final unterminated segment counts once. Other Unicode separators affect
    words via str.split(), but do not terminate lines. A retained BOM is an
    ordinary non-whitespace character.

    Args:
        text: Complete decoded caller text.
        strip_bom: Remove exactly one initial U+FEFF when true (the default).
            Interior BOMs and a second initial BOM remain.

    Returns:
        Immutable nonnegative integer line and word totals.
    """
    if strip_bom and text.startswith("\ufeff"):
        text = text[1:]
    lines = len(re.findall(r"\r\n|\r|\n", text))
    if text and not text.endswith(("\r", "\n")):
        lines += 1
    return TextStats(lines=lines, words=len(text.split()))
