from typing import Dict, List
from fastapi import APIRouter, Response, UploadFile, File
from fastapi.params import Form 
from fastapi import Depends

from fastapi.responses import JSONResponse
import json
from src.configs.database import get_session, to_dict
from src.configs.models import ResponseModel
from src.configs.s3Configs import S3Client
from src.musiscs.DTOs.music import CreateMusic, MusicPlayResponse, MusicResponse
from src.musiscs.entities.music import Music
from src.musiscs.repository.musicRepository import MusicRepository
router = APIRouter()


@router.post("/create-music")
async def create_music(session = Depends(get_session),file: UploadFile = File(...), music_json: str = Form(...)) -> ResponseModel[Dict[str,str]]:
    content = await file.read()
    music = CreateMusic(**json.loads(music_json))
    repository = MusicRepository(session=session)
    s3 = S3Client()
    await s3.put(file, object_name=music.name + ".mp3", file_content=content)
    return JSONResponse(status_code=201, content={"status":"created"})

@router.get("/get-musics")
async def get_all_musiscs(session = Depends(get_session)) -> ResponseModel[List[MusicResponse]]:
    repository = MusicRepository(session=session)
    response = await repository.getAll()
    return {"data": response}


@router.post("/get-musics-play")
async def get_musics_play(music_ids: List[int],session = Depends(get_session)):
    repository = MusicRepository(session=session)
    s3 = S3Client()
    
    musics: List[MusicResponse] = [MusicResponse(**(to_dict(await repository.get_by_id(id)))) for id in music_ids]
    musics_play = [MusicPlayResponse(**music.model_dump(), URI = await s3.get_objects(music.name)) for music in musics]
    return {"data": musics_play}
    