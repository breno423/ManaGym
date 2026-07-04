from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.database.database import Base


class Aluno(Base):
    __tablename__ = "aluno"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    academia_id: Mapped[int] = mapped_column(ForeignKey("academia.id"), nullable=False)

    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    telefone: Mapped[str] = mapped_column(String(20), nullable=True)
    email: Mapped[str] = mapped_column(String(120), nullable=True)

    ativo: Mapped[bool] = mapped_column(Boolean, default=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    academia: Mapped["Academia"] = relationship()
    mensalidades: Mapped[list["Mensalidade"]] = relationship(
        back_populates="aluno",
        cascade="all, delete-orphan"
    )