try:
    from pydantic_settings import BaseSettings
except ImportError:
    from pydantic import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    database_url: str = "sqlite:///./test.db"
    redis_url: str = "redis://localhost:6379/0"
    openai_api_key: str = "mock_key"
    mock_llm: bool = True
    debug: bool = False
    secret_key: str = "dev_secret_key"

    class Config:
        env_file = ".env"

settings = Settings()