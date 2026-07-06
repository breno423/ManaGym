from datetime import date, datetime
import enum
from sqlalchemy import Enum as SQLEnum

from sqlalchemy import (
    String,
    Date,
    DateTime,
    Boolean,
    ForeignKey,
    Numeric,
    Integer,
    Text
)

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.database.database import Base

class StatusAluno(str, enum.Enum):
    ATIVO = "ATIVO"
    INADIMPLENTE = "INADIMPLENTE"
    PAUSADO = "PAUSADO"
    CANCELADO = "CANCELADO"


class Aluno(Base):
    __tablename__ = "aluno"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    academia_id: Mapped[int] = mapped_column(
        ForeignKey("academia.id"),
        nullable=False
    )

    nome: Mapped[str] = mapped_column(String(120), nullable=False)

    telefone: Mapped[str] = mapped_column(String(20), nullable=False)

    email: Mapped[str | None] = mapped_column(String(120))

    cpf: Mapped[str | None] = mapped_column(String(14))

    data_nascimento: Mapped[date | None] = mapped_column(Date)

    endereco: Mapped[str | None] = mapped_column(String(255))

    observacoes: Mapped[str | None] = mapped_column(Text)

    plano_id: Mapped[int] = mapped_column(
        ForeignKey("plano.id"),
        nullable=False
    )

    data_inicio: Mapped[date] = mapped_column(Date)

    status: Mapped[StatusAluno] = mapped_column(
        SQLEnum(StatusAluno),
        default=StatusAluno.ATIVO,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    academia = relationship(
        "Academia",
        back_populates="alunos"
    )

    mensalidades = relationship(
        "Mensalidade",
        back_populates="aluno",
        cascade="all, delete-orphan"
    )

    plano = relationship(
    "Plano",
    back_populates="alunos"
    )