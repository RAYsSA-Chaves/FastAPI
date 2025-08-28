from typing import Optional
from pydantic import BaseModel

class StrangerThingsCharacters(BaseModel):
    id: Optional[int] = None
    nome: str
    status: str
    ocupaçao: str
    habilidades: str
    familia: str
    foto: str

# Modelo para PATCH (edição parcial do personagem)
class StrangerThingsCharactersPatch(BaseModel):
    nome: Optional[str] = None
    status: Optional[str] = None
    ocupaçao: Optional[str] = None
    habilidades: Optional[str] = None
    familia: Optional[str] = None
    foto: Optional[str] = None
