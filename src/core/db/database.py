import asyncio
import logging

from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    async_sessionmaker,
)

from src.core.configs.config import settings
from src.core.db.models.base import Base

logger = logging.getLogger(__name__)


engine: AsyncEngine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,  # Dev
    future=True,
    pool_pre_ping=True,
    pool_size=10,  # Maximum connections
    max_overflow=20,  # Additional connections as needed
)

async_session_local = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False,
)

# sync engine (для Alembic)
# sync_engine = create_engine(settings.DATABASE_URL.replace("aiosqlite", "pysqlite"), echo=True, future=True)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Dependency for FastAPI
async def get_db() -> AsyncGenerator[Any, Any]:
    async with async_session_local() as session:
        yield session


async def main():
    logger.info("📦 Initializing database...")
    try:
        await init_db()
        logger.info("✅ Database initialized successfully")
    except Exception as e:
        logger.info(f"❌ Database initialization error: {e}")
        import traceback

        traceback.print_exc()
    finally:
        await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
