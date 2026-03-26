from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str
    redis_url: str
    openai_api_key: str
    debug: bool = False
    secret_key: str

    class Config:
        env_file = ".env"

settings = Settings()