from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from app.core.security import create_access_token
from jose import jwt, JWTError
from app.core.config import settings

from app.database.deps import get_db
from app.schemas.usuario import UsuarioCreate
from app.models.usuario import TipoUsuario
from app.crud import usuario as crud_usuario
router = APIRouter(
    prefix="/auth",
    tags=["Autenticação"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

@router.post("/register")
def register(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db)
):

    print("PAYLOAD RECEBIDO:", usuario)
    print("SENHA:", usuario.senha)
    print("TIPO:", type(usuario.senha))

    existente = crud_usuario.get_by_email(
        db,
        usuario.email
    )

    if existente:
        raise HTTPException(
            status_code=400,
            detail="E-mail já cadastrado."
        )

    novo = crud_usuario.create(
        db=db,
        usuario=usuario,
        academia_id=1,
        tipo=TipoUsuario.ADMIN
    )

    return novo

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    usuario = crud_usuario.authenticate(
        db,
        form_data.username,
        form_data.password
    )

    if not usuario:
        raise HTTPException(
            status_code=401,
            detail="Nome de usuário ou senha inválidos."
        )

    token = create_access_token(
        {
            "sub": usuario.email,
            "id": usuario.id
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.get("/me")
def get_me(
    token: str = Depends(oauth2_scheme),
    db = Depends(get_db)
):
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        user_id = payload.get("id")

        usuario = crud_usuario.get_by_id(db, user_id)

        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")

        return usuario

    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")