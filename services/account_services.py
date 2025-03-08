from typing import Type

from sqlalchemy.orm import Session
from models.account import Account
from datetime import datetime


def find_all_accounts(db: Session) -> list[Type[Account]]:
    """
        Retrieve all accounts from the database.
        :param db: Session - The database connection
        :return: List of Account objects
    """
    return db.query(Account).all()

def find_account_by_id(db: Session, account_id: int) -> Type[Account] | None:
    """
        Retrieve an account by ID from the database.
        :param db: Session - The database connection
        :param account_id: int - The ID of the account to retrieve
        :return: Account object
    """
    try:
        return db.query(Account).filter(Account.id == account_id).first()
    except Exception as e:
        print(f"Error retrieving account by ID: {e}")
        return None

def find_account_by_username(db: Session, username: str) -> Type[Account] | None:
    """
        Retrieve an account by username from the database.
        :param db: Session - The database connection
        :param username: str - The username of the account to retrieve
        :return: Account object
    """
    try:
        return db.query(Account).filter(Account.username == username).first()
    except Exception as e:
        print(f"Error retrieving account by ID: {e}")
        return None

def sign_in_account(db: Session,
                    username: str, password: str) -> Type[Account] | None:
    """
        Sign in an account using the provided username and password.
        :param db: Session - The database connection
        :param username: str - The username of the account
        :param password: str - The password of the account
    """
    try:
        account = find_account_by_username(db, username)

        if account and account.verify_password(password):
            account.last_login = datetime.now()
            db.commit()

        if account:
            account.last_login = datetime.now()
            db.commit()
        return account
    except Exception as e:
        print(f"Error signing in account: {e}")
        return None