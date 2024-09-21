from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
import sqlalchemy as sa

from src.group.entities.entities import Group

class GroupRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def createGroup(self, name: str):
        group = Group(group_name=name)
        try:
            async with self._session.begin():
                self._session.add(group)
        
        except Exception as e:
            
            print(f"Erro ao criar grupo: {e}")
    
    async def getAll(self):
        result = await self._session.execute(sa.select(Group))
        return result.scalars().all()
            
    async def get_by_id(self, id: int):
        result = await self._session.execute(sa.select(Group).where(Group.id == id))
        return result.scalar_one()