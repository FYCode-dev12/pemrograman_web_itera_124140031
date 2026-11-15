# ==============================================================================
# Berkas: latihan_karyawan.py
# Deskripsi: Latihan Mandiri 4 - Enkapsulasi Penggajian Karyawan & @property
# Praktikan: Febrian Yoel Anggara Saputra (124140031) - Kelas RB
# Praktikum Pengembangan Aplikasi Web - Pertemuan 5
# ==============================================================================

class Karyawan:
    """Class Karyawan yang menerapkan prinsip enkapsulasi data gaji sesuai standar UMR."""

    # Konstanta batas Upah Minimum Regional (UMR)
    UMR_MINIMAL = 3200000.0

    def __init__(self, nama: str, jabatan: str, gaji_pokok_awal: float):
        # 1. Atribut Publik: Nama dan Jabatan dapat dibaca & diakses secara bebas
        self.nama = nama
        self.jabatan = jabatan

        # 2. Atribut Private: Gaji pokok dilindungi name mangling
        # Inisialisasi awal melalui setter untuk menjamin validasi aturan UMR
        self.__gaji_pokok = self.UMR_MINIMAL
        self.gaji_pokok = gaji_pokok_awal  # Menggunakan setter

    # --------------------------------------------------------------------------
    # PROPERTY GETTER
    # --------------------------------------------------------------------------
    @property
    def gaji_pokok(self) -> float:
        """Mengembalikan nilai gaji pokok karyawan secara aman (read-access)."""
        return self.__gaji_pokok

    # --------------------------------------------------------------------------
    # PROPERTY SETTER (Validasi Ketat Regulasi UMR)
    # --------------------------------------------------------------------------
    @gaji_pokok.setter
    def gaji_pokok(self, nominal_baru: float):
        """Mengatur gaji pokok dengan validasi tidak boleh di bawah UMR (Rp 3.200.000)."""
        if not isinstance(nominal_baru, (int, float)):
            raise TypeError("Gaji pokok harus bertipe angka numerik!")

        nominal_float = float(nominal_baru)
        if nominal_float < self.UMR_MINIMAL:
            raise ValueError(
                f"Gagal Menetapkan Gaji: Rp {nominal_float:,.2f} berada di bawah batas "
                f"UMR Minimum (Rp {self.UMR_MINIMAL:,.2f})!"
            )

        self.__gaji_pokok = nominal_float
        print(f"[HR INFO] Gaji pokok {self.nama} ({self.jabatan}) disetujui: Rp {self.__gaji_pokok:,.2f}")

    # --------------------------------------------------------------------------
    # METODE BISNIS PENGGAJIAN
    # --------------------------------------------------------------------------
    def hitung_gaji_bersih(self, pajak_persen: float = 5.0) -> float:
        """Menghitung total gaji take-home-pay setelah dipotong persentase pajak penghasilan.

        Args:
            pajak_persen (float): Persentase potongan pajak PPh (contoh: 5.0 untuk 5%).

        Returns:
            float: Gaji bersih yang diterima karyawan.
        """
        if not (0.0 <= pajak_persen <= 100.0):
            print(f"Peringatan: Persen pajak {pajak_persen}% tidak wajar!")
            return self.__gaji_pokok

        potongan_pajak = self.__gaji_pokok * (pajak_persen / 100.0)
        gaji_bersih = self.__gaji_pokok - potongan_pajak
        return gaji_bersih

    def cetak_slip_gaji(self, pajak_persen: float = 5.0) -> None:
        """Mencetak slip gaji resmi karyawan."""
        potongan = self.__gaji_pokok * (pajak_persen / 100.0)
        gaji_bersih = self.hitung_gaji_bersih(pajak_persen)

        print("\n" + "=" * 54)
        print(f"             SLIP GAJI BULANAN KARYAWAN")
        print("=" * 54)
        print(f" Nama Karyawan   : {self.nama}")
        print(f" Jabatan         : {self.jabatan}")
        print(f" Standar UMR     : Rp {self.UMR_MINIMAL:,.2f}")
        print("-" * 54)
        print(f" Gaji Pokok      : Rp {self.gaji_pokok:>14,.2f}")
        print(f" Potongan PPh({pajak_persen}%) : Rp {potongan:>14,.2f}")
        print("-" * 54)
        print(f" GAJI BERSIH (THP): Rp {gaji_bersih:>14,.2f}")
        print("=" * 54)


# --- DEMONSTRASI EKSEKUSI ---
if __name__ == "__main__":
    print("====================================================================")
    print("LATIHAN MANDIRI 4: ENKAPSULASI PENGGAJIAN KARYAWAN & @PROPERTY")
    print("Praktikan: Febrian Yoel Anggara Saputra (124140031) - Kelas RB")
    print("====================================================================")

    # 1. Instansiasi objek Karyawan dengan gaji valid di atas UMR
    karyawan1 = Karyawan("Febrian Yoel", "Senior Software Engineer", 12500000)
    karyawan2 = Karyawan("Andi Pratama", "Junior Web Developer", 4500000)

    # 2. Akses atribut publik dan property getter
    print("\n--- Akses Atribut Publik & Property Getter ---")
    print(f"Nama Karyawan 1 : {karyawan1.nama} (Public)")
    print(f"Jabatan         : {karyawan1.jabatan} (Public)")
    print(f"Gaji Pokok      : Rp {karyawan1.gaji_pokok:,.2f} (via @property getter)")

    # 3. Cetak Slip Gaji dengan pemotongan pajak
    karyawan1.cetak_slip_gaji(pajak_persen=5.0)
    karyawan2.cetak_slip_gaji(pajak_persen=5.0)

    # 4. Pengujian Setter: Kenaikan Gaji (Valid)
    print("\n--- Uji Setter: Kenaikan Gaji Karyawan 2 ---")
    karyawan2.gaji_pokok = 5500000
    print(f"Gaji pokok baru Andi: Rp {karyawan2.gaji_pokok:,.2f}")

    # 5. Pengujian Validasi Setter: Mencoba mengatur gaji di bawah UMR (< Rp 3.200.000)
    print("\n--- Uji Validasi Setter: Penolakan Gaji di Bawah UMR ---")
    try:
        # Percobaan menetapkan gaji di bawah UMR
        karyawan2.gaji_pokok = 2500000
    except ValueError as err:
        print(f"Pencegahan Berhasil! Exception Tertangkap:\n -> {err}")

    # 6. Pembuktian Name Mangling: Mencoba akses langsung ke __gaji_pokok
    print("\n--- Uji Proteksi Enkapsulasi Private Attribute ---")
    try:
        # Akses langsung atribut private harus memicu AttributeError
        print(karyawan1.__gaji_pokok)
    except AttributeError:
        print("Akses langsung 'karyawan1.__gaji_pokok' DITOLAK (AttributeError terbukti)!")

    # Mengakses lewat name mangling Python internal (_Karyawan__gaji_pokok)
    print(f"Akses via Name Mangling (_Karyawan__gaji_pokok): Rp {karyawan1._Karyawan__gaji_pokok:,.2f}")

