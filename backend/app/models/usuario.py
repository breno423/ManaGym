from datetime import datetime
import enum
from sqlalchemy import DateTime, ForeignKey, String, Enum, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.database.database import Base

class TipoUsuario(str, enum.Enum):
    ADMIN = "ADMIN"
    PROFESSOR = "PROFESSOR"
    FUNCIONARIO = "FUNCIONARIO"


class Usuario(Base):
    __tablename__ = "usuario"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    academia_id: Mapped[int] = mapped_column(
        ForeignKey("academia.id"),
        nullable=False
    )

    nome: Mapped[str] = mapped_column(String(60), nullable=False)

    email: Mapped[str] = mapped_column(
        String(120),
        unique=True,
        index=True,
        nullable=False
    )

    senha_hash: Mapped[str] = mapped_column(String(255), nullable=False)


    tipo: Mapped[TipoUsuario] = mapped_column(
        Enum(TipoUsuario)
    )

    ativo: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    ultimo_login: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    academia: Mapped["Academia"] = relationship(
    back_populates="usuarios"
)