import AppRoutes from "./routes/AppRoutes";
import { useSettings } from "./context/SettingsContext";

function App() {
    const { theme } = useSettings();

    return (
        <div data-theme={theme}>
            <AppRoutes />
        </div>
    );
}

export default App;