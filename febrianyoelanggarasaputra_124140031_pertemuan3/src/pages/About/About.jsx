import React from 'react';
import Card from '../../components/Card/Card';
import './About.css';

function About() {
  return (
    <div className="about-page">
      <div className="container">
        <header className="page-header">
          <h1 className="page-title">Tentang Aplikasi</h1>
          <p className="page-description">
            Informasi pengembang dan detail implementasi teknologi React.
          </p>
        </header>

        <div className="about-grid">
          {/* Kartu Profil Mahasiswa */}
          <Card title="Identitas Praktikan" subtitle="Pengembangan Aplikasi Web - Pertemuan 3">
            <div className="profile-info-list">
              <div className="profile-row">
                <span className="profile-label">Nama Lengkap</span>
                <span className="profile-val">Febrian Yoel Anggara Saputra</span>
              </div>
              <div className="profile-row">
                <span className="profile-label">NIM</span>
                <span className="profile-val">124140031</span>
              </div>
              <div className="profile-row">
                <span className="profile-label">Program Studi</span>
                <span className="profile-val">Teknik Informatika</span>
              </div>
              <div className="profile-row">
                <span className="profile-label">Institusi</span>
                <span className="profile-val">Institut Teknologi Sumatera (ITERA)</span>
              </div>
            </div>
          </Card>

          {/* Arsitektur Teknologi */}
          <Card title="Teknologi & Fitur React" subtitle="Penerapan konsep modern React">
            <ul className="feature-checklist">
              <li>
                <strong>Functional Components & Hooks:</strong> Menggunakan <code>useState</code> untuk state lokal dan <code>useEffect</code> untuk side-effects sinkronisasi.
              </li>
              <li>
                <strong>Custom Hooks:</strong>
                <ul>
                  <li><code>useLocalStorage.js</code>: Abstraksi persistensi state ke local storage browser dengan penanganan JSON aman.</li>
                  <li><code>useBookStats.js</code>: Memoized kalkulasi metrik statistik koleksi buku.</li>
                </ul>
              </li>
              <li>
                <strong>Global State (Context API):</strong>
                <code>BookContext.jsx</code> mengelola buku, filter status, query pencarian, serta fungsi CRUD tanpa prop drilling.
              </li>
              <li>
                <strong>Multi-Page Routing:</strong>
                Menggunakan <code>react-router-dom</code> dengan navigasi Beranda (Koleksi), Statistik, Tentang, dan rute fallback 404 Not Found.
              </li>
              <li>
                <strong>Type Checking:</strong>
                Seluruh komponen reusable diperiksa menggunakan <code>PropTypes</code> untuk menjamin keutuhan data.
              </li>
              <li>
                <strong>Testing Otomatis:</strong>
                Unit testing menggunakan Vitest dan React Testing Library untuk memastikan fungsionalitas rendering, penambahan, penghapusan, filter, dan validasi form.
              </li>
            </ul>
          </Card>
        </div>
      </div>
    </div>
  );
}

export default About;
