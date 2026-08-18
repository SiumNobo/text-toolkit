# text-toolkit

A command-line tool for word counting, text chunking, and cleaning —
built from scratch to practice production Python patterns: type-safe
config, structured logging, custom exceptions, and tested CLI commands.

## Install

```bash
git clone https://github.com/SiumNobo/text-toolkit.git
cd text-toolkit
uv pip install -e .
```

## Usage

```bash
text-toolkit stats myfile.txt
text-toolkit chunk myfile.txt --size 500 --overlap 50
text-toolkit clean myfile.txt
```

## Design Decisions

- **src/ layout** — forces an editable install, so tests run against
  the real installed package, not whatever's sitting in the working directory.
- **Pydantic for ChunkConfig** — rejects invalid chunk settings
  (like overlap >= size) at the point of creation, not deep inside chunking logic.
- **Custom exceptions** — `EmptyTextError` names a failure specifically,
  instead of crashing with a generic Python error. The error message alone
  tells you what went wrong, without needing to read the code that raised it.
- **structlog over print()** — every log line carries a timestamp and a
  severity level automatically, and can be filtered or searched later —
  something a plain `print()` statement can't do.

## What I'd Do Differently

Write tests alongside each feature the moment it's built, not after —
one test (`test_count_words_empty_string`) silently broke for a full day
when `count_words`'s error-handling changed, and nothing caught it until
the next full test run.