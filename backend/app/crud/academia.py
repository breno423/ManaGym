from sqlalchemy.orm import Session

from app.models.academia import Academia
from app.schemas.academia import AcademiaCreate


def create(
    db: Session,
    academia: AcademiaCreate
):

    nova = Academia(

        nome=academia.nome,

        telefone=academia.telefone,

        email=academia.email,

        pix_key=academia.pix_key

    )

    db.add(nova)

    db.commit()

    db.refresh(nova)

    return nova