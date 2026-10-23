import React, { useState } from 'react';
import Card from '../../components/Card/Card';
import BookForm from '../../components/BookForm/BookForm';
import BookFilter from '../../components/BookFilter/BookFilter';
import BookList from '../../components/BookList/BookList';
import Modal from '../../components/Modal/Modal';
import { useBooks } from '../../context/BookContext';
import './Home.css';

function Home() {
  const {
    filteredBooks,
    filterStatus,
    setFilterStatus,
    searchQuery,
    setSearchQuery,
    addBook,
    updateBook,
    deleteBook,
    stats,
  } = useBooks();

  const [isAddModalOpen, setIsAddModalOpen] = useState(false);
  const [editingBookData, setEditingBookData] = useState(null);
  const [deleteCandidate, setDeleteCandidate] = useState(null);

  const handleAddSubmit = (bookData) => {
    addBook(bookData);
    setIsAddModalOpen(false);
  };

  const handleEditClick = (book) => {
    setEditingBookData(book);
  };

  const handleUpdateSubmit = (updatedData) => {
    if (editingBookData) {
      updateBook(editingBookData.id, updatedData);
      setEditingBookData(null);
    }
  };

  const handleDeletePrompt = (id, title) => {
    setDeleteCandidate({ id, title });
  };

  const handleConfirmDelete = () => {
    if (deleteCandidate) {
      deleteBook(deleteCandidate.id);
      setDeleteCandidate(null);
    }
  };

  const handleStatusChange = (id, newStatus) => {
    updateBook(id, { status: newStatus });
  };

  return (
    <div className="home-page">
      {/* Hero Banner */}
      <section className="hero-banner">
        <div className="container hero-content">
          <div>
            <h1 className="hero-title">Kelola Koleksi Buku Pribadi Anda</h1>
            <p className="hero-subtitle">
              Catat buku yang Anda miliki, sedang dibaca, atau rencanakan untuk dibeli dengan mudah dan terorganisir.
            </p>
          </div>
          <button className="btn btn-hero" onClick={() => setIsAddModalOpen(true)}>
            Tambah Buku Baru
          </button>
        </div>
      </section>

      <main className="container main-content">
        {/* Quick Stats Grid */}
        <section className="quick-stats-row">
          <div className="stat-card stat-total">
            <div>
              <span className="stat-value">{stats.total}</span>
              <span className="stat-label">Total Buku</span>
            </div>
          </div>
          <div className="stat-card stat-milik">
            <div>
              <span className="stat-value">{stats.milik}</span>
              <span className="stat-label">Dimiliki</span>
            </div>
          </div>
          <div className="stat-card stat-baca">
            <div>
              <span className="stat-value">{stats.baca}</span>
              <span className="stat-label">Sedang Dibaca</span>
            </div>
          </div>
          <div className="stat-card stat-beli">
            <div>
              <span className="stat-value">{stats.beli}</span>
              <span className="stat-label">Rencana Beli</span>
            </div>
          </div>
        </section>

        {/* Filter and Search */}
        <BookFilter
          currentFilter={filterStatus}
          onFilterChange={setFilterStatus}
          searchQuery={searchQuery}
          onSearchChange={setSearchQuery}
          stats={stats}
        />

        {/* Book List Section */}
        <div className="list-header">
          <h2>
            Daftar Buku
            <span className="results-count">({filteredBooks.length} buku ditampilkan)</span>
          </h2>
          <button className="btn btn-primary btn-sm" onClick={() => setIsAddModalOpen(true)}>
            Tambah Buku
          </button>
        </div>

        <BookList
          books={filteredBooks}
          onEdit={handleEditClick}
          onDelete={handleDeletePrompt}
          onStatusChange={handleStatusChange}
          filterStatus={filterStatus}
          searchQuery={searchQuery}
          onResetFilter={() => {
            setFilterStatus('semua');
            setSearchQuery('');
          }}
        />
      </main>

      {/* Modal Tambah Buku */}
      <Modal
        isOpen={isAddModalOpen}
        onClose={() => setIsAddModalOpen(false)}
        title="Tambah Buku Baru ke Koleksi"
      >
        <BookForm
          onSubmit={handleAddSubmit}
          onCancel={() => setIsAddModalOpen(false)}
          submitButtonText="Tambahkan Buku"
        />
      </Modal>

      {/* Modal Edit Buku */}
      <Modal
        isOpen={!!editingBookData}
        onClose={() => setEditingBookData(null)}
        title="Edit Informasi Buku"
      >
        {editingBookData && (
          <BookForm
            initialData={editingBookData}
            onSubmit={handleUpdateSubmit}
            onCancel={() => setEditingBookData(null)}
            submitButtonText="Perbarui Buku"
          />
        )}
      </Modal>

      {/* Modal Konfirmasi Hapus */}
      <Modal
        isOpen={!!deleteCandidate}
        onClose={() => setDeleteCandidate(null)}
        title="Konfirmasi Hapus Buku"
      >
        {deleteCandidate && (
          <div className="delete-confirm-box">
            <p>
              Apakah Anda yakin ingin menghapus buku <strong>"{deleteCandidate.title}"</strong> dari koleksi Anda?
            </p>
            <p className="delete-warning">Tindakan ini tidak dapat dibatalkan.</p>
            <div className="modal-actions">
              <button
                type="button"
                className="btn btn-secondary"
                onClick={() => setDeleteCandidate(null)}
              >
                Batal
              </button>
              <button
                type="button"
                className="btn btn-danger"
                onClick={handleConfirmDelete}
              >
                Hapus Buku
              </button>
            </div>
          </div>
        )}
      </Modal>
    </div>
  );
}

export default Home;
