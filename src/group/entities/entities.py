from sqlalchemy import Column, TEXT, Integer

from src.configs.database import Base


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer,primary_key=True, autoincrement=True)
    group_name = Column(TEXT)
