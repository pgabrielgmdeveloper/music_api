from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_HOST= os.getenv('DATABASE_HOST')
DATABASE_USER_NAME= os.getenv('DATABASE_USER_NAME')
DATABASE_PASSWORD= os.getenv('DATABASE_PASSWORD')
ACCESS_KEY= os.getenv('ACCESS_KEY')
SECRET_KEY= os.getenv('SECRET_KEY')
BUCKET_NAME= os.getenv('BUCKET_NAME')
CONN = f"postgresql+asyncpg://{DATABASE_USER_NAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:5432/postgres"
ENGINE = create_async_engine(CONN)
Base = declarative_base()


async_session_factory = sessionmaker(
    bind=ENGINE,
    class_=AsyncSession,
    expire_on_commit=False,
)

    
async def get_session() -> AsyncSession:
    async with async_session_factory() as session:
        yield session