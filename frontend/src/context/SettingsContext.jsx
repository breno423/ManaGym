import { createContext, useContext, useEffect, useState } from "react";

const SettingsContext = createContext();

export function SettingsProvider({ children }) {
    const [theme, setTheme] = useState("dark");
    const [format, setFormat] = useState("full");

    // carregar do storage
    useEffect(() => {
        const saved = localStorage.getItem("settings");

        if (saved) {
            const parsed = JSON.parse(saved);
            setTheme(parsed.theme || "dark");
            setFormat(parsed.format || "full");
        }
    }, []);

    // salvar sempre que mudar
    useEffect(() => {
        localStorage.setItem(
            "settings",
            JSON.stringify({ theme, format })
        );

        document.documentElement.setAttribute("data-theme", theme);
    }, [theme, format]);

    return (
        <SettingsContext.Provider
            value={{
                theme,
                setTheme,
                format,
                setFormat,
            }}
        >
            {children}
        </SettingsContext.Provider>
    );
}

export function useSettings() {
    return useContext(SettingsContext);
}