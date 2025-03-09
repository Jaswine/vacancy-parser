import asyncio
from logging.config import fileConfig
from sqlalchemy.ext.asyncio import create_async_engine, AsyncConnection

from alembic import context

from configs.database_config import engine
from models.base import Base
from sqlalchemy import pool

from models.account import Account
from models.filter import Filter
from models.link import Link
from models.link_list import LinkList
from models.parsing_log import ParsingLog
from models.subscribe import Subscribe


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config
if config.config_file_name:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.
database_url = config.get_main_option("sqlalchemy.url")

connectable = create_async_engine(database_url, future=True)

engine = create_async_engine(database_url, echo=True, poolclass=pool.NullPool)

async def run_migrations():
    """Run migrations in async mode."""
    async with engine.begin() as connection:
        await connection.run_sync(do_run_migrations)

def do_run_migrations(connection):
    """Synchronous migration runner."""
    context.configure(connection=connection, target_metadata=Base.metadata)

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations using asyncio."""
    asyncio.run(run_migrations())

# Run migrations
if context.is_offline_mode():
    context.configure(url=database_url, target_metadata=Base.metadata)
    with context.begin_transaction():
        context.run_migrations()
else:
    run_migrations_online()

