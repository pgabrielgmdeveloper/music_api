from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.group.controllers.group_controller import router
from src.configs.database import ENGINE
from src.group.entities.entities import *


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


app.include_router(router=router)