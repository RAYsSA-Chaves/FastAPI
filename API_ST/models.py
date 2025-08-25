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