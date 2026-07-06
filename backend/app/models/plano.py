from datetime import datetime

from sqlalchemy import (
    String,
    Numeric,
    Boolean,
    DateTime,
    ForeignKey,
    Integer
)

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.database.database import Base


class Plano(Base):
    __tablename__ = "plano"

    id: Mapped[int] = mapped_column(primary_key=True)

    academia_id: Mapped[int] = mapped_column(
        ForeignKey("academia.id"),
        nullable=False
    )

    nome: Mapped[str] = mapped_column(
        String(80),
        nullable=False
    )

    descricao: Mapped[str | None] = mapped_column(
        String(255)
    )

    valor: Mapped[float] = mapped_column(
        Numeric(10,2),
        nullable=False
    )

    dia_vencimento: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    ativo: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    academia = relationship(
        "Academia",
        back_populates="planos"
    )

    alunos = relationship(
        "Aluno",
        back_populates="plano"
    )

    mensalidades = relationship(
        "Mensalidade",
        back_populates="plano",
        cascade="all, delete-orphan"
    )