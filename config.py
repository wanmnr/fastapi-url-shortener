# config.py

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "FastAPI App"
    debug: bool = True
    database_url: str = "sqlite:///./test.db"
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()