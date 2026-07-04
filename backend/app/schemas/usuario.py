from pydantic import BaseModel, EmailStr
from datetime import datetime

from app.models.usuario import TipoUsuario


class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str

class UsuarioLogin(BaseModel):
    email: EmailStr
    senha: str

class UsuarioResponse(BaseModel):

    id: int

    nome: str

    email: EmailStr

    tipo: TipoUsuario

    ativo: bool

    created_at: datetime

    class Config:
        from_attributes = True

class UsuarioUpdate(BaseModel):

    nome: str | None = None

    senha: str | None = None

    ativo: bool | None = None