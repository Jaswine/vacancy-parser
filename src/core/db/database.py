import asyncio, logging

from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

from src.core.configs.config import settings


logger = logging.getLogger(__name__)


engine: AsyncEngine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,           # Dev
    future=True,
    pool_pre_ping=True,
    pool_size=10,        # Maximum connections
    max_overflow=20      # Additional connections as needed
)

async_session_local = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)

# sync engine (для Alembic)
# sync_engine = create_engine(settings.DATABASE_URL.replace("aiosqlite", "pysqlite"), echo=True, future=True)

Base = declarative_base()

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