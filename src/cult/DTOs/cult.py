from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import date

class CreateCult(BaseModel):
    name: str
    end_date: date = Field(..., alias="endDate")

class CultResponse(BaseModel):
     id: int
     name: str
     created_at: date
     end_date: date



class AddPraise(BaseModel):
    cult_id: int = Field(..., alias="cultId")
    music_id: int = Field(..., alias="musicId")
    group_id: int = Field(..., alias="groupId")


class PraiseResponsse(BaseModel):
    name: str
    URI: str
    letter: str
    group: str

class CultDayResponse(CultResponse):
    praises: List[PraiseResponsse]