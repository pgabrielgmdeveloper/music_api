from pydantic import Field
from src.configs.models import BaseDTO

class CreateGroup(BaseDTO):
    name: str 

class GroupResponse(BaseDTO):
    id: int
    name: str