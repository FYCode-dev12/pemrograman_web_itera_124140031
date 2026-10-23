import React from 'react';
import { Link } from 'react-router-dom';
import Card from '../../components/Card/Card';
import './NotFound.css';

function NotFound() {
  return (
    <div className="notfound-page">
      <div className="container">
        <Card className="notfound-card">
          <div className="notfound-code">404</div>
          <h2>Halaman Tidak Ditemukan</h2>
          <p>
            Maaf, halaman yang Anda tuju tidak ditemukan atau alamat URL salah.
          </p>
          <Link to="/" className="btn btn-primary">
            Kembali ke Koleksi Buku
          </Link>
        </Card>
      </div>
    </div>
  );
}

export default NotFound;
