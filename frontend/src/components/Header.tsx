import { Link } from "react-router-dom";

export default function Header() {
  return (
    <header className="py-4 shadow">
      <div className="container mx-auto px-4 flex justify-between items-center">
        <Link to="/" className="text-xl font-bold">
          Quizora
        </Link>
        <nav>
          <Link to="/" className="hover:underline">
            Home
          </Link>
          <Link to="/explore" className="hover:underline">
            Explore
          </Link>
        </nav>
      </div>
    </header>
  );
}
