from sqlalchemy.orm import Session

from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate
from app.core.security import (
    get_password_hash,
    verify_password
)

def get_by_email(
    db: Session,
    email: str
):

    return (
        db.query(Usuario)
        .filter(Usuario.email == email)
        .first()
    )

def get_by_id(
    db: Session,
    usuario_id: int
):

    return db.get(
        Usuario,
        usuario_id
    )

def create(
    db: Session,
    usuario: UsuarioCreate,
    academia_id: int,
    tipo
):

    novo_usuario = Usuario(

        nome=usuario.nome,

        email=usuario.email,

        senha_hash=get_password_hash(
            usuario.senha
        ),

        academia_id=academia_id,

        tipo=tipo
    )

    db.add(novo_usuario)

    db.commit()

    db.refresh(novo_usuario)

    return novo_usuario

def authenticate(
    db: Session,
    email: str,
    senha: str
):

    usuario = get_by_email(
        db,
        email
    )

    if not usuario:
        return None

    if not verify_password(
        senha,
        usuario.senha_hash
    ):
        return None

    return usuario

