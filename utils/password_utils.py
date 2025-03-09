from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from passlib.context import CryptContext

SECRET_KEY = 'your_secret_key'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_tokens(data: dict) -> dict[str, str]:
    """
        Generate both access and refresh tokens
        :param data: dict - payload for JWT
        :return: dict - access and refresh tokens
    """
    to_encode = data.copy()

    # Generate Access Token (expires in 30 minutes)
    access_expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwt.encode({**to_encode, 'exp': access_expire}, SECRET_KEY, algorithm=ALGORITHM)

    # Generate Refresh Token (expires in 7 days)
    refresh_expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    refresh_token = jwt.encode({**to_encode, 'exp': refresh_expire}, SECRET_KEY, algorithm=ALGORITHM)

    return {'access_token': access_token, 'refresh_token': refresh_token}

def refresh_access_token(refresh_token: str) -> dict[str, str] | ValueError:
    """
        Refresh the access token if the refresh token is valid.
        :param refresh_token: str - JWT refresh token
        :return: str - new access token
    """
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        new_access_token = create_tokens({"sub": payload["sub"]})["access_token"]
        return {"access_token": new_access_token}
    except JWTError:
        raise ValueError("Invalid refresh token")
