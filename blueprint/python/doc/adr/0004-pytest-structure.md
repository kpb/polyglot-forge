# ADR 0004: Pytest testing structure with unit/integration split and Testcontainers

- **Status:** Accepted
- **Date:** 2026-01-02

## Context
We need a testing approach that scales from tiny libraries to service code, supports CI, and keeps fast feedback
loops. Integration tests should validate real service boundaries without requiring shared external infrastructure.

## Decision
Adopt **pytest** with a standard layout and marker:
- `tests/unit/` for unit tests
- `tests/integration/` for integration tests
- mark integration tests with `@pytest.mark.integration`
- run integration tests explicitly (e.g., `pytest -m integration` / `make test-integration`)

Use **Testcontainers** for integration tests that require external services. Provide a trivial
Redis container test as the reference pattern.

## Consequences
- **Pros:** unit tests stay fast and default; integration tests are explicit; containers provide
  realistic dependencies without manual setup; works well in CI/devcontainers.
- **Cons:** integration tests require Docker access; can be slower; occasional platform/network
  quirks when running Docker inside containers.

## Alternatives considered
- Mocking external services (fast, but weaker confidence for integration boundaries)
- Local shared services (more operational burden; harder to keep deterministic across dev/CI)
- docker-compose for tests (works, but more bespoke orchestration and lifecycle handling)
