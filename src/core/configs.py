from pydantic import BaseSettings
from sqlalchemy.orm import declarative_base


class Settings(BaseSettings):
    API_STR: str = "/api"
    DB_URL: str = "postgresql+asyncpg://postgres:root@localhost:5432/orcamentosapi"

    DBBaseModel = declarative_base()

    JWT_SECRET: str = "MKlIJdwqQXm93gg1vXFCLQejP8tIW24Nmu5bdSf3sm4"

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINURES = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings: Settings = Settings()
