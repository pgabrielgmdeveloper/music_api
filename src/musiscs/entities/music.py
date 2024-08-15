from sqlalchemy import TEXT, Column, Integer
from src.configs.database import Base


class Music(Base):
    __tablename__ = "music"
    id: str = Column(Integer, primary_key=True, autoincrement=True) 
    singer: str = Column(TEXT, nullable=False)
    name: str = Column(TEXT, nullable=False)
    letter: str = Column(TEXT, nullable=False)