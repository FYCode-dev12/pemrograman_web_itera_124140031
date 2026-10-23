import React from 'react';
import Card from '../../components/Card/Card';
import { useBooks } from '../../context/BookContext';
import './Stats.css';

function Stats() {
  const { books, stats } = useBooks();

  const recentBooks = [...books].slice(0, 5);

  return (
    <div className="stats-page">
      <div className="container">
        <header className="page-header">
          <h1 className="page-title">Statistik & Analisis Koleksi Buku</h1>
          <p className="page-description">
            Lihat ringkasan menyeluruh mengenai status buku yang Anda miliki, sedang dibaca, maupun rencana pembelian.
          </p>
        </header>

        {/* Kartu Ringkasan Atas */}
        <div className="stats-overview-grid">
          <Card className="metric-card">
            <span className="metric-badge">Total</span>
            <div className="metric-number">{stats.total}</div>
            <p className="metric-label">Seluruh buku yang tercatat di sistem</p>
          </Card>
          <Card className="metric-card metric-milik">
            <span className="metric-badge">Dimiliki</span>
            <div className="metric-number">{stats.milik}</div>
            <p className="metric-label">{stats.percentMilik}% dari seluruh koleksi</p>
          </Card>
          <Card className="metric-card metric-baca">
            <span className="metric-badge">Sedang Dibaca</span>
            <div className="metric-number">{stats.baca}</div>
            <p className="metric-label">{stats.percentBaca}% buku sedang aktif dipelajari</p>
          </Card>
          <Card className="metric-card metric-beli">
            <span className="metric-badge">Rencana Beli</span>
            <div className="metric-number">{stats.beli}</div>
            <p className="metric-label">{stats.percentBeli}% wishlist buku incaran</p>
          </Card>
        </div>

        {/* Progress Bar Visualisasi */}
        <Card title="Distribusi Koleksi Buku" subtitle="Visualisasi persentase status buku">
          <div className="distribution-container">
            <div className="progress-bar-stacked">
              <div
                className="progress-segment seg-milik"
                style={{ width: `${stats.percentMilik}%` }}
                title={`Milik: ${stats.percentMilik}%`}
              ></div>
              <div
                className="progress-segment seg-baca"
                style={{ width: `${stats.percentBaca}%` }}
                title={`Baca: ${stats.percentBaca}%`}
              ></div>
              <div
                className="progress-segment seg-beli"
                style={{ width: `${stats.percentBeli}%` }}
                title={`Beli: ${stats.percentBeli}%`}
              ></div>
            </div>

            <div className="distribution-legend">
              <div className="legend-item">
                <span className="legend-dot dot-milik"></span>
                <span>Dimiliki: <strong>{stats.milik} ({stats.percentMilik}%)</strong></span>
              </div>
              <div className="legend-item">
                <span className="legend-dot dot-baca"></span>
                <span>Sedang Dibaca: <strong>{stats.baca} ({stats.percentBaca}%)</strong></span>
              </div>
              <div className="legend-item">
                <span className="legend-dot dot-beli"></span>
                <span>Rencana Beli: <strong>{stats.beli} ({stats.percentBeli}%)</strong></span>
              </div>
            </div>
          </div>
        </Card>

        {/* Tabel Koleksi Terbaru */}
        <Card title="Buku yang Baru Ditambahkan" subtitle="5 buku terakhir dalam catatan Anda">
          {recentBooks.length === 0 ? (
            <p className="empty-text">Belum ada buku yang tercatat.</p>
          ) : (
            <div className="recent-table-wrapper">
              <table className="recent-table">
                <thead>
                  <tr>
                    <th>Judul Buku</th>
                    <th>Penulis</th>
                    <th>Status</th>
                    <th>Kategori</th>
                  </tr>
                </thead>
                <tbody>
                  {recentBooks.map((b) => (
                    <tr key={b.id}>
                      <td className="font-semibold">{b.title}</td>
                      <td>{b.author}</td>
                      <td>
                        <span className={`tag-status status-${b.status}`}>
                          {b.status === 'milik'
                            ? 'Dimiliki'
                            : b.status === 'baca'
                            ? 'Sedang Dibaca'
                            : 'Rencana Beli'}
                        </span>
                      </td>
                      <td>{b.category || '-'}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </Card>
      </div>
    </div>
  );
}

export default Stats;
