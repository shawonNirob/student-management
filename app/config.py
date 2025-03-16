from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    OPENAI_API_KEY: str
    MODEL_ID: str

    class Config:
        env_file = ".env"

settings = Settings()
