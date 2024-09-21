from typing import List
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from src.configs.database import get_session, to_dict
from src.configs.models import ResponseModel
from src.configs.s3Configs import S3Client
from src.cult.DTOs.cult import AddPraise, CreateCult, CultDayResponse, CultResponse, PraiseResponsse
from src.cult.entities.cult import Cult
from src.cult.repository.CultRepository import CultRepository
from src.group.repository.GroupRepository import GroupRepository
from src.musiscs.DTOs.music import MusicPlayResponse, MusicResponse
from src.musiscs.repository.musicRepository import MusicRepository
from src.prase.entities.praise import Praise 

router = APIRouter()



@router.post("/create-cult")
async def create_cult(cult: CreateCult, session = Depends(get_session)):
    repository = CultRepository(session)
    await repository.createCult(cult=Cult(**cult.model_dump()))
    return JSONResponse(status_code=201, content={})

@router.get("/get-cults")
async def get_cult(session = Depends(get_session)) -> ResponseModel[CultResponse]:
    repository = CultRepository(session)
    cults_e = await repository.get_all()
    cults = [CultResponse(**to_dict(cult)) for cult in cults_e]
    return {"data": cults}


@router.get("/get-cult/{id}")
async def get_cult_day(id: int,session = Depends(get_session)) -> ResponseModel[CultDayResponse]:
    repository = CultRepository(session)
    music_repository = MusicRepository(session)
    s3 = S3Client()
    cult = await repository.get_by_id(id)
    musics  = [
            {**to_dict(await music_repository.get_by_id(praise.music_id)), "group": praise.group}
         for praise in cult.praises
        ]
    musics_play = [{**music, "URI": await s3.get_objects(music["name"] + ".mp3")} for music in musics]
    music_response = [
        PraiseResponsse(**music) for music in musics_play
    ]
    cult_dict = to_dict(cult)
    cult_dict['praises'] = music_response
    
    response = CultDayResponse(**cult_dict)
    return {"data": response}


@router.post("/add-praise")
async def add_praise(add_praise: AddPraise ,session = Depends(get_session)):
    repository = CultRepository(session)
    groupRepository = GroupRepository(session)
    group = await groupRepository.get_by_id(add_praise.group_id)
    await repository.add_praise(add_praise.cult_id, Praise(**add_praise.model_dump(),group=group.group_name))
    return JSONResponse(content=204)