from select import select
from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from models.account import Account
from datetime import datetime

from utils.account_utils import is_email_checker
from utils.password_utils import get_password_hash


async def find_all_accounts(db: AsyncSession) -> list[Type[Account]]:
    """
        Retrieve all accounts from the database.
        :param db: Session - Database connection
        :return: List of Account objects
    """
    result = await db.execute(select(Account))
    return result.scalars().all()

async def find_account_by_id(db: AsyncSession, account_id: int) -> Account | None:
    """
        Retrieve an account by ID from the database.
        :param db: Session - Database connection
        :param account_id: int - ID of the account to retrieve
        :return: Account object
    """
    try:
        result = await db.execute(select(Account).where(Account.id == account_id))
        return result.scalars().first()
    except Exception as e:
        print(f"Error retrieving account by ID: {e}")

async def find_account_by_email_or_username(db: AsyncSession, param: str) -> Account | None:
    """
        Retrieve an account by email or username from the database.
        :param db: Session - Database connection
        :param param: str - Email or Username of the account to retrieve
        :return: Account object
    """
    try:
        if is_email_checker(param):
            result = await db.execute(select(Account).where(Account.email == param))
        else:
            result = await db.execute(select(Account).where(Account.username == param))
        return result.scalars().first()
    except Exception as e:
        print(f"Error retrieving account by ID: {e}")

async def create_account(db: AsyncSession, username: str, email: str, password: str) -> Account | None:
    """
        Create a new account
        :param db: Session - Database connection
        :param username: str - User's username
        :param email: str - User's email
        :param password: str - User's password
        :return: Account object
    """
    try:
        account =  Account(
            username=username,
            email=email,
            password=get_password_hash(password),
        )
        db.add(account)
        await db.commit()
        await db.refresh(account)
        return account
    except Exception as e:
        await db.rollback()
        print(f"Error creating account: {e}")

async def change_account_last_login_date_time(db: AsyncSession, account: Account) -> None:
    """
        Change account last_login date time
        :param db: Session - Database connection
        :param account: Account - Account
    """
    try:
        account.last_login = datetime.now()
        await db.commit()
        await db.refresh(account)
    except Exception as e:
        await db.rollback()
        print(f"Error updating last login field account: {e}")
