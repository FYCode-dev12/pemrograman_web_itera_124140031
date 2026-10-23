import React from 'react';
import Header from '../../components/Header/Header';
import { useTasks } from '../../context/TaskContext';
import './About.css';

function About() {
  const { stats } = useTasks();

  return (
    <div className="about">
      <Header
        title="Tentang Task Manager"
        description="Aplikasi Manajemen Tugas Praktikum Pemrograman Web"
      />

      <main className="container">
        <div className="about-content">
          <h2>Tentang Aplikasi</h2>
          <p>
            Aplikasi Task Manager ini dibangun menggunakan React modern dengan functional component,
            React Hooks (useState, useEffect), custom hooks, dan React Router untuk navigasi multi-halaman.
          </p>

          {/* Latihan Mandiri 5: Tampilkan Statistik di Halaman About */}
          <div className="global-stats-banner">
            <p className="stats-highlight">
              <strong>Saat ini Anda memiliki total {stats.total} tugas yang tersimpan di sistem.</strong>
            </p>
            <div className="stats-detail-chips">
              <span className="chip chip-success">Selesai: {stats.completed}</span>
              <span className="chip chip-pending">Tertunda: {stats.remaining}</span>
              <span className="chip chip-info">Progress: {stats.completionRate.toFixed(0)}%</span>
            </div>
          </div>

          <h3>Fitur Unggulan:</h3>
          <ul>
            <li>Manajemen tugas real-time (tambah, tandai selesai, hapus)</li>
            <li>Penyimpanan lokal persisten melalui localStorage</li>
            <li>Navigasi kilat tanpa refresh halaman dengan React Router</li>
            <li>State Global terintegrasi menggunakan Context API</li>
            <li>Deteksi ukuran layar responsif dengan custom hook useWindowSize</li>
            <li>Fitur hapus semua tugas dengan konfirmasi aman</li>
          </ul>
        </div>
      </main>
    </div>
  );
}

export default About;
