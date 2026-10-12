# Team conventions

Practice repo: a small Python to-do CLI (`src/todo/`), used to practice a trunk-based team Git workflow.

## Workflow
- `main` is always releasable. Never push to it directly: open a PR.
- Branch from an up-to-date `main`: `feat/<topic>`, `fix/<topic>`, `chore/<topic>`.
- Branches are short-lived (hours, not days). One concern per PR, small diffs.
- Commits use Conventional Commits: `feat: ...`, `fix: ...`, `chore: ...`, `docs: ...`, `test: ...`, `refactor: ...`.
- Keep your branch current with `git pull --rebase origin main` (only on your own branch).
  Push rebased branches with `--force-with-lease`, never `--force`. Never rebase shared branches.
- PRs are squash-merged, so the PR title must be a conventional commit message.
- PR description: what changed, why, how it was tested.
- Never merge your own PR or push without being asked; the human maintainer reviews and merges.

## Checks (must pass before opening a PR; CI runs the same)
- `ruff check .`
- `pytest`

## Code
- Python >= 3.9. Code lives in `src/todo/`, tests in `tests/` (one test file per module).
- Add tests with every behaviour change. Touch only files related to your task.
