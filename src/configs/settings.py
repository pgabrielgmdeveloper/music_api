import os
from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_host: str = Field(..., env='DATABASE_HOST')
    database_user_name: str = Field(..., env='DATABASE_USER')
    database_password: str = Field(..., env='DATABASE_PASSWORD')
    access_key: str = Field(..., env='ACCESS_KEY')
    secret_key: str = Field(..., env='SECRET_KEY')
    bucket_name: str = Field(..., env='BUCKET_NAME')

settings = Settings()