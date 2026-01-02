# ADR 0003: Standardize on Ruff for linting and formatting

- **Status:** Accepted
- **Date:** 2026-01-02

## Context
We want consistent Python style and automatic formatting.

## Decision
Use **Ruff** for:
- linting (`ruff check`)
- formatting (`ruff format`)

Configure Ruff in `pyproject.toml`. Run Ruff via `uv run -- ...` to ensure the pinned version
is used consistently.

## Consequences
- **Pros:** one tool for lint + format; _very fast_; simple configuration; fewer dependencies than
  multi-tool chains.
- **Cons:** some lint rules and formatter behaviors may differ from legacy toolchains; occasional
  rule tuning may be needed for specific projects.

## Alternatives considered
- Black + isort + flake8 (+ plugins) (common, but more tools/config and slower)
- pylint (powerful but heavier and noisier for many teams)
