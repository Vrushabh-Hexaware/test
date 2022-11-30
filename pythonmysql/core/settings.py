import os
import ssl
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):

    DB_CONN: str
    PORT: int
    LOG_LEVEL: str
    LOG_FILE: str
    BASE_PATH: Optional[str]

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
settings.BASE_PATH = os.path.dirname(os.path.abspath(''))
