import React from 'react';
import { Link } from 'react-router-dom';
import Header from '../../components/Header/Header';
import './NotFound.css';

function NotFound() {
  return (
    <div className="not-found">
      <Header title="404 - Halaman Tidak Ditemukan" description="Halaman yang Anda tuju tidak tersedia" />
      <main className="container">
        <div className="not-found-card">
          <div className="error-code">404</div>
          <h2>Oops! Halaman Tidak Ada</h2>
          <p>Halaman atau rute yang Anda masukkan tidak terdaftar dalam sistem Task Manager.</p>
          <Link to="/" className="back-home-btn">Kembali ke Beranda</Link>
        </div>
      </main>
    </div>
  );
}

export default NotFound;
