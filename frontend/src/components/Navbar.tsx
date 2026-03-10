import { Link } from "react-router-dom";
import { useState } from "react";
import "./Navbar.css";

function Navbar() {
  const [menuOpen, setMenuOpen] = useState(false);

  return (
    <nav>
      <div className="nav-logo">
        <img src="./icon2.png" alt="Fade & Blade" />
      </div>

      <button className="burger" onClick={() => setMenuOpen(!menuOpen)}>
        ☰
      </button>

      <ul className={`nav-links ${menuOpen ? "open" : ""}`}>
        <li>
          <Link to="/" onClick={() => setMenuOpen(false)}>
            Home
          </Link>
        </li>
        <li>
          <Link to="/services" onClick={() => setMenuOpen(false)}>
            Services
          </Link>
        </li>
        <li>
          <Link to="/login" onClick={() => setMenuOpen(false)}>
            Members Login
          </Link>
        </li>
        <li>
          <Link to="/staff" onClick={() => setMenuOpen(false)}>
            Staff Login
          </Link>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;
