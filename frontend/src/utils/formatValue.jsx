export function formatValue(value, format) {
    if (value === null || value === undefined) return "";

    if (format === "compact") {
        return new Intl.NumberFormat("pt-BR", {
            notation: "compact",
        }).format(value);
    }

    return value.toLocaleString("pt-BR");
}