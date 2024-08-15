from src.configs.models import BaseDTO


class CreateMusic(BaseDTO):
    singer: str 
    name: str
    letter: str
    
class MusicResponse(CreateMusic):
    id: int


class MusicPlayResponse(MusicResponse):
    URI: str

