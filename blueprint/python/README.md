# Python blueprint (uv + ruff + pytest)

This is a copyable Python starter blueprint.

## What you get
- `uv`-managed project workflow (sync/lock/run)
- `ruff` for linting + formatting
- `pytest` for tests
- `src/` layout
- Makefile targets for common ops
- Unit & integration test folders with a sample testcontainers fixture
- Dev-container setup for vscode

## Quick start (after copying this blueprint into a new project dir)
1. Rename the package:
   - `src/example_pkg` -> `src/<your_pkg>`
   - Update `pyproject.toml`:
     - `project.name`
     - `tool.ruff.src` (optional)
2. Run:
   - `make init`
   - `make test`

## Day-to-day
- `make fmt`
- `make lint`
- `make test`

## Notes
- `uv.lock` will be generated the first time you `uv sync` / `uv run` / `uv lock`.
  Commit it for reproducible installs.

## Pre-commit (Ruff on commit)

This repo uses `pre-commit` to run Ruff automatically when you `git commit`.

**One-time setup (from `blueprint/python/`):**

```bash
uv add --dev pre-commit
make sync
make hooks-install
```

**Run hooks manually**
On staged files (matches commit behavior):
```bash
make hooks-run-staged
```

**On all files:**

```bash
make hooks-run
```

**Update hook versions**

```bash
make hooks-update
```

**Notes**

The hook config lives at the repo root: .pre-commit-config.yaml

Ruff is run using the blueprint’s config: blueprint/python/pyproject.toml
