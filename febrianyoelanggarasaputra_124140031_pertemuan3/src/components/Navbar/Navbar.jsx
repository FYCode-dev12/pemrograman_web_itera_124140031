import React from 'react';
import { NavLink, Link } from 'react-router-dom';
import PropTypes from 'prop-types';
import './Navbar.css';

function Navbar({ totalBooks }) {
  return (
    <nav className="app-navbar">
      <div className="container nav-content">
        <Link to="/" className="brand-logo">
          
          <div className="brand-text">
            <span className="brand-title">PustakaKu</span>
            <span className="brand-subtitle">Manajemen Buku Pribadi</span>
          </div>
        </Link>
        <ul className="nav-menu">
          <li>
            <NavLink
              to="/"
              className={({ isActive }) => (isActive ? 'nav-link active' : 'nav-link')}
              end
            >
              Koleksi Buku
              {totalBooks > 0 && <span className="nav-counter">{totalBooks}</span>}
            </NavLink>
          </li>
          <li>
            <NavLink
              to="/stats"
              className={({ isActive }) => (isActive ? 'nav-link active' : 'nav-link')}
            >
              Statistik
            </NavLink>
          </li>
          <li>
            <NavLink
              to="/about"
              className={({ isActive }) => (isActive ? 'nav-link active' : 'nav-link')}
            >
              Tentang
            </NavLink>
          </li>
        </ul>
      </div>
    </nav>
  );
}

Navbar.propTypes = {
  totalBooks: PropTypes.number,
};

Navbar.defaultProps = {
  totalBooks: 0,
};

export default Navbar;
