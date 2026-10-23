import React, { createContext, useContext, useState, useMemo } from 'react';
import PropTypes from 'prop-types';
import useLocalStorage from '../hooks/useLocalStorage';
import useBookStats from '../hooks/useBookStats';

const BookContext = createContext(null);

const DEFAULT_BOOKS = [
  {
    id: 1,
    title: 'Clean Code: A Handbook of Agile Software Craftsmanship',
    author: 'Robert C. Martin',
    status: 'milik',
    year: 2008,
    category: 'Rekayasa Perangkat Lunak',
    notes: 'Buku wajib untuk memahami best practice penulisan kode bersih.',
    createdAt: '2026-01-10T10:00:00.000Z'
  },
  {
    id: 2,
    title: 'Designing Data-Intensive Applications',
    author: 'Martin Kleppmann',
    status: 'baca',
    year: 2017,
    category: 'Sistem Terdistribusi',
    notes: 'Sedang membaca bab tentang Replikasi dan Partisi Basis Data.',
    createdAt: '2026-02-14T14:30:00.000Z'
  },
  {
    id: 3,
    title: 'The Pragmatic Programmer: 20th Anniversary Edition',
    author: 'David Thomas & Andrew Hunt',
    status: 'beli',
    year: 2019,
    category: 'Pengembangan Diri Pemrogram',
    notes: 'Rencana dibeli saat promo tanggal kembar bulan depan.',
    createdAt: '2026-03-01T09:15:00.000Z'
  },
  {
    id: 4,
    title: 'JavaScript: The Definitive Guide',
    author: 'David Flanagan',
    status: 'milik',
    year: 2020,
    category: 'Web Development',
    notes: 'Referensi utama fitur modern ECMAScript.',
    createdAt: '2026-03-20T11:20:00.000Z'
  }
];

export function useBooks() {
  const context = useContext(BookContext);
  if (!context) {
    throw new Error('useBooks harus digunakan di dalam BookProvider');
  }
  return context;
}

export function BookProvider({ children }) {
  const [books, setBooks] = useLocalStorage('personal_book_manager_data', DEFAULT_BOOKS);
  const [filterStatus, setFilterStatus] = useState('semua');
  const [searchQuery, setSearchQuery] = useState('');
  const [editingBook, setEditingBook] = useState(null);

  // Fungsi Tambah Buku
  const addBook = (newBookData) => {
    const newBook = {
      ...newBookData,
      id: Date.now(),
      createdAt: new Date().toISOString(),
    };
    setBooks((prev) => [newBook, ...prev]);
    return newBook;
  };

  // Fungsi Update Buku
  const updateBook = (id, updatedFields) => {
    setBooks((prev) =>
      prev.map((b) => (b.id === id ? { ...b, ...updatedFields } : b))
    );
    if (editingBook && editingBook.id === id) {
      setEditingBook(null);
    }
  };

  // Fungsi Hapus Buku
  const deleteBook = (id) => {
    setBooks((prev) => prev.filter((b) => b.id !== id));
    if (editingBook && editingBook.id === id) {
      setEditingBook(null);
    }
  };

  // Filter & Search yang di-memoize
  const filteredBooks = useMemo(() => {
    return books.filter((book) => {
      const matchStatus = filterStatus === 'semua' || book.status === filterStatus;
      const query = searchQuery.trim().toLowerCase();
      const matchQuery =
        !query ||
        book.title.toLowerCase().includes(query) ||
        book.author.toLowerCase().includes(query) ||
        (book.category && book.category.toLowerCase().includes(query));
      return matchStatus && matchQuery;
    });
  }, [books, filterStatus, searchQuery]);

  // Statistik dihitung via custom hook useBookStats
  const stats = useBookStats(books);

  const value = {
    books,
    filteredBooks,
    filterStatus,
    setFilterStatus,
    searchQuery,
    setSearchQuery,
    addBook,
    updateBook,
    deleteBook,
    editingBook,
    setEditingBook,
    stats,
  };

  return <BookContext.Provider value={value}>{children}</BookContext.Provider>;
}

BookProvider.propTypes = {
  children: PropTypes.node.isRequired,
};

export default BookContext;
