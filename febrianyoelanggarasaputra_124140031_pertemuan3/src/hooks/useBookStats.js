import { useMemo } from 'react';

/**
 * Custom Hook untuk menghitung metrik statistik koleksi buku
 * @param {Array} books Daftar array data buku
 * @returns {Object} Statistik buku (total, milik, baca, beli, persentase)
 */
export function useBookStats(books = []) {
  return useMemo(() => {
    const total = books.length;
    const milik = books.filter((b) => b.status === 'milik').length;
    const baca = books.filter((b) => b.status === 'baca').length;
    const beli = books.filter((b) => b.status === 'beli').length;

    const percentMilik = total > 0 ? Math.round((milik / total) * 100) : 0;
    const percentBaca = total > 0 ? Math.round((baca / total) * 100) : 0;
    const percentBeli = total > 0 ? Math.round((beli / total) * 100) : 0;

    return {
      total,
      milik,
      baca,
      beli,
      percentMilik,
      percentBaca,
      percentBeli,
    };
  }, [books]);
}

export default useBookStats;
