import React from 'react';
import PropTypes from 'prop-types';
import './BookItem.css';

function BookItem({ book, onEdit, onDelete, onStatusChange }) {
  const getStatusBadge = (status) => {
    switch (status) {
      case 'milik':
        return { label: 'Dimiliki', className: 'badge-milik' };
      case 'baca':
        return { label: 'Sedang Dibaca', className: 'badge-baca' };
      case 'beli':
        return { label: 'Rencana Beli', className: 'badge-beli' };
      default:
        return { label: status, className: 'badge-default' };
    }
  };

  const badge = getStatusBadge(book.status);

  return (
    <div className={`book-item-card status-${book.status}`}>
      <div className="book-item-top">
        <div className="book-info">
          <div className="badge-row">
            <span className={`status-badge ${badge.className}`}>
              {badge.label}
            </span>
            {book.category && <span className="category-pill">{book.category}</span>}
            {book.year && <span className="year-pill">Tahun {book.year}</span>}
          </div>
          <h4 className="book-title">{book.title}</h4>
          <p className="book-author">Oleh: <strong>{book.author}</strong></p>
        </div>
      </div>

      {book.notes && (
        <div className="book-notes">
          <p>{book.notes}</p>
        </div>
      )}

      <div className="book-item-footer">
        {/* Dropdown Ubah Status Cepat */}
        <div className="quick-status-selector">
          <label htmlFor={`quick-status-${book.id}`}>Ubah status:</label>
          <select
            id={`quick-status-${book.id}`}
            value={book.status}
            onChange={(e) => onStatusChange(book.id, e.target.value)}
            className="status-select"
            aria-label="Ubah status buku"
          >
            <option value="milik">Dimiliki</option>
            <option value="baca">Sedang Dibaca</option>
            <option value="beli">Rencana Beli</option>
          </select>
        </div>

        {/* Tombol Aksi */}
        <div className="book-actions">
          <button
            className="btn-action btn-edit"
            onClick={() => onEdit(book)}
            title="Edit buku"
            aria-label={`Edit ${book.title}`}
          >
            Edit
          </button>
          <button
            className="btn-action btn-delete"
            onClick={() => onDelete(book.id, book.title)}
            title="Hapus buku"
            aria-label={`Hapus ${book.title}`}
          >
            Hapus
          </button>
        </div>
      </div>
    </div>
  );
}

BookItem.propTypes = {
  book: PropTypes.shape({
    id: PropTypes.number.isRequired,
    title: PropTypes.string.isRequired,
    author: PropTypes.string.isRequired,
    status: PropTypes.string.isRequired,
    year: PropTypes.oneOfType([PropTypes.number, PropTypes.string]),
    category: PropTypes.string,
    notes: PropTypes.string,
  }).isRequired,
  onEdit: PropTypes.func.isRequired,
  onDelete: PropTypes.func.isRequired,
  onStatusChange: PropTypes.func.isRequired,
};

export default BookItem;
