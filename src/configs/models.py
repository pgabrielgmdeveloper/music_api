from typing import Generic, List, TypeVar, Union
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
import os


def to_camel_case(string: str) -> str:
    components = string.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


class BaseDTO(BaseModel):
    class config:
        allow_generator = to_camel_case
        allow_population_by_field_name =True


T = TypeVar("T")

class ResponseModel(GenericModel, Generic[T]):
    data: Union[List[T], T]