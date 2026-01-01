import pytest
import redis


@pytest.mark.integration
def test_redis_container_ping(redis_client: redis.Redis):
        assert redis_client.ping()
