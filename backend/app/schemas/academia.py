from datetime import datetime

from pydantic import BaseModel, EmailStr


class AcademiaBase(BaseModel):
    nome: str
    telefone: str
    email: EmailStr
    pix_key: str


class AcademiaCreate(BaseModel):
    nome: str
    telefone: str
    email: EmailStr
    pix_key: str

class AcademiaUpdate(BaseModel):
    nome: str | None = None
    telefone: str | None = None
    email: EmailStr | None = None
    pix_key: str | None = None


class AcademiaResponse(AcademiaBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True