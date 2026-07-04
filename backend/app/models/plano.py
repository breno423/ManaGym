from datetime import datetime
from sqlalchemy import String, DateTime, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.database.database import Base


class Plano(Base):
    __tablename__ = "plano"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    academia_id: Mapped[int] = mapped_column(ForeignKey("academia.id"), nullable=False)

    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    valor: Mapped[float] = mapped_column(Float, nullable=False)
    descricao: Mapped[str] = mapped_column(String(255), nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    mensalidades: Mapped[list["Mensalidade"]] = relationship(back_populates="plano")