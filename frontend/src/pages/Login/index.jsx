import { useState } from "react";
import styles from "./styles.module.css";
import { login } from "./services";
import { Dumbbell } from "lucide-react";
import { useNavigate } from "react-router-dom";
import { Link } from "react-router-dom";

export default function Login() {
    const navigate = useNavigate();

    const [email, setEmail] = useState("");
    const [senha, setSenha] = useState("");
    const [loading, setLoading] = useState(false);
    const [erro, setErro] = useState("");

    async function handleSubmit(e) {
        e.preventDefault();

        setErro("");
        setLoading(true);

        try {
            const token = await login(email, senha);

            localStorage.setItem("token", token.access_token);

            navigate("/dashboard");
        } catch {
            setErro("Email ou senha inválidos.");
        } finally {
            setLoading(false);
        }
    }

    return (
        <main className={styles.container}>
            <form
                className={styles.card}
                onSubmit={handleSubmit}
            >

                <div className={styles.logo}>
                    <Dumbbell size={40} />
                    <h1>ManaGym</h1>
                    <span className={styles.sub}>Entre para treinar</span>
                </div>

                <h2>Acesse sua conta</h2>

                <input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e)=>setEmail(e.target.value)}
                />

                <input
                    type="password"
                    placeholder="Senha"
                    value={senha}
                    onChange={(e)=>setSenha(e.target.value)}
                />

                {erro && (
                    <span className={styles.error}>
                        {erro}
                    </span>
                )}

                <button disabled={loading}>
                    {loading ? "Entrando..." : "Entrar"}
                </button>

                <div className={styles["link-row"]}>
                    <a href="#">Esqueci a senha</a>
                    <Link to="/register">
                Criar conta
                    </Link>
                </div>

            </form>
        </main>
    );
}