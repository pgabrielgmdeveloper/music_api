from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

from src.configs.settings import settings

DATABASE_HOST= settings.database_host
DATABASE_USER_NAME= settings.database_user_name
DATABASE_PASSWORD= settings.database_password
ACCESS_KEY= settings.access_key
SECRET_KEY= settings.secret_key
BUCKET_NAME= settings.bucket_name
CONN = f"postgresql+asyncpg://{DATABASE_USER_NAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:5432/postgres"
ENGINE = create_async_engine(CONN)

Base = declarative_base()

def to_dict(self):
    return {column: getattr(self, column) for column in vars(self) if not column.startswith('_')}

async_session_factory = sessionmaker(
    bind=ENGINE,
    class_=AsyncSession,
    expire_on_commit=False,
)

    
async def get_session() -> AsyncSession:
    async with async_session_factory() as session:
        yield session