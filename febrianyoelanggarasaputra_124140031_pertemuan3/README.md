# Aplikasi Manajemen Buku Pribadi (PustakaKu)

**Praktikum Pengembangan Aplikasi Web (PAW)**  
**Pertemuan 3: React Basics**  
**Teknik Informatika - Institut Teknologi Sumatera (ITERA)**

---

### Identitas Praktikan
- **Nama**: Febrian Yoel Anggara Saputra
- **NIM**: 124140031
- **Kelas Praktikum**: RB
- **Tahun Ajaran**: 2026/2027 Ganjil

---

## 1. Deskripsi Aplikasi

**PustakaKu** adalah aplikasi web berbasis React yang dirancang untuk membantu pengguna mengelola, mendokumentasikan, dan memantau koleksi buku pribadi secara terstruktur dan efisien.

Aplikasi ini mencakup:
1. **Pencatatan Buku**: Menambah buku baru beserta data judul, penulis, status, tahun rilis, kategori, dan catatan refleksi bacaan.
2. **Kategorisasi Status**: Mengelompokkan buku ke dalam 3 status utama:
   - **Dimiliki (Milik)**: Buku fisik/digital yang sudah dimiliki.
   - **Sedang Dibaca (Baca)**: Buku yang sedang aktif dibaca.
   - **Rencana Beli (Beli)**: Wishlist buku yang ingin dibeli.
3. **Filter & Pencarian Real-Time**: Pencarian cepat tanpa jeda berdasarkan judul, nama penulis, maupun kategori dengan dukungan tab filter status.
4. **Manajemen Koleksi (CRUD)**: Mengubah status buku, mengedit detail buku melalui dialog modal, serta menghapus buku dengan konfirmasi aman.
5. **Dashboard Statistik**: Visualisasi statistik koleksi dalam bentuk progress bar proporsional dan tabel buku terbaru.
6. **Persistensi Data**: Penyimpanan data otomatis di browser menggunakan `localStorage`.

---

## 2. Panduan Instalasi & Menjalankan Proyek

Pastikan di komputer Anda telah terpasang **Node.js** (versi 18.x atau lebih baru) dan **npm**.

### Langkah-langkah:

```bash
# 1. Buka terminal dan arahkan ke direktori proyek tugas:
cd febrianyoelanggarasaputra_124140031_pertemuan3

# 2. Pasang seluruh dependensi yang dibutuhkan:
npm install

# 3. Jalankan server pengembang lokal (Vite):
npm run dev

# 4. Buka browser pada alamat yang ditampilkan:
# http://localhost:5173 (atau port yang diberikan Vite)

# 5. Jalankan unit test otomatis (Vitest):
npm test
```

---

## 3. Fitur React yang Diterapkan

Sesuai dengan seluruh persyaratan silabus Praktikum Pertemuan 3:

| Fitur / Konsep | Implementasi dalam Proyek |
| :--- | :--- |
| **Functional Components & Hooks** | Menggunakan functional component di seluruh aplikasi dengan `useState` dan `useEffect`. |
| **Minimal 3 Komponen Reusable** | Dibuat lebih dari 6 komponen reusable: `BookForm`, `BookItem`, `BookList`, `BookFilter`, `Card`, `Modal`, dan `Navbar`. |
| **Global State (Context API)** | `BookContext.jsx` (`BookProvider` dan custom consumer hook `useBooks()`) mengelola data buku dan filtering tanpa prop-drilling. |
| **Multi-page Navigation (React Router)** | Navigasi halaman Beranda (`/`), Statistik (`/stats`), Tentang (`/about`), dan Fallback Not Found (`*`) menggunakan `react-router-dom`. |
| **Persistensi Data** | `localStorage` tersinkronisasi otomatis setiap kali ada mutasi state buku. |
| **Minimal 2 Custom Hooks** | 1. `useLocalStorage.js` (abstraksi sinkronisasi storage browser aman).<br>2. `useBookStats.js` (kalkulasi memoized metrik total, milik, baca, beli, dan persentase). |
| **Type Checking (PropTypes)** | Seluruh komponen reusable divalidasi ketat menggunakan pustaka `prop-types`. |
| **Error Handling & Validasi Form** | Validasi kolom wajib (judul & penulis tidak boleh kosong/spasi), visual border merah, pesan peringatan informatif, dan validasi tahun. |
| **Unit Testing (Vitest & RTL)** | 8 skenario pengujian komprehensif menguji rendering, penambahan buku, validasi error, filter status, pencarian, dan aksi tombol. |

---

## 4. Struktur Folder Proyek

```
febrianyoelanggarasaputra_124140031_pertemuan3/
├── index.html                     # File entry point HTML
├── package.json                   # Konfigurasi dependensi dan scripts
├── vite.config.js                 # Konfigurasi Vite & Vitest test runner
├── README.md                      # Dokumentasi komprehensif tugas
├── modul/                         # Folder Latihan Modul Praktikum 3 (Submodul 0 - 7)
│   ├── cdn-react.html             # Demo instan metode HTML + CDN
│   ├── package.json               # Paket latihan modul
│   └── src/                       # Komponen latihan modul & latihan mandiri
└── src/
    ├── main.jsx                   # Entry point React DOM
    ├── App.jsx                    # Routing & Root App
    ├── App.css                    # Layout styling
    ├── index.css                  # Global design tokens & reset
    ├── setupTests.js              # Setup Jest-DOM matcher untuk Vitest
    ├── context/
    │   └── BookContext.jsx        # Context API & Provider data buku
    ├── hooks/
    │   ├── useLocalStorage.js     # Custom hook penyimpanan lokal
    │   └── useBookStats.js        # Custom hook kalkulasi statistik
    ├── components/
    │   ├── BookForm/              # Form tambah & edit dengan validasi
    │   ├── BookItem/              # Card item buku dengan tombol aksi
    │   ├── BookList/              # Container daftar buku & empty state
    │   ├── BookFilter/            # Filter tab status & bar pencarian
    │   ├── Card/                  # Komponen container wadah berbingkai
    │   ├── Modal/                 # Dialog modal backdrop interaktif
    │   └── Navbar/                # Navigation bar responsif
    └── pages/
        ├── Home/                  # Halaman utama manajemen buku
        ├── Stats/                 # Halaman visualisasi statistik
        ├── About/                 # Halaman identitas & dokumentasi
        └── NotFound/              # Halaman error 404 penangkap fallback
```

---

## 5. Hasil Pengujian Unit Test

Pengujian dilakukan menggunakan **Vitest** dan **React Testing Library**. Semua skenario lulus (PASS):

```
✓ src/components/BookItem/BookItem.test.jsx (4 tests)
  ✓ Komponen BookItem > Test 1: Merender informasi judul, penulis, dan status buku dengan benar
  ✓ Komponen BookItem > Test 2: Memanggil handler onDelete ketika tombol Hapus diklik
  ✓ Komponen BookItem > Test 3: Memanggil handler onEdit ketika tombol Edit diklik
  ✓ Komponen BookItem > Test 4: Memanggil onStatusChange saat memilih opsi status baru dari dropdown

✓ src/components/BookForm/BookForm.test.jsx (2 tests)
  ✓ Komponen BookForm (Validasi & Error Handling) > Test 5: Menampilkan pesan error validasi ketika field wajib (judul & penulis) kosong
  ✓ Komponen BookForm (Validasi & Error Handling) > Test 6: Berhasil submit data ketika form diisi dengan valid

✓ src/components/BookFilter/BookFilter.test.jsx (2 tests)
  ✓ Komponen BookFilter > Test 7: Memanggil onFilterChange saat tab status diklik
  ✓ Komponen BookFilter > Test 8: Memanggil onSearchChange saat mengetik di input pencarian

Test Files  3 passed (3)
     Tests  8 passed (8)
```
