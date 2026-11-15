# ==============================================================================
# Berkas: latihan_truk.py
# Deskripsi: Latihan Mandiri 3 - Armada Truk Ekspedisi Kargo (Inheritance & Overriding)
# Praktikan: Febrian Yoel Anggara Saputra (124140031) - Kelas RB
# Praktikum Pengembangan Aplikasi Web - Pertemuan 5
# ==============================================================================

class Kendaraan:
    """Superclass Kendaraan yang mendefinisikan atribut dasar transportasi darat."""

    def __init__(self, merek: str, model: str, tahun: int):
        self.merek = merek
        self.model = model
        self.tahun = tahun
        self.odometer = 0.0

    def deskripsi(self) -> str:
        """Mengembalikan deskripsi dasar identitas kendaraan."""
        return f"{self.merek} {self.model} ({self.tahun})"

    def tambah_jarak(self, km: float) -> None:
        """Menambah catatan jarak tempuh odometer."""
        if km > 0:
            self.odometer += km
            print(f"[{self.merek}] Menempuh perjalanan +{km} km. Total Odo: {self.odometer} km")
        else:
            print("Nilai kilometer tambahan tidak valid!")

    def klakson(self) -> str:
        """Klakson standar kendaraan."""
        return "Tin tin!"


class Truk(Kendaraan):
    """Subclass Truk yang mewarisi Kendaraan dengan spesialisasi kapasitas muatan logistik."""

    def __init__(self, merek: str, model: str, tahun: int, kapasitas_maksimal_ton: float):
        # Memanggil konstruktor superclass Kendaraan
        super().__init__(merek, model, tahun)
        self.kapasitas_maksimal_ton = float(kapasitas_maksimal_ton)
        self.muatan_saat_ini = 0.0  # Muatan awal kosong (0 ton)

    def muat_barang(self, berat_ton: float) -> bool:
        """Memuat barang dengan validasi ketat agar tidak melampaui kapasitas maksimal.

        Args:
            berat_ton (float): Berat kargo yang ingin ditambahkan (dalam ton).

        Returns:
            bool: True jika berhasil dimuat, False jika muatan berlebih/invalid.
        """
        if berat_ton <= 0:
            print(f"[{self.merek} {self.model}] Gagal muat: Berat barang harus > 0 ton!")
            return False

        if self.muatan_saat_ini + berat_ton > self.kapasitas_maksimal_ton:
            sisa_ruang = self.kapasitas_maksimal_ton - self.muatan_saat_ini
            print(
                f"[{self.merek} {self.model}] OVERLOAD! Gagal menambah {berat_ton} ton. "
                f"Kapasitas tersisa hanya {sisa_ruang:.2f} ton dari total {self.kapasitas_maksimal_ton} ton."
            )
            return False

        self.muatan_saat_ini += berat_ton
        print(
            f"[{self.merek} {self.model}] Berhasil memuat kargo +{berat_ton} ton. "
            f"Total muatan sekarang: {self.muatan_saat_ini:.2f} / {self.kapasitas_maksimal_ton} ton."
        )
        return True

    def bongkar_barang(self, berat_ton: float) -> bool:
        """Membongkar kargo muatan dari truk."""
        if berat_ton <= 0:
            print("Berat bongkar harus > 0 ton!")
            return False
        if berat_ton > self.muatan_saat_ini:
            print(f"Gagal: Berat bongkar ({berat_ton} ton) melebihi muatan ada ({self.muatan_saat_ini} ton)!")
            return False

        self.muatan_saat_ini -= berat_ton
        print(f"[{self.merek} {self.model}] Membongkar {berat_ton} ton. Sisa muatan: {self.muatan_saat_ini:.2f} ton.")
        return True

    # METHOD OVERRIDING: Memperluas deskripsi kendaraan dengan status muatan saat ini
    def deskripsi(self) -> str:
        deskripsi_dasar = super().deskripsi()
        persentase_terpakai = (self.muatan_saat_ini / self.kapasitas_maksimal_ton) * 100
        return (
            f"{deskripsi_dasar} [Truk Ekspedisi | Kapasitas: {self.kapasitas_maksimal_ton} Ton | "
            f"Muatan Saat Ini: {self.muatan_saat_ini:.2f} Ton ({persentase_terpakai:.1f}%)]"
        )

    # OVERRIDING KLAKSON
    def klakson(self) -> str:
        return "HONK! HONK! (Klakson Udara Truk Tronton)"


# --- DEMONSTRASI EKSEKUSI ---
if __name__ == "__main__":
    print("====================================================================")
    print("LATIHAN MANDIRI 3: ARMADA TRUK EKSPEDISI KARGO (INHERITANCE)")
    print("Praktikan: Febrian Yoel Anggara Saputra (124140031) - Kelas RB")
    print("====================================================================")

    # 1. Instansiasi Armada Truk
    truk_fuso = Truk("Mitsubishi", "Fuso Fighter FN62", 2023, kapasitas_maksimal_ton=15.0)
    truk_hino = Truk("Hino", "Ranger FM 260 JD", 2024, kapasitas_maksimal_ton=20.0)

    # 2. Cetak deskripsi awal (muatan 0 ton)
    print("\n--- Status Awal Armada Truk ---")
    print(truk_fuso.deskripsi())
    print(truk_hino.deskripsi())

    # 3. Uji Coba Suara Klakson Truk (Overriding)
    print("\n--- Uji Suara Klakson Truk ---")
    print(f"{truk_fuso.model} : {truk_fuso.klakson()}")

    # 4. Simulasi Muat Barang Bertahap pada Truk Fuso
    print("\n--- Proses Muat Kargo Truk Fuso (Kapasitas: 15 Ton) ---")
    truk_fuso.muat_barang(6.5)   # Sukses
    truk_fuso.muat_barang(5.0)   # Sukses -> Total 11.5 ton
    truk_fuso.muat_barang(5.5)   # GAGAL (11.5 + 5.5 = 17.0 > 15.0 ton)
    truk_fuso.muat_barang(3.0)   # Sukses -> Total 14.5 ton

    # 5. Operasional Perjalanan Truk
    print("\n--- Perjalanan Pengantaran Logistik ---")
    truk_fuso.tambah_jarak(320.0)

    # 6. Deskripsi Terkini Pasca Operasional
    print("\n--- Status Terkini Armada Truk ---")
    print(truk_fuso.deskripsi())

    # 7. Bongkar Muatan di Tujuan
    print("\n--- Pembongkaran Kargo di Gudang Tujuan ---")
    truk_fuso.bongkar_barang(10.0)
    print(truk_fuso.deskripsi())

