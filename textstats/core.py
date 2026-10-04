"""Pure whole-input counting and its immutable statistics value."""

from dataclasses import dataclass


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
    if strip_bom and text.startswith("\ufeff"):
        text = text[1:]
    # Normalizing CRLF first prevents its two characters counting twice.
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = normalized.count("\n")
    if normalized and not normalized.endswith("\n"):
        lines += 1
    return TextStats(lines, len(text.split()))
