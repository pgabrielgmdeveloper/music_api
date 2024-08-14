from sqlalchemy import Column, TEXT, Integer

from src.configs.database import Base


class Group(Base):
    __tablename__ = 'group_t'
    id = Column(Integer,primary_key=True, autoincrement=True)
    group_name = Column(TEXT)
