from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Float, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.database.database import Base


class Pagamento(Base):
    __tablename__ = "pagamento"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    mensalidade_id: Mapped[int] = mapped_column(
        ForeignKey("mensalidade.id"),
        nullable=False
    )

    valor_pago: Mapped[float] = mapped_column(Float, nullable=False)

    metodo: Mapped[str] = mapped_column(String(50))  # PIX, CARTAO, DINHEIRO

    data_pagamento: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    comprovante_url: Mapped[str | None] = mapped_column(String(255), nullable=True)

    mensalidade: Mapped["Mensalidade"] = relationship(back_populates="pagamentos")