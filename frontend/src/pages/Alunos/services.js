import api from "../../services/api";

export async function getAlunos() {
    const { data } = await api.get("/alunos");
    return data;
}

export async function createAluno(aluno) {
    const { data } = await api.post("/alunos", aluno);
    return data;
}

export async function updateAluno(id, aluno) {
    const { data } = await api.put(`/alunos/${id}`, aluno);
    return data;
}

export async function deleteAluno(id) {
    await api.delete(`/alunos/${id}`);
}