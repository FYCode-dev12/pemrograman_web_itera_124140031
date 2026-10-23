import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import BookFilter from './BookFilter';

describe('Komponen BookFilter', () => {
  const mockStats = { total: 10, milik: 5, baca: 3, beli: 2 };
  const mockFilterChange = vi.fn();
  const mockSearchChange = vi.fn();

  test('Test 7: Memanggil onFilterChange saat tab status diklik', () => {
    render(
      <BookFilter
        currentFilter="semua"
        onFilterChange={mockFilterChange}
        searchQuery=""
        onSearchChange={mockSearchChange}
        stats={mockStats}
      />
    );

    const bacaTab = screen.getByText('Sedang Dibaca');
    fireEvent.click(bacaTab);
    expect(mockFilterChange).toHaveBeenCalledWith('baca');
  });

  test('Test 8: Memanggil onSearchChange saat mengetik di input pencarian', () => {
    render(
      <BookFilter
        currentFilter="semua"
        onFilterChange={mockFilterChange}
        searchQuery=""
        onSearchChange={mockSearchChange}
        stats={mockStats}
      />
    );

    const searchInput = screen.getByPlaceholderText(/Cari berdasarkan judul/i);
    fireEvent.change(searchInput, { target: { value: 'clean code' } });
    expect(mockSearchChange).toHaveBeenCalledWith('clean code');
  });
});
