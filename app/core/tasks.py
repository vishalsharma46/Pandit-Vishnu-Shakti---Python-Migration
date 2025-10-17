from unittest import result
from celery import Celery
from app.core.config import settings
import app.core.tasks

celery_app = Celery(
    "pandit_vishnu_shakti",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="Asia/Kolkata",
    enable_utc=True,
)

celery_app.autodiscover_tasks(["app.workers", "app.core"])

@celery_app.task(name="test.hello")
def hello_task(name: str):
    print(f"Hello, {name}! Task executed successfully.")
    return f"Hello, {name}!"

