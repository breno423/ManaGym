import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { Dumbbell } from "lucide-react";
import styles from "./styles.module.css";
import { register } from "./services";

export default function Register() {

    const navigate = useNavigate();

    const [nome, setNome] = useState("");
    const [email, setEmail] = useState("");
    const [senha, setSenha] = useState("");

    const [loading, setLoading] = useState(false);
    const [erro, setErro] = useState("");

    async function handleSubmit(e) {

        e.preventDefault();

        setErro("");
        setLoading(true);

        try {

            await register(nome, email, senha);

            navigate("/");

        } catch (err) {

            setErro(
                err.response?.data?.detail ||
                "Erro ao criar conta."
            );

        } finally {

            setLoading(false);
        }
    }

    return (

        <main className={styles.container}>

            <form
                onSubmit={handleSubmit}
                className={styles.card}
            >

                <div className={styles.logo}>
                    <Dumbbell size={40}/>
                    <h1>ManaGym</h1>
                </div>

                <h2>Criar Conta</h2>

                <input
                    placeholder="Nome"
                    value={nome}
                    onChange={(e)=>setNome(e.target.value)}
                />

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
                    {loading ? "Criando..." : "Cadastrar"}
                </button>

                <span className={styles.backLink}>
    Já possui conta? <Link to="/">Entrar</Link>
</span>

            </form>

        </main>
    );
}