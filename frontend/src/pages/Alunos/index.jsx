import { useEffect, useState } from "react";
import { Plus, Search, Pencil, Trash2 } from "lucide-react";
import styles from "./styles.module.css";
import { getAlunos } from "./services";

export default function Alunos() {
    const [alunos, setAlunos] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        loadAlunos();
    }, []);

    async function loadAlunos() {
        try {
            const data = await getAlunos();
            setAlunos(data);
        } catch (err) {
            console.log(err);
        } finally {
            setLoading(false);
        }
    }

    function statusClass(status) {
        if (!status) return styles.statusDefault;
        const s = status.toLowerCase();
        if (s.includes("ativ")) return styles.statusAtivo;
        if (s.includes("inativ")) return styles.statusInativo;
        if (s.includes("pend")) return styles.statusPendente;
        return styles.statusDefault;
    }

    return (
        <div className={styles.container}>
            <div className={styles.header}>
                <div>
                    <h1 className={styles.title}>Alunos</h1>
                    <p className={styles.subtitle}>Gerencie os alunos cadastrados na academia</p>
                </div>
                <button className={styles.newButton}>
                    <Plus size={18} />
                    Novo aluno
                </button>
            </div>

            <div className={styles.searchBox}>
                <Search size={18} className={styles.searchIcon} />
                <input
                    className={styles.searchInput}
                    placeholder="Pesquisar aluno..."
                />
            </div>

            <div className={styles.tableWrapper}>
                <table className={styles.table}>
                    <thead>
                        <tr>
                            <th>Nome</th>
                            <th>Telefone</th>
                            <th>Plano</th>
                            <th>Status</th>
                            <th className={styles.actionsHeader}>Ações</th>
                        </tr>
                    </thead>
                    <tbody>
                        {loading ? (
                            <tr>
                                <td colSpan={5} className={styles.emptyState}>
                                    Carregando...
                                </td>
                            </tr>
                        ) : alunos.length === 0 ? (
                            <tr>
                                <td colSpan={5} className={styles.emptyState}>
                                    Nenhum aluno cadastrado.
                                </td>
                            </tr>
                        ) : (
                            alunos.map(aluno => (
                                <tr key={aluno.id} className={styles.row}>
                                    <td className={styles.nameCell}>{aluno.nome}</td>
                                    <td>{aluno.telefone}</td>
                                    <td>{aluno.plano?.nome ?? "—"}</td>
                                    <td>
                                        <span className={`${styles.statusBadge} ${statusClass(aluno.status)}`}>
                                            {aluno.status}
                                        </span>
                                    </td>
                                    <td>
                                        <div className={styles.actions}>
                                            <button className={styles.editButton} title="Editar">
                                                <Pencil size={16} />
                                            </button>
                                            <button className={styles.deleteButton} title="Excluir">
                                                <Trash2 size={16} />
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                            ))
                        )}
                    </tbody>
                </table>
            </div>
        </div>
    );
}