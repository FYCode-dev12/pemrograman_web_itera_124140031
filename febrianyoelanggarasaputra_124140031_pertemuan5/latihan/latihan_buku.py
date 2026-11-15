# ==============================================================================
# Berkas: latihan_buku.py
# Deskripsi: Latihan Mandiri 2 - Class Buku dengan Diskon & Dunder Length
# Praktikan: Febrian Yoel Anggara Saputra (124140031) - Kelas RB
# Praktikum Pengembangan Aplikasi Web - Pertemuan 5
# ==============================================================================

class Buku:
    """Class Buku yang merepresentasikan karya literatur dengan fitur diskon dan dunder len."""

    def __init__(self, judul: str, penulis: str, harga_asli: float, jumlah_halaman: int):
        self.judul = judul
        self.penulis = penulis
        self.harga_asli = max(0.0, float(harga_asli))
        self.jumlah_halaman = max(0, int(jumlah_halaman))

    def hitung_harga_diskon(self, persen: float) -> float:
        """Menghitung harga buku setelah dipotong diskon persentase.

        Args:
            persen (float): Nilai diskon dalam persen (0 - 100).

        Returns:
            float: Harga akhir setelah diskon.
        """
        if not (0.0 <= persen <= 100.0):
            print(f"Peringatan: Persen diskon {persen}% tidak valid (harus 0 - 100).")
            return self.harga_asli
        potongan = self.harga_asli * (persen / 100.0)
        return self.harga_asli - potongan

    def __str__(self) -> str:
        """Representasi kartu buku yang rapi dan mudah dibaca."""
        return (
            f"+----------------------------------------------------------+\n"
            f"| JUDUL  : {self.judul:<47} |\n"
            f"| PENULIS: {self.penulis:<47} |\n"
            f"| HALAMAN: {self.jumlah_halaman:<4} hlm                                      |\n"
            f"| HARGA  : Rp {self.harga_asli:>10,.2f}                               |\n"
            f"+----------------------------------------------------------+"
        )

    def __len__(self) -> int:
        """Dunder method untuk mengembalikan jumlah halaman saat len(buku) dipanggil."""
        return self.jumlah_halaman


# --- DEMONSTRASI EKSEKUSI ---
if __name__ == "__main__":
    print("====================================================================")
    print("LATIHAN MANDIRI 2: CLASS BUKU DENGAN DISKON & DUNDER LENGTH")
    print("Praktikan: Febrian Yoel Anggara Saputra (124140031) - Kelas RB")
    print("====================================================================")

    # 1. Instansiasi objek buku
    buku1 = Buku(
        judul="Pemrograman Python untuk Rekayasa Web Modern",
        penulis="Guido van Rossum",
        harga_asli=145000,
        jumlah_halaman=480
    )

    buku2 = Buku(
        judul="Struktur Data dan Algoritma Lanjut",
        penulis="Donald E. Knuth",
        harga_asli=210000,
        jumlah_halaman=650
    )

    # 2. Mencetak representasi string via __str__
    print("\n--- Kartu Informasi Buku 1 (via __str__) ---")
    print(buku1)

    print("\n--- Kartu Informasi Buku 2 (via __str__) ---")
    print(buku2)

    # 3. Uji Dunder Method __len__ via pemanggilan fungsi built-in len()
    print("\n--- Uji Dunder Method len(buku) ---")
    print(f"Tebal buku '{buku1.judul}' adalah: {len(buku1)} halaman")
    print(f"Tebal buku '{buku2.judul}' adalah: {len(buku2)} halaman")

    # 4. Uji Perhitungan Diskon
    diskon_persen = 25.0
    harga_akhir1 = buku1.hitung_harga_diskon(diskon_persen)
    harga_akhir2 = buku2.hitung_harga_diskon(diskon_persen)

    print(f"\n--- Simulasi Promo Diskon {diskon_persen}% ---")
    print(f"Buku 1 : Rp {buku1.harga_asli:,.2f} -> Diskon {diskon_persen}% = Rp {harga_akhir1:,.2f}")
    print(f"Buku 2 : Rp {buku2.harga_asli:,.2f} -> Diskon {diskon_persen}% = Rp {harga_akhir2:,.2f}")

