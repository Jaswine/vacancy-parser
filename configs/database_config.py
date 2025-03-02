from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://vacancy_parser:vacancy_parser@localhost:5432/vacancy_parser"

engine = create_async_engine(DATABASE_URL, echo=True)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
