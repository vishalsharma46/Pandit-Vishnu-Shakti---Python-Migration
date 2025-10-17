from idna import encode
from app.core.config import settings
import redis.asyncio as redis

redis_client = redis.from_url(
    settings.REDIS_URL,
    encoding="utf-8",
    decode_responses=True,
)

async def test_redis_connection():
    try:
        pong = await redis_client.ping()
        if pong:
            print("Redis connection successful")
        else:
            print("Redis connection failed")
    except Exception as e:
        print(f"Redis error: {e}")