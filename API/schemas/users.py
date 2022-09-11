from pydantic import BaseModel


class Usuario(BaseModel):
    nombre:str
    edad:int
    email:str
