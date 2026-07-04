from datetime import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.database.database import Base


class Academia(Base):
    __tablename__ = "academia"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    nome: Mapped[str] = mapped_column(String(100))
    telefone: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    pix_key: Mapped[str]

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    usuarios: Mapped[list["Usuario"]] = relationship(
        back_populates="academia",
        cascade="all, delete-orphan"
    )