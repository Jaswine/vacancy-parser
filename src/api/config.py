from functools import lru_cache

from pydantic_settings import BaseSettings


class APISettings(BaseSettings):
    NAME: str = 'Vacancy parser'
    VERSION: str = '1.0.0'
    ROOT_PATH: str = '/api'

@lru_cache()
def get_settings() -> APISettings:
    return APISettings()  # type: ignore

api_settings = get_settings()