import { useState, useEffect } from 'react';

/**
 * Custom Hook untuk sinkronisasi state React dengan browser localStorage
 * @param {string} key Kunci penyimpanan di localStorage
 * @param {*} initialValue Nilai awal jika data di localStorage belum tersedia
 * @returns {[any, Function]} Tuple [storedValue, setValue]
 */
export function useLocalStorage(key, initialValue) {
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error(`Gagal membaca key "${key}" dari localStorage:`, error);
      return initialValue;
    }
  });

  useEffect(() => {
    try {
      window.localStorage.setItem(key, JSON.stringify(storedValue));
    } catch (error) {
      console.error(`Gagal menyimpan key "${key}" ke localStorage:`, error);
    }
  }, [key, storedValue]);

  return [storedValue, setStoredValue];
}

export default useLocalStorage;
