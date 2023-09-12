from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):

    API_V1_STR: str = '/api'
    DB_URL: str = 'postgresql+asyncpg://postgres:root@localhost:5432/orcamentosapi'
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True


settings: Settings = Settings()