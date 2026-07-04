from datetime import datetime, date
from sqlalchemy import DateTime, ForeignKey, Date, Enum, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
import enum

from app.database.database import Base


class StatusMensalidade(str, enum.Enum):
    PENDENTE = "PENDENTE"
    PAGO = "PAGO"
    ATRASADO = "ATRASADO"
    CANCELADO = "CANCELADO"


class Mensalidade(Base):
    __tablename__ = "mensalidade"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    aluno_id: Mapped[int] = mapped_column(ForeignKey("aluno.id"), nullable=False)
    plano_id: Mapped[int] = mapped_column(ForeignKey("plano.id"), nullable=False)

    valor: Mapped[float] = mapped_column(Float, nullable=False)

    data_vencimento: Mapped[date] = mapped_column(Date, nullable=False)

    status: Mapped[StatusMensalidade] = mapped_column(
        Enum(StatusMensalidade),
        default=StatusMensalidade.PENDENTE
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    aluno: Mapped["Aluno"] = relationship(back_populates="mensalidades")
    plano: Mapped["Plano"] = relationship(back_populates="mensalidades")
    pagamentos: Mapped[list["Pagamento"]] = relationship(
        back_populates="mensalidade",
        cascade="all, delete-orphan"
    )