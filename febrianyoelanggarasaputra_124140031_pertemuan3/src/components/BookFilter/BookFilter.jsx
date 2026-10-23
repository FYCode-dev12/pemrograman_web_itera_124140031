import React from 'react';
import PropTypes from 'prop-types';
import './BookFilter.css';

function BookFilter({ currentFilter, onFilterChange, searchQuery, onSearchChange, stats }) {
  const filterOptions = [
    { key: 'semua', label: 'Semua', count: stats.total },
    { key: 'milik', label: 'Dimiliki', count: stats.milik },
    { key: 'baca', label: 'Sedang Dibaca', count: stats.baca },
    { key: 'beli', label: 'Rencana Beli', count: stats.beli },
  ];

  return (
    <div className="book-filter-container">
      {/* Search Input */}
      <div className="search-bar">
        
        <input
          type="text"
          placeholder="Cari berdasarkan judul, penulis, atau kategori..."
          value={searchQuery}
          onChange={(e) => onSearchChange(e.target.value)}
          aria-label="Pencarian buku"
        />
        {searchQuery && (
          <button
            className="clear-search-btn"
            onClick={() => onSearchChange('')}
            title="Hapus pencarian"
          >
            &times;
          </button>
        )}
      </div>

      {/* Filter Tabs */}
      <div className="filter-tabs" role="tablist">
        {filterOptions.map((opt) => (
          <button
            key={opt.key}
            role="tab"
            aria-selected={currentFilter === opt.key}
            className={`filter-tab ${currentFilter === opt.key ? 'active' : ''}`}
            onClick={() => onFilterChange(opt.key)}
          >
            
            <span className="filter-tab-label">{opt.label}</span>
            <span className="filter-badge">{opt.count}</span>
          </button>
        ))}
      </div>
    </div>
  );
}

BookFilter.propTypes = {
  currentFilter: PropTypes.string.isRequired,
  onFilterChange: PropTypes.func.isRequired,
  searchQuery: PropTypes.string.isRequired,
  onSearchChange: PropTypes.func.isRequired,
  stats: PropTypes.shape({
    total: PropTypes.number.isRequired,
    milik: PropTypes.number.isRequired,
    baca: PropTypes.number.isRequired,
    beli: PropTypes.number.isRequired,
  }).isRequired,
};

export default BookFilter;
