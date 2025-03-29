from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent


class DbConfig(BaseModel):
    url: str
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 5
    max_overflow: int = 10


class BotConfig(BaseModel):
    token: str


class AdminConfig(BaseModel):
    id: int


class Settings(BaseSettings):
    db: DbConfig
    bot: BotConfig
    admin: AdminConfig

    model_config = SettingsConfigDict(
        env_file="./.env",
        env_prefix="CONFIG__",
        env_nested_delimiter="__",
        case_sensitive=False,
        env_file_encoding="utf-8",
        validate_default=False,
    )


settings = Settings()
