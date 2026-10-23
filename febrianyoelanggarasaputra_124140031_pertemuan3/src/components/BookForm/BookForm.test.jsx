import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import BookForm from './BookForm';

describe('Komponen BookForm (Validasi & Error Handling)', () => {
  const mockSubmit = vi.fn();

  beforeEach(() => {
    vi.clearAllMocks();
  });

  test('Test 5: Menampilkan pesan error validasi ketika field wajib (judul & penulis) kosong', () => {
    render(<BookForm onSubmit={mockSubmit} />);

    const submitBtn = screen.getByRole('button', { name: /Simpan Buku/i });
    fireEvent.click(submitBtn);

    expect(screen.getByText(/Judul buku wajib diisi!/i)).toBeInTheDocument();
    expect(screen.getByText(/Nama penulis wajib diisi!/i)).toBeInTheDocument();
    expect(mockSubmit).not.toHaveBeenCalled();
  });

  test('Test 6: Berhasil submit data ketika form diisi dengan valid', () => {
    render(<BookForm onSubmit={mockSubmit} />);

    const titleInput = screen.getByPlaceholderText(/Contoh: Belajar React Modern/i);
    const authorInput = screen.getByPlaceholderText(/Contoh: Dan Abramov/i);
    const submitBtn = screen.getByRole('button', { name: /Simpan Buku/i });

    fireEvent.change(titleInput, { target: { value: 'Refactoring' } });
    fireEvent.change(authorInput, { target: { value: 'Martin Fowler' } });
    fireEvent.click(submitBtn);

    expect(mockSubmit).toHaveBeenCalledTimes(1);
    expect(mockSubmit).toHaveBeenCalledWith(
      expect.objectContaining({
        title: 'Refactoring',
        author: 'Martin Fowler',
        status: 'milik',
      })
    );
  });
});
