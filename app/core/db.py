from click import echo
from app.core.config import settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

if not settings.DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in settings.")

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Base = declarative_base()

async def get_ub():
    async with AsyncSessionLocal() as session:
        yield session