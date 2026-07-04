import { useSettings } from "../../context/SettingsContext";
import { Moon, Sun, Zap, AlignLeft, Hash, Check } from "lucide-react";
import styles from "./styles.module.css";

const opcoesTema = [
    { valor: "dark", label: "Dark", desc: "Escuro com dourado", icon: Moon },
    { valor: "light", label: "Light", desc: "Claro e neutro", icon: Sun },
    { valor: "lightning", label: "Lightning", desc: "Alto contraste", icon: Zap },
];

const opcoesFormato = [
    { valor: "full", label: "Completo", desc: "12.056", icon: AlignLeft },
    { valor: "compact", label: "Compacto", desc: "12k", icon: Hash },
];

export default function SettingsPage() {
    const { theme, setTheme, format, setFormat } = useSettings();

    return (
        <div className={styles.container}>

            <header className={styles.header}>
                <h1>Configurações</h1>
                <p>Personalize a aparência e o formato de exibição do sistema</p>
            </header>

            <section className={styles.section}>
                <div className={styles.sectionHeader}>
                    <h2>Tema</h2>
                    <span className={styles.sectionDesc}>
                        Escolha como as telas do ManaGym vão aparecer pra você
                    </span>
                </div>

                <div className={styles.optionsGrid}>
                    {opcoesTema.map((opcao) => {
                        const Icon = opcao.icon;
                        const ativo = theme === opcao.valor;

                        return (
                            <button
                                key={opcao.valor}
                                className={`${styles.optionCard} ${ativo ? styles.optionActive : ""}`}
                                onClick={() => setTheme(opcao.valor)}
                            >
                                {ativo && (
                                    <span className={styles.checkBadge}>
                                        <Check size={12} />
                                    </span>
                                )}

                                <div className={styles.optionIcon}>
                                    <Icon size={22} />
                                </div>

                                <div className={styles.optionText}>
                                    <strong>{opcao.label}</strong>
                                    <span>{opcao.desc}</span>
                                </div>
                            </button>
                        );
                    })}
                </div>
            </section>

            <section className={styles.section}>
                <div className={styles.sectionHeader}>
                    <h2>Formato de valores</h2>
                    <span className={styles.sectionDesc}>
                        Defina como números e valores monetários serão exibidos
                    </span>
                </div>

                <div className={styles.optionsGrid}>
                    {opcoesFormato.map((opcao) => {
                        const Icon = opcao.icon;
                        const ativo = format === opcao.valor;

                        return (
                            <button
                                key={opcao.valor}
                                className={`${styles.optionCard} ${ativo ? styles.optionActive : ""}`}
                                onClick={() => setFormat(opcao.valor)}
                            >
                                {ativo && (
                                    <span className={styles.checkBadge}>
                                        <Check size={12} />
                                    </span>
                                )}

                                <div className={styles.optionIcon}>
                                    <Icon size={22} />
                                </div>

                                <div className={styles.optionText}>
                                    <strong>{opcao.label}</strong>
                                    <span>{opcao.desc}</span>
                                </div>
                            </button>
                        );
                    })}
                </div>
            </section>

        </div>
    );
}