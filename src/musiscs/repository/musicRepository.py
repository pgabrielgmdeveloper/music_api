import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession
from src.musiscs.entities.music import Music


class MusicRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session


    async def createMusic(self, music: Music):
        try:
            async with self._session.begin():
                self._session.add(music)
        
        except Exception as e:
            print(f"Erro ao criar Musica: {e}")
    

    async def getAll(self):
        result = await self._session.execute(sa.select(Music))
        return result.scalars().all()
    
    async def get_by_id(self, id: int) -> Music:
        result = await self._session.execute(sa.select(Music).where(Music.id == id))            
        return result.scalar_one()