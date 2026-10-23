import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { BookProvider, useBooks } from './context/BookContext';
import Navbar from './components/Navbar/Navbar';
import Home from './pages/Home/Home';
import Stats from './pages/Stats/Stats';
import About from './pages/About/About';
import NotFound from './pages/NotFound/NotFound';
import './App.css';

function AppContent() {
  const { stats } = useBooks();

  return (
    <div className="app-layout">
      <Navbar totalBooks={stats.total} />
      <div className="app-body">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/stats" element={<Stats />} />
          <Route path="/about" element={<About />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </div>
      <footer className="app-footer">
        <div className="container footer-content">
          <p>© 2026 Aplikasi Manajemen Buku Pribadi • Praktikum Pemrograman Web ITERA</p>
          <p className="footer-nim">Febrian Yoel Anggara Saputra - 124140031</p>
        </div>
      </footer>
    </div>
  );
}

function App() {
  return (
    <Router>
      <BookProvider>
        <AppContent />
      </BookProvider>
    </Router>
  );
}

export default App;
