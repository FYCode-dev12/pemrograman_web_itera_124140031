# ===================================================
# Berkas: latihan1.py
# Deskripsi: Kartu identitas praktikan memakai print(), sep, dan escape
# ===================================================

LEBAR = 52

print("#" * LEBAR)
print("#" + "KARTU IDENTITAS PRAKTIKAN".center(LEBAR - 2) + "#")
print("#" * LEBAR)

# Beberapa argumen dengan separator pipa
print("Nama", "Febrian Yoel Anggara Saputra", sep=" | ")
print("NIM", "124140031", sep=" | ")
print("Angkatan", "2024", sep=" | ")
print("Minat Penelitian", "Jaringan Komputer & Web", sep=" | ")

print("-" * LEBAR)
# Escape character: \t untuk tab, \n untuk baris baru
print(
    "Ringkasan:\n"
    "\tPraktikan aktif Program Studi Teknik Informatika\n"
    "\tITERA, T.A. 2026/2027 Ganjil"
)
print("#" * LEBAR)

# Eksperimen tambahan: kartu dua kolom yang sejajar
print("\nEksperimen format sejajar:")
print(f"{'Nama':<18}: {'Febrian Yoel Anggara Saputra'}")
print(f"{'Kelas':<18}: RB")
print(f"{'Bahasa Favorit':<18}: Python")
