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
