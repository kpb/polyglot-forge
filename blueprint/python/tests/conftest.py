from __future__ import annotations

import subprocess
from collections.abc import Iterator

import pytest


def _docker_is_available() -> bool:
    """Return True if docker CLI can talk to a daemon."""
    try:
        res = subprocess.run(
            ["docker", "info"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
            timeout=5,
        )
        return res.returncode == 0
    except Exception:
        return False


@pytest.fixture(scope="session")
def docker_available() -> bool:
    return _docker_is_available()


@pytest.fixture(autouse=True)
def _skip_integration_if_no_docker(
    request: pytest.FixtureRequest, docker_available: bool
) -> None:
    """If a test is marked integration, ensure docker is reachable."""
    if (
        request.node.get_closest_marker("integration") is not None
        and not docker_available
    ):
        pytest.skip("Docker is not available (required for integration tests)")


@pytest.fixture
def redis_client():
    from testcontainers.redis import RedisContainer

    with RedisContainer("redis:7-alpine") as c:
        yield c.get_client()
