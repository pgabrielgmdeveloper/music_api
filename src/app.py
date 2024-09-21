from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.group.controllers.group_controller import router as router_group
from src.musiscs.controllers.musicController import router as router_music
from src.cult.controllers.cultController import router as router_cult
from src.configs.database import ENGINE
from src.group.entities.entities import *
from src.musiscs.entities.music import *
from src.cult.entities.cult import *
from src.prase.entities.praise import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    #sTARTUP
    async with ENGINE.begin() as conn:
        print('criando tabelas')
        await conn.run_sync(Base.metadata.create_all)
    yield
    #shutdown


app = FastAPI(
    lifespan=lifespan
)


app.include_router(prefix="/group",router=router_group)
app.include_router(prefix="/music", router=router_music)
app.include_router(prefix="/cult", router=router_cult)