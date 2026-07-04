import api from "./api";

export const login = (email, senha) => {
    const form = new URLSearchParams();
    form.append("username", email);
    form.append("password", senha);

    return api.post("/auth/login", form, {
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
    });
};

export const register = (nome, email, senha) => {
    return api.post("/auth/register", {
        nome,
        email,
        senha,
    });
};

export async function getMe() {
    const token = localStorage.getItem("token");

    const response = await api.get("/auth/me", {
        headers: {
            Authorization: `Bearer ${token}`,
        },
    });

    return response.data;
}