import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:8000",
});

export async function login(email, senha) {

    const form = new URLSearchParams();

    form.append("username", email);
    form.append("password", senha);

    const { data } = await api.post(
        "/auth/login",
        form,
        {
            headers: {
                "Content-Type":
                    "application/x-www-form-urlencoded",
            },
        }
    );

    return data;
}