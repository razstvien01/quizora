import "./App.css";
import { Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import Explore from "./pages/Explore";
import NotFound from "./pages/NotFound";
import { ThemeProvider } from "./components/theme-provider";
import Auth from "./pages/Auth";

function App() {
  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/explore" element={<Explore />} />
        <Route path="*" element={<NotFound />} />
        <Route path="/auth" element={<Auth />} />
      </Routes>
    </ThemeProvider>
  );
}

export default App;
