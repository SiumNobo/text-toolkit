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

### Alternative: using venv + pip

If you don't have `uv` installed:

```bash
git clone https://github.com/SiumNobo/text-toolkit.git
cd text-toolkit
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

Note: `pip install -e .` installs runtime dependencies only
(`pydantic`, `pydantic-settings`, `structlog`, `typer`). Development
tools (pytest, mypy, ruff) are managed via `uv`'s dependency groups
and may need manual installation with plain `pip`.

## Usage

```bash
text-toolkit stats myfile.txt
text-toolkit chunk myfile.txt --size 500 --overlap 50
text-toolkit clean myfile.txt
```

## Real-World Test

Ran against Jane Austen's *Pride and Prejudice* (Project Gutenberg, ~720KB):

## Real-World Test

Ran against Jane Austen's *Pride and Prejudice* (Project Gutenberg, ~720KB):

```bash
curl -o pride_and_prejudice.txt https://www.gutenberg.org/files/1342/1342-0.txt
uv run text-toolkit stats pride_and_prejudice.txt
```

```
Total unique words: 14160
```
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