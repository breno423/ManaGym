from sqlalchemy.orm import Session

from app.models.aluno import Aluno


def create(db: Session, academia_id: int, aluno):

    novo = Aluno(
        academia_id=academia_id,

        nome=aluno.nome,
        telefone=aluno.telefone,
        email=aluno.email,
        cpf=aluno.cpf,
        data_nascimento=aluno.data_nascimento,
        endereco=aluno.endereco,
        observacoes=aluno.observacoes,

        valor_mensalidade=aluno.valor_mensalidade,
        dia_vencimento=aluno.dia_vencimento,
        data_inicio=aluno.data_inicio
    )

    db.add(novo)
    db.commit()
    db.refresh(novo)

    return novo


def get_all(db: Session, academia_id: int):

    return (
        db.query(Aluno)
        .filter(
            Aluno.academia_id == academia_id,
            Aluno.ativo == True
        )
        .all()
    )


def get_by_id(db: Session, academia_id: int, aluno_id: int):

    return (
        db.query(Aluno)
        .filter(
            Aluno.id == aluno_id,
            Aluno.academia_id == academia_id
        )
        .first()
    )


def update(db: Session, aluno: Aluno, dados):

    dados = dados.model_dump(exclude_unset=True)

    for campo, valor in dados.items():
        setattr(aluno, campo, valor)

    db.commit()
    db.refresh(aluno)

    return aluno


def delete(db: Session, aluno: Aluno):

    aluno.ativo = False

    db.commit()