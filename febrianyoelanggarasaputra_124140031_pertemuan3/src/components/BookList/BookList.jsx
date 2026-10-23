import React from 'react';
import PropTypes from 'prop-types';
import BookItem from '../BookItem/BookItem';
import './BookList.css';

function BookList({ books, onEdit, onDelete, onStatusChange, filterStatus, searchQuery, onResetFilter }) {
  if (books.length === 0) {
    return (
      <div className="empty-state">
        
        <h3>Tidak Ada Buku yang Ditemukan</h3>
        <p>
          {searchQuery
            ? `Tidak ada buku yang cocok dengan kata kunci "${searchQuery}".`
            : filterStatus !== 'semua'
            ? `Belum ada buku dengan status "${filterStatus}".`
            : 'Koleksi buku Anda masih kosong. Mulai tambahkan buku pertama Anda!'}
        </p>
        {(searchQuery || filterStatus !== 'semua') && (
          <button className="btn btn-secondary reset-btn" onClick={onResetFilter}>
            Tampilkan Semua Buku
          </button>
        )}
      </div>
    );
  }

  return (
    <div className="book-grid">
      {books.map((book) => (
        <BookItem
          key={book.id}
          book={book}
          onEdit={onEdit}
          onDelete={onDelete}
          onStatusChange={onStatusChange}
        />
      ))}
    </div>
  );
}

BookList.propTypes = {
  books: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      title: PropTypes.string.isRequired,
      author: PropTypes.string.isRequired,
      status: PropTypes.string.isRequired,
    })
  ).isRequired,
  onEdit: PropTypes.func.isRequired,
  onDelete: PropTypes.func.isRequired,
  onStatusChange: PropTypes.func.isRequired,
  filterStatus: PropTypes.string.isRequired,
  searchQuery: PropTypes.string.isRequired,
  onResetFilter: PropTypes.func.isRequired,
};

export default BookList;
