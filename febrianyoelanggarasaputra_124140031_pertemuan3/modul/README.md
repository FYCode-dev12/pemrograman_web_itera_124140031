# Latihan Modul Praktikum 3: React Basics

Repositori ini memuat implementasi seluruh materi pembelajaran dan **Latihan Mandiri** pada Modul Praktikum 3 (React Basics):

## Ringkasan Fitur & Latihan Mandiri yang Diselesaikan

1. **Submodul 0: Konsep Dasar React**
   - Disertakan file contoh HTML + React 18 & Babel Standalone via CDN di `cdn-react.html`.
2. **Submodul 1: Setup Project React**
   - Struktur folder modular: `components`, `pages`, `hooks`, `context`.
   - **Latihan Mandiri 1 (Eksplorasi HMR)**: Mengubah warna background header ke `#0d9488`.
3. **Submodul 2: Components & Props**
   - Komponen terstruktur: `Header`, `TaskItem`, `TaskForm`.
   - Penerapan `PropTypes` untuk validasi tipe data props.
   - **Latihan Mandiri 2 (Children Props)**: Komponen `Card` berbingkai menggunakan `props.children` untuk membungkus `TaskForm`.
4. **Submodul 3: State Management & Hooks**
   - Penggunaan `useState` dan `useEffect` untuk persistensi data di `localStorage`.
   - **Latihan Mandiri 3 (Tombol Bersihkan Semua)**: Tombol "Hapus Semua Tugas" dengan dialog konfirmasi aman `window.confirm`.
5. **Submodul 4: Routing dengan React Router**
   - Rute navigasi halaman `Home` dan `About` menggunakan `BrowserRouter`, `Routes`, `Route`, dan `Link`.
   - **Latihan Mandiri 4 (Halaman 404 Not Found)**: Komponen `NotFound.jsx` menangani rute fallback wildcard `*`.
6. **Submodul 5: Pembuatan Custom Hook**
   - Custom hook `useLocalStorage.js` untuk sinkronisasi otomatis ke storage browser.
   - Custom hook `useWindowSize.js` untuk mendeteksi lebar jendela browser.
   - **Latihan Mandiri 5 (Terapkan useWindowSize)**: Badge status responsif ("Mode Layar Mobile" / "Mode Layar Desktop").
7. **Submodul 6: Global State Context API**
   - Wadah global `TaskContext.jsx` dengan hook `useTasks()` dan `TaskProvider`.
   - **Latihan Mandiri 6 (Tampilkan Statistik di About)**: Halaman `About` menampilkan total tugas dari global state.
8. **Submodul 7: Unit Testing (Vitest & RTL)**
   - Pengujian `TaskItem.test.jsx` dengan Vitest dan React Testing Library (3 test lulus 100%).

## Cara Menjalankan

```bash
# 1. Masuk ke folder modul
cd febrianyoelanggarasaputra_124140031_pertemuan3/modul

# 2. Install dependensi
npm install

# 3. Jalankan server pengembangan
npm run dev

# 4. Jalankan pengujian unit (Vitest)
npm test
```
