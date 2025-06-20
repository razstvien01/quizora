import "./App.css";
import { Route } from "react-router-dom";
import Home from "./pages/Home";
import Explore from "./pages/Explore";
import NotFound from "./pages/NotFound";

function App() {
  return (
    <Route>
      <Route path="/" element={<Home />} />
      <Route path="/explore" element={<Explore />} />
      <Route path="*" element={<NotFound />} />
    </Route>
  );
}

export default App;
