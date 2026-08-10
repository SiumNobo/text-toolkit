# def count_words(text: str) -> dict[str, int]:
#     counts: dict[str, int] = {}
#     for word in text.split():
#         counts[word] = counts.get(word, 0) + 1
#     return counts


# from text_toolkit.exceptions import EmptyTextError


# def count_words(text: str) -> dict[str, int]:
#     if not text.strip():
#         raise EmptyTextError("text must not be empty")

#     counts: dict[str, int] = {}
#     for word in text.split():
#         counts[word] = counts.get(word, 0) + 1
#     return counts


import structlog

from text_toolkit.exceptions import EmptyTextError

logger = structlog.get_logger()


def count_words(text: str) -> dict[str, int]:
    if not text.strip():
        logger.error("empty_text_rejected")
        raise EmptyTextError("text must not be empty")

    counts: dict[str, int] = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts