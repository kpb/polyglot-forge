# ADR 0002: Use uv for Python dependency management and task execution

- **Status:** Accepted
- **Date:** 2026-01-02

## Context
We want a fast, reproducible, low-friction Python workflow across developer machines, CI, and devcontainers. The
monorepo will host multiple languages, so Python tooling should be:
- straightforward to bootstrap
- deterministic (lockfile-driven)
- quick to run (common tasks: sync, test, lint, format)

## Decision
Use **uv** as the standard for Python:
- `uv venv` / `uv sync` to create and synchronize environments
- `uv lock` to produce `uv.lock`
- `uv run -- <cmd>` to execute tools in the project environment

Commit `uv.lock` in real projects (templates/blueprints ignore it to avoid stale pins).

## Consequences
- **Pros:** fast installs; reproducible environments via lockfile; fewer “works on my machine”
  issues; consistent task execution (`uv run`) without manual venv activation.
- **Cons:** adds a non-stdlib tool dependency; team must learn uv conventions; lockfile format
  differs from other ecosystems.

## Alternatives considered
- `pip` + `venv` + `requirements*.txt` (more manual; slower; weaker reproducibility)
- `pip-tools` (good reproducibility, but more moving parts and workflow steps)
- Poetry / PDM (feature-rich, but heavier; different ergonomics; may be slower for day-to-day)
