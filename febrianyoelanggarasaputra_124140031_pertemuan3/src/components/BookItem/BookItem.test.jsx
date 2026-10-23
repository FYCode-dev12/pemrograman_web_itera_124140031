import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import BookItem from './BookItem';

describe('Komponen BookItem', () => {
  const dummyBook = {
    id: 101,
    title: 'Atomic Habits',
    author: 'James Clear',
    status: 'milik',
    year: 2018,
    category: 'Self Improvement',
    notes: 'Buku sangat inspiratif tentang pembentukan kebiasaan kecil.',
  };

  const mockEdit = vi.fn();
  const mockDelete = vi.fn();
  const mockStatusChange = vi.fn();

  beforeEach(() => {
    vi.clearAllMocks();
  });

  test('Test 1: Merender informasi judul, penulis, dan status buku dengan benar', () => {
    render(
      <BookItem
        book={dummyBook}
        onEdit={mockEdit}
        onDelete={mockDelete}
        onStatusChange={mockStatusChange}
      />
    );

    expect(screen.getByText('Atomic Habits')).toBeInTheDocument();
    expect(screen.getByText('James Clear')).toBeInTheDocument();
    expect(screen.getAllByText(/Dimiliki/)[0]).toBeInTheDocument();
    expect(screen.getByText('Tahun 2018')).toBeInTheDocument();
  });

  test('Test 2: Memanggil handler onDelete ketika tombol Hapus diklik', () => {
    render(
      <BookItem
        book={dummyBook}
        onEdit={mockEdit}
        onDelete={mockDelete}
        onStatusChange={mockStatusChange}
      />
    );

    const deleteButton = screen.getByText(/Hapus/);
    fireEvent.click(deleteButton);
    expect(mockDelete).toHaveBeenCalledWith(101, 'Atomic Habits');
  });

  test('Test 3: Memanggil handler onEdit ketika tombol Edit diklik', () => {
    render(
      <BookItem
        book={dummyBook}
        onEdit={mockEdit}
        onDelete={mockDelete}
        onStatusChange={mockStatusChange}
      />
    );

    const editButton = screen.getByText(/Edit/);
    fireEvent.click(editButton);
    expect(mockEdit).toHaveBeenCalledWith(dummyBook);
  });

  test('Test 4: Memanggil onStatusChange saat memilih opsi status baru dari dropdown', () => {
    render(
      <BookItem
        book={dummyBook}
        onEdit={mockEdit}
        onDelete={mockDelete}
        onStatusChange={mockStatusChange}
      />
    );

    const select = screen.getByRole('combobox', { name: /Ubah status buku/i });
    fireEvent.change(select, { target: { value: 'baca' } });
    expect(mockStatusChange).toHaveBeenCalledWith(101, 'baca');
  });
});
