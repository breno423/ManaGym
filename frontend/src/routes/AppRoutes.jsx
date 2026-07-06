import { Routes, Route } from "react-router-dom";

import Login from "../pages/Login";
import Register from "../pages/Register";
import Dashboard from "../pages/Dashboard";
import Settings from "../pages/Settings";
import Alunos from "../pages/Alunos";

export default function AppRoutes() {
    return (
        <Routes>

            <Route path="/" element={<Login />} />

            <Route path="/register" element={<Register />} />

            <Route path="/dashboard" element={<Dashboard />} />

            <Route path="/settings" element={<Settings />} />

            <Route path="/alunos" element={<Alunos />}/>

        </Routes>
    );
}