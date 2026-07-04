from pydantic import BaseModel

from app.schemas.academia import AcademiaCreate
from app.schemas.usuario import UsuarioCreate


class RegisterRequest(BaseModel):
    academia: AcademiaCreate
    usuario: UsuarioCreate