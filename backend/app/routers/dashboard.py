from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database.database import get_db
from fastapi.security import OAuth2PasswordBearer

from app.models.alunos import Aluno
from app.models.mensalidade import Mensalidade
from app.models.plano import Plano

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

@router.get("/")
def get_dashboard(db: Session = Depends(get_db)):
    total_alunos = db.query(func.count(Aluno.id)).filter(Aluno.ativo == True).scalar()

    total_planos = db.query(func.count(Plano.id)).scalar()

    receita_mes = db.query(func.sum(Mensalidade.valor)).scalar() or 0

    return {
        "total_alunos": total_alunos,
        "total_planos": total_planos,
        "receita_mes": float(receita_mes)
    }