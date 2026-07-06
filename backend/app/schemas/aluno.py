from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, EmailStr


class AlunoCreate(BaseModel):
    nome: str
    telefone: str
    email: EmailStr | None = None
    cpf: str | None = None
    data_nascimento: date | None = None
    endereco: str | None = None
    observacoes: str | None = None

    valor_mensalidade: Decimal
    dia_vencimento: int
    data_inicio: date


class AlunoUpdate(BaseModel):
    nome: str | None = None
    telefone: str | None = None
    email: EmailStr | None =None
    cpf: str | None = None
    data_nascimento: date | None = None
    endereco: str | None = None
    observacoes: str | None = None

    valor_mensalidade: Decimal | None = None
    dia_vencimento: int | None = None
    data_inicio: date | None = None

    ativo: bool | None = None


class AlunoResponse(BaseModel):

    id: int

    nome: str
    telefone: str
    email: str | None

    cpf: str | None

    endereco: str | None

    observacoes: str | None

    valor_mensalidade: Decimal

    dia_vencimento: int

    data_inicio: date

    ativo: bool

    created_at: datetime

    class Config:
        from_attributes = True