from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: int
    POSTGRES_HOST: str
    DATABASE_URL: str
    CLIENT_URL: str
    SENDER_EMAIL: str
    PASSWORD_EMAILER: str
    SERVER_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
