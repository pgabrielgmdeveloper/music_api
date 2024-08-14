from typing import List
from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from src.configs.database import get_session
from src.group.DTOs.Group import CreateGroup, GroupResponse
from src.group.repository.GroupRepository import GroupRepository
from src.configs.models import ResponseModel

router = APIRouter()



@router.post("/create_group")
async def group(group: CreateGroup, session: AsyncSession = Depends(get_session)):
    repository = GroupRepository(session=session)
    await repository.createGroup(group.name)
    return JSONResponse(status_code=201, content=None)

@router.get("/get_groups")
async def get_group(session: AsyncSession =Depends(get_session)) -> ResponseModel[List[GroupResponse]]:
    repository = GroupRepository(session=session)
    result = await repository.getAll()
    result = [GroupResponse(name=group.group_name, id=group.id) for group in result]
    return {"data":result}