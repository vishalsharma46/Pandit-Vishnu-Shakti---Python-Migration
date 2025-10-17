from dotenv import load_dotenv
import os

load_dotenv()

class Settings():

    APP_NAME = 'Pandit Vishnu Shakti AI Bot'
    PORT = int(os.getenv("PORT", 3100))
    DATABASE_URL = os.getenv("DATABASE_URL")
    REDIS_URL = os.getenv("REDIS_URL")
    REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
    SENTRY_DSN = os.getenv("SENTRY_DSN")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")


settings = Settings()

