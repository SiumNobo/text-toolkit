class TextToolkitError(Exception):
    """Base error for all text-toolkit failures."""


class EmptyTextError(TextToolkitError):
    """Raised when text input is empty when it shouldn't be."""
