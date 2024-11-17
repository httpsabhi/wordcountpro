from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URI: str
    SECREAT_KEY: str
    ALGORITHM: str
    
    model_config = SettingsConfigDict(env_file=".env")
    
settings = Settings()