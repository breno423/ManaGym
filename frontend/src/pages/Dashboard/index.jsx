import { useState, useEffect, useRef } from "react";
import { useNavigate } from "react-router-dom";
import { getMe } from "../../services/auth";
import {
    Dumbbell,
    LayoutDashboard,
    Users,
    DollarSign,
    Settings,
    LogOut,
    GripVertical,
    Menu,
    X,
    ChevronLeft,
    ChevronRight,
    ClipboardList,
} from "lucide-react";
import styles from "./styles.module.css";
import { useSettings } from "../../context/SettingsContext";
import { formatValue } from "../../utils/formatValue";
import { Link } from "react-router-dom";

const widgetsIniciais = [
    {
        id: "ativos",
        titulo: "Alunos ativos",
        valor: "128",
        icon: Users,
    },
    {
        id: "receber",
        titulo: "Valor a receber",
        valor: "R$ 4.320,00",
        icon: DollarSign,
    },
    {
        id: "recebido",
        titulo: "Valor recebido",
        valor: "R$ 12.980,00",
        icon: DollarSign,
    },
];

export default function Dashboard() {

    const { format } = useSettings();
    const navigate = useNavigate();

    const [usuarioLogado, setUsuarioLogado] = useState(null);

    const [widgets, setWidgets] = useState(widgetsIniciais);
    const [dragId, setDragId] = useState(null);
    const [dragOverId, setDragOverId] = useState(null);

    const [collapsed, setCollapsed] = useState(false);
    const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
    const [openProfile, setOpenProfile] = useState(false);

    const profileRef = useRef(null);

    useEffect(() => {

        function handleClickOutside(event) {
            if (profileRef.current && !profileRef.current.contains(event.target)) {
                setOpenProfile(false);
            }
        }

        async function loadUser() {
            try {
                const data = await getMe();
                setUsuarioLogado(data);
            } catch (err) {
                console.log("Erro ao buscar usuário", err);
                navigate("/");
            }
        }

        loadUser();

        document.addEventListener("mousedown", handleClickOutside);
        return () => document.removeEventListener("mousedown", handleClickOutside);
    }, []);

    function handleDragStart(id) {
        setDragId(id);
    }

    function handleDragOver(e, id) {
        e.preventDefault();
        setDragOverId(id);

        if (id === dragId) return;

        const dragIndex = widgets.findIndex((w) => w.id === dragId);
        const overIndex = widgets.findIndex((w) => w.id === id);

        const novaLista = [...widgets];
        const [removido] = novaLista.splice(dragIndex, 1);
        novaLista.splice(overIndex, 0, removido);

        setWidgets(novaLista);
    }

    function handleDragEnd() {
        setDragId(null);
        setDragOverId(null);
    }

    function handleLogout() {
        localStorage.removeItem("token");
        navigate("/");
    }

    const iniciais = usuarioLogado?.nome?.charAt(0)?.toUpperCase() || "";

    return (
        <div className={styles.layout}>

            {mobileMenuOpen && (
                <div className={styles.overlay} onClick={() => setMobileMenuOpen(false)} />
            )}

            <aside
                className={`${styles.sidebar} ${collapsed ? styles.collapsed : ""} ${
                    mobileMenuOpen ? styles.mobileOpen : ""
                }`}
            >

                <div className={styles.sidebarTop}>
                    <div className={styles.sidebarLogo}>
                        <Dumbbell size={28} />
                        <h1>ManaGym</h1>
                    </div>

                    <button
                        className={styles.collapseBtn}
                        onClick={() => setCollapsed((c) => !c)}
                        title={collapsed ? "Expandir menu" : "Retrair menu"}
                    >
                        {collapsed ? <ChevronRight size={16} /> : <ChevronLeft size={16} />}
                    </button>

                    <button
                        className={styles.closeMobileBtn}
                        onClick={() => setMobileMenuOpen(false)}
                    >
                        <X size={20} />
                    </button>
                </div>

                <nav className={styles.nav}>
                    <a className={`${styles.navItem} ${styles.active}`} title="Dashboard">
                        <LayoutDashboard size={18} />
                        <span className={styles.navLabel}>Dashboard</span>
                    </a>

                    <a className={styles.navItem} title="Alunos">
                        <Users size={18} />
                        <span className={styles.navLabel}>Alunos</span>
                    </a>

                    <a className={styles.navItem} title="Planos">
                        <ClipboardList size={18} />
                        <span className={styles.navLabel}>Planos</span>
                    </a>

                    <a className={styles.navItem} title="Financeiro">
                        <DollarSign size={18} />
                        <span className={styles.navLabel}>Financeiro</span>
                    </a>

                    <Link
                        to="/settings"
                        className={styles.navItem}
                    >
                        <Settings size={18} />
                        <span className={styles.navLabel}>Configurações</span>
                    </Link>
                </nav>

                <button className={styles.logoutBtn} onClick={handleLogout} title="Sair">
                    <LogOut size={18} />
                    <span className={styles.navLabel}>Sair</span>
                </button>

            </aside>

            <main className={styles.main}>

                <header className={styles.topbar}>

                    <button
                        className={styles.hamburgerBtn}
                        onClick={() => setMobileMenuOpen(true)}
                    >
                        <Menu size={22} />
                    </button>

                    <div className={styles.profileWrapper} ref={profileRef}>
                        <div
                            className={styles.profile}
                            onClick={() => setOpenProfile((p) => !p)}
                        >
                            <div className={styles.avatar}>{iniciais}</div>
                            <span className={styles.profileName}>
                                {usuarioLogado?.nome || "Carregando..."}
                            </span>
                        </div>

                        {openProfile && usuarioLogado && (
                            <div className={styles.profileDropdown}>

                                <div className={styles.profileDropdownHeader}>
                                    <div className={styles.avatarLg}>{iniciais}</div>
                                    <div className={styles.profileInfo}>
                                        <strong>{usuarioLogado.nome}</strong>
                                        <span>{usuarioLogado.email}</span>
                                    </div>
                                </div>

                                <div className={styles.profileDivider} />

                                <a
                                    className={styles.profileMenuItem}
                                    onClick={() => {
                                        navigate("/settings");
                                    }}
                                >
                                    <Settings size={16} />
                                    Configurações
                                </a>

                                <button className={styles.profileLogout} onClick={handleLogout}>
                                    <LogOut size={16} />
                                    Sair da conta
                                </button>

                            </div>
                        )}
                    </div>
                </header>

                <section className={styles.board}>
                    {widgets.map((widget) => {
                        const Icon = widget.icon;

                        return (
                            <div
                                key={widget.id}
                                className={`${styles.widget} ${
                                    dragId === widget.id ? styles.dragging : ""
                                } ${dragOverId === widget.id && dragId !== widget.id ? styles.dragOver : ""}`}
                                draggable
                                onDragStart={() => handleDragStart(widget.id)}
                                onDragOver={(e) => handleDragOver(e, widget.id)}
                                onDragEnd={handleDragEnd}
                            >
                                <div className={styles.widgetHeader}>
                                    <div className={styles.widgetIcon}>
                                        <Icon size={26} />  
                                    </div>
                               
                                    <GripVertical size={18} className={styles.gripIcon} />
                                </div>

                                <span>
                                    {formatValue(widget.valor, format)}
                                </span>

                                <span className={styles.widgetValue}>{widget.valor}</span>
                                <span className={styles.widgetLabel}>{widget.titulo}</span>
                            </div>
                        );
                    })}
                </section>

            </main>

        </div>
    );
}