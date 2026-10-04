"""Public interfaces for whole-input text statistics."""

from .core import TextStats, count_text
from .io import count_file

__all__ = ["TextStats", "count_text", "count_file"]
