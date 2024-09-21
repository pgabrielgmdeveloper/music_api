import sqlalchemy as sa
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from src.cult.entities.cult import Cult
from src.prase.entities.praise import Praise
from datetime import date

class CultRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session


    async def createCult(self, cult: Cult):
        try:
            async with self._session.begin():
                self._session.add(cult)
        
        except Exception as e:
            print(f"Erro ao criar Musica: {e}")
    

    async def get_all(self):
        result = await self._session.execute(
            sa.select(Cult).where(Cult.end_date >= date.today())
        )
        return result.scalars().all()
    
    async def get_by_id(self, id: int) -> Cult:
        result = await self._session.execute(sa.select(Cult).options(selectinload(Cult.praises)).where(Cult.id == id))         
        
        return result.scalar_one()
    
    async def add_praise(self, id: int, praise: Praise):
        cult  = await self.get_by_id(id)
        if self._session.in_transaction:
            cult.praises.append(praise)
            self._session.add(cult)
            await self._session.commit()
        else:
            async with self._session.begin():
                cult.praises.append(praise)
                self._session.add(cult)
        
        
