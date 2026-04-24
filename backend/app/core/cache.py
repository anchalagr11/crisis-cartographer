import redis
from .config import settings

redis_client = redis.from_url(settings.redis_url)


def get_cache():
    return redis_client
