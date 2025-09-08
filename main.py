from fastapi import FastAPI
from configs.database_config import async_engine, base
from routes import account_routes

from models.account import Account
from models.filter import Filter
from models.link import Link
from models.link_list import LinkList
from models.parsing_log import ParsingLog
from models.subscribe import Subscribe

app = FastAPI(
    title='Vacancy parser',
    version='1.0.0'
)

@app.on_event("startup")
async def on_startup():
    # Create tables at startup (not for production – use Alembic)
    async with async_engine.begin() as conn:
        await conn.run_sync(base.metadata.create_all)

app.include_router(account_routes.router, prefix='/accounts', tags=['Accounts'])