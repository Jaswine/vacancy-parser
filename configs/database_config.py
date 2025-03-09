from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager

DATABASE_URL = "postgresql+asyncpg://vacancy_parser:vacancy_parser@localhost:5432/vacancy_parser"

engine = create_async_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

@asynccontextmanager
async def get_db():
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()