import logging
import sys
from venv import logger
from app.core.config import settings

try:
    import sentry_sdk
except ImportError:
    sentry_sdk = None

LOG_FORMAT = (
    "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
)

logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[
        logging.StreamHandler(sys.stdout)
    ],
)

if settings.SENTRY_DSN and sentry_sdk:
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        traces_sample_rate=1.0,
        environment=settings.ENVIRONMENT,
    )
    logger.info("Sentry initialized")
else:
    logger.info("Sentry not configured; using console logging only.")