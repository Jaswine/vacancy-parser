from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
import os

# PostgreSQL
# DATABASE_URL = "postgresql+asyncpg://vacancy_parser:vacancy_parser@localhost:5432/vacancy_parser"

# SQLite
DATABASE_URL = "sqlite+aiosqlite:///./test.db"

async_engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Each request will use this async session
async_session_local = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)

# sync engine (для Alembic)
sync_engine = create_engine(DATABASE_URL.replace("aiosqlite", "pysqlite"), echo=True, future=True)

base = declarative_base()

# Dependency for FastAPI
async def get_db() -> AsyncGenerator[Any, Any]:
    async with async_session_local() as session:
        yield session