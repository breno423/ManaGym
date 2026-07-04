import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:8000",
});

export async function register(nome, email, senha) {

    const { data } = await api.post("/auth/register", {
        nome,
        email,
        senha,
    });

    return data;
}