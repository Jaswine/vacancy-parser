from __future__ import annotations

from functools import lru_cache

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class CoreSettings(BaseSettings):
    """
    Application settings loaded from .env
    """

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="ignore")

    # PostgreSQL
    DB_HOST: SecretStr
    DB_PORT: SecretStr
    DB_USER: SecretStr
    DB_PASSWORD: SecretStr
    DB_NAME: SecretStr

    @property
    def DATABASE_URL_SYNC(self) -> str:
        # Sync URL form Alembic
        return (
            f"postgresql://"
            f"{self.DB_USER.get_secret_value()}:"
            f"{self.DB_PASSWORD.get_secret_value()}@"
            f"{self.DB_HOST.get_secret_value()}:"
            f"{self.DB_PORT.get_secret_value()}/"
            f"{self.DB_NAME.get_secret_value()}"
        )

    @property
    def DATABASE_URL_ASYNC(self) -> str:
        # Async URL for asyncpg / async SQLAlchemy
        return (
            f"postgresql+asyncpg://"
            f"{self.DB_USER.get_secret_value()}:"
            f"{self.DB_PASSWORD.get_secret_value()}@"
            f"{self.DB_HOST.get_secret_value()}:"
            f"{self.DB_PORT.get_secret_value()}/"
            f"{self.DB_NAME.get_secret_value()}"
        )

    # Redis
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: SecretStr | None = None
    REDIS_DB: int = 0  # db number

    # Kafka
    KAFKA_BOOTSTRAP_SERVERS: SecretStr | None = "localhost:9092"

    # RabbitMQ
    RABBITMQ_HOST: str = "localhost"
    RABBITMQ_PORT: int = 5672
    RABBITMQ_USER: str = "guest"
    RABBITMQ_PASSWORD: SecretStr  # guest

    @property
    def RABBITMQ_DSN(self) -> str:
        # Sync URL form Alembic
        return (
            f"amqp://"
            f"{self.RABBITMQ_USER}:"
            f"{self.RABBITMQ_PASSWORD.get_secret_value()}@"
            f"{self.RABBITMQ_HOST}:"
            f"{self.RABBITMQ_PORT}/"
        )

    # JWT
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 87840
    JWT_SECRET_KEY: SecretStr

    # Application
    LOG_LEVEL: str = "INFO"


@lru_cache
def get_settings() -> CoreSettings:
    return CoreSettings()


settings = get_settings()
