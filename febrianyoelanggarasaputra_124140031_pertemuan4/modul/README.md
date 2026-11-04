# Modul Praktikum Pertemuan 4 — Python Dasar

Folder ini memuat skrip demonstrasi modul dan latihan mandiri. Semua berkas
dijalankan dari **folder ini** agar modul lokal (`kalkulator_lib`, `password_gen`)
dapat diimpor.

| Berkas | Keterangan |
| :--- | :--- |
| `01_pengenalan.py` | `print()`, `sep`, `end`, escape character |
| `02_variabel.py` | Tipe data, f-string, slicing, casting, `input()` |
| `03_kendali.py` | Percabangan, ternary, `for`, `while`, `break`/`continue` |
| `04_fungsi.py` | Fungsi, default parameter, `*args`, `**kwargs`, lambda |
| `05_struktur_data.py` | List, tuple, dictionary, set |
| `06_modul_app.py` | Standard library + modul kustom `kalkulator_lib` |
| `kalkulator_lib.py` | Modul aritmatika dengan blok `__main__` |
| `latihan1.py` | Kartu identitas praktikan |
| `latihan2_suhu.py` | Konversi Celsius → Fahrenheit & Kelvin |
| `latihan3_tebak.py` | Game tebak angka 1–20 |
| `latihan4_validasi.py` | Validator password (min. 8 karakter + angka) |
| `latihan5_kontak.py` | Katalog kontak berbasis dictionary |
| `password_gen.py` | Modul generator password acak |
| `main.py` | Program penguji `password_gen` |

## Menjalankan

```bash
cd modul
python 01_pengenalan.py
python 06_modul_app.py
python main.py
```

> `02_variabel.py`, `latihan2_suhu.py`, `latihan3_tebak.py`,
> `latihan4_validasi.py`, dan `latihan5_kontak.py` bersifat interaktif dan
> menunggu masukan dari keyboard.

Screenshot hasil eksekusi tersedia di folder `../docs/`.
