# mistakes.md

- **Day 2**: `models.py` was accidentally named `model.py` (missing "s") — caused a
  NameError, then ImportError, then ModuleNotFoundError in a chain. Fixed by renaming
  the file to match the import statement exactly.

- **Day 3**: Retyping tests overwrote the whole file instead of appending — lost
  `test_count_words_simple` without noticing. Caught only because `collected 2 items`
  didn't match the expected 3.

- **Day 4**: `.env` got committed on the first attempt, before it was added to
  `.gitignore`. Caught before the push succeeded — fixed with `git rm --cached` +
  `commit --amend`. Rule: secrets files go in `.gitignore` before they're ever created.

- **Day 4**: `git push` failed with `ECONNREFUSED` on a stale VS Code socket, likely
  from the earlier WSL drive move. Fixed by fully closing and reopening VS Code.

- **Day 5**: Typer collapses to a single implicit command when only one `@app.command()`
  exists — running `text-toolkit stats file.txt` failed until `chunk` and `clean` were
  added, which restored normal command-name behavior.

- **Saturday**: `ruff format` exposed a real bug — `test_count_words_empty_string` had
  been silently broken since Day 4, when `count_words` started raising `EmptyTextError`
  instead of returning `{}`. The test was never updated to match. Lesson: re-run tests
  after every behavior change, not just when writing new code.

- **Saturday**: Committed `sample.txt` and later a full 720KB `pride_and_prejudice.txt`
  demo file into the repo unnecessarily. Not a security issue like `.env`, but the same
  underlying habit — scratch/demo data belongs in `.gitignore`, not the repo.