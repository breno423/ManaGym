from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database.deps import get_db

from app.schemas.aluno import (
    AlunoCreate,
    AlunoUpdate,
    AlunoResponse
)

from app.crud import aluno as crud_aluno

from app.dependencies.auth import get_current_user


router = APIRouter(
    prefix="/alunos",
    tags=["Alunos"]
)

@router.post("", response_model=AlunoResponse)
def create(
    aluno: AlunoCreate,
    db: Session = Depends(get_db),
    usuario=Depends(get_current_user)
):

    return crud_aluno.create(
        db,
        usuario.academia_id,
        aluno
    )

@router.get("", response_model=list[AlunoResponse])
def get_all(
    db: Session = Depends(get_db),
    usuario=Depends(get_current_user)
):

    return crud_aluno.get_all(
        db,
        usuario.academia_id
    )

@router.get("/{aluno_id}", response_model=AlunoResponse)
def get_by_id(
    aluno_id: int,
    db: Session = Depends(get_db),
    usuario=Depends(get_current_user)
):

    aluno = crud_aluno.get_by_id(
        db,
        usuario.academia_id,
        aluno_id
    )

    if not aluno:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
        )

    return aluno

@router.put("/{aluno_id}", response_model=AlunoResponse)
def update(
    aluno_id: int,
    dados: AlunoUpdate,
    db: Session = Depends(get_db),
    usuario=Depends(get_current_user)
):

    aluno = crud_aluno.get_by_id(
        db,
        usuario.academia_id,
        aluno_id
    )

    if not aluno:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
        )

    return crud_aluno.update(
        db,
        aluno,
        dados
    )

@router.delete("/{aluno_id}")
def delete(
    aluno_id: int,
    db: Session = Depends(get_db),
    usuario=Depends(get_current_user)
):

    aluno = crud_aluno.get_by_id(
        db,
        usuario.academia_id,
        aluno_id
    )

    if not aluno:
        raise HTTPException(
            status_code=404,
            detail="Aluno não encontrado"
        )

    crud_aluno.delete(
        db,
        aluno
    )

    return {
        "message": "Aluno removido."
    }

