# ==============================================================================
# Berkas: latihan_entitas_toko.py
# Deskripsi: Latihan Mandiri 1 - Pemodelan Entitas Nyata Sistem Kasir Toko Online
# Praktikan: Febrian Yoel Anggara Saputra (124140031) - Kelas RB
# Praktikum Pengembangan Aplikasi Web - Pertemuan 5
# ==============================================================================

"""
PEMODELAN ENTITAS SISTEM KASIR TOKO ONLINE:

1. Entitas: Produk
   - Atribut Data:
     1. kode_produk (str) : Identifikasi unik setiap barang dagangan
     2. nama_produk (str) : Nama deskriptif barang
     3. harga (float)     : Harga satuan produk dalam mata uang Rupiah
     4. stok (int)        : Jumlah ketersediaan unit barang di gudang
   - Metode Perilaku:
     1. kurangi_stok(jumlah: int) -> bool : Mengurangi stok saat terjadi pembelian
     2. tambah_stok(jumlah: int) -> None  : Menambah pasokan stok produk
     3. hitung_subtotal(jumlah: int) -> float : Menghitung total harga beli

2. Entitas: Keranjang
   - Atribut Data:
     1. id_keranjang (str) : ID unik sesi belanja keranjang
     2. pemilik (str)      : Nama pemilik keranjang
     3. daftar_item (dict) : Kamus produk yang disimpan beserta jumlah belinya
   - Metode Perilaku:
     1. tambah_produk(produk: Produk, jumlah: int) -> bool : Memasukkan item belanja
     2. hapus_produk(kode_produk: str) -> bool             : Menghapus item belanja
     3. hitung_total() -> float                            : Menghitung total transaksi
     4. tampilkan_rincian() -> None                        : Mencetak struk isi keranjang

3. Entitas: Pengguna
   - Atribut Data:
     1. id_user (str)       : ID identitas unik pengguna / pembeli
     2. nama (str)          : Nama lengkap pengguna
     3. email (str)         : Alamat surel kontak akun pengguna
     4. saldo_dompet (float): Saldo e-money yang dimiliki untuk pembayaran
   - Metode Perilaku:
     1. topup_saldo(nominal: float) -> None                : Menambah deposit saldo dompet
     2. bayar_transaksi(total: float) -> bool              : Memvalidasi & memotong saldo
     3. checkout(keranjang: Keranjang) -> bool             : Melakukan finalisasi belanja
"""


class Produk:
    """Representasi komoditas produk dagangan pada toko online."""

    def __init__(self, kode_produk: str, nama_produk: str, harga: float, stok: int):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.harga = max(0.0, float(harga))
        self.stok = max(0, int(stok))

    def kurangi_stok(self, jumlah: int) -> bool:
        """Mengurangi stok barang jika stok mencukupi."""
        if 0 < jumlah <= self.stok:
            self.stok -= jumlah
            return True
        return False

    def tambah_stok(self, jumlah: int) -> None:
        """Menambahkan pasokan unit stok barang."""
        if jumlah > 0:
            self.stok += jumlah

    def hitung_subtotal(self, jumlah: int) -> float:
        """Menghitung total harga untuk sejumlah unit tertentu."""
        return self.harga * jumlah

    def __str__(self) -> str:
        return f"[{self.kode_produk}] {self.nama_produk} - Rp {self.harga:,.2f} (Stok: {self.stok})"


class Keranjang:
    """Representasi penampung daftar item belanja pembeli."""

    def __init__(self, id_keranjang: str, pemilik: str):
        self.id_keranjang = id_keranjang
        self.pemilik = pemilik
        # Menyimpan pasangan: {Produk: jumlah_beli}
        self.daftar_item = {}

    def tambah_produk(self, produk: Produk, jumlah: int = 1) -> bool:
        """Memasukkan produk ke dalam keranjang dengan validasi stok."""
        if jumlah <= 0:
            print(f"Gagal: Jumlah pembelian untuk {produk.nama_produk} harus > 0.")
            return False

        if produk.stok < jumlah:
            print(f"Gagal: Stok {produk.nama_produk} tersisa {produk.stok}, tidak cukup untuk pesanan {jumlah}.")
            return False

        if produk in self.daftar_item:
            self.daftar_item[produk] += jumlah
        else:
            self.daftar_item[produk] = jumlah

        print(f"Sukses menambahkan {jumlah}x '{produk.nama_produk}' ke keranjang {self.pemilik}.")
        return True

    def hapus_produk(self, kode_produk: str) -> bool:
        """Menghapus produk dari keranjang berdasarkan kode produk."""
        for produk in list(self.daftar_item.keys()):
            if produk.kode_produk == kode_produk:
                del self.daftar_item[produk]
                print(f"Produk '{produk.nama_produk}' dihapus dari keranjang.")
                return True
        print(f"Produk dengan kode '{kode_produk}' tidak ditemukan di keranjang.")
        return False

    def hitung_total(self) -> float:
        """Menghitung total biaya belanja seluruh item di keranjang."""
        total = 0.0
        for produk, qty in self.daftar_item.items():
            total += produk.hitung_subtotal(qty)
        return total

    def tampilkan_rincian(self) -> None:
        """Mencetak rincian seluruh item belanja di dalam keranjang."""
        print(f"\n--- Rincian Keranjang [{self.id_keranjang}] Pemilik: {self.pemilik} ---")
        if not self.daftar_item:
            print("Keranjang masih kosong.")
            return

        for idx, (produk, qty) in enumerate(self.daftar_item.items(), 1):
            subtotal = produk.hitung_subtotal(qty)
            print(f"{idx}. {produk.nama_produk:<25} x{qty:<2} @Rp {produk.harga:,.2f} = Rp {subtotal:,.2f}")
        print("-" * 52)
        print(f"Total Belanja: Rp {self.hitung_total():,.2f}")


class Pengguna:
    """Representasi akun pembeli dalam ekosistem sistem toko."""

    def __init__(self, id_user: str, nama: str, email: str, saldo_awal: float = 0.0):
        self.id_user = id_user
        self.nama = nama
        self.email = email
        self.saldo_dompet = max(0.0, float(saldo_awal))

    def topup_saldo(self, nominal: float) -> None:
        """Menambahkan saldo dana ke dompet digital pengguna."""
        if nominal > 0:
            self.saldo_dompet += nominal
            print(f"[Top-Up] Berhasil menambah Rp {nominal:,.2f}. Saldo saat ini: Rp {self.saldo_dompet:,.2f}")
        else:
            print("Nominal top-up tidak valid!")

    def bayar_transaksi(self, total: float) -> bool:
        """Memotong saldo pengguna jika mencukupi untuk tagihan."""
        if total <= 0:
            return True
        if self.saldo_dompet >= total:
            self.saldo_dompet -= total
            return True
        return False

    def checkout(self, keranjang: Keranjang) -> bool:
        """Melakukan finalisasi pesanan, validasi pembayaran, dan pemotongan stok."""
        total = keranjang.hitung_total()
        print(f"\n[Checkout] Pengguna {self.nama} memproses keranjang [{keranjang.id_keranjang}]...")
        print(f"Total Tagihan: Rp {total:,.2f} | Saldo Tersedia: Rp {self.saldo_dompet:,.2f}")

        if not keranjang.daftar_item:
            print("Gagal: Keranjang belanja kosong!")
            return False

        if not self.bayar_transaksi(total):
            print("Gagal Checkout: Saldo dompet tidak mencukupi untuk melunasi tagihan!")
            return False

        # Pengurangan stok produk secara nyata
        for produk, qty in keranjang.daftar_item.items():
            produk.kurangi_stok(qty)

        keranjang.daftar_item.clear()
        print(f"Checkout BERHASIL! Saldo tersisa: Rp {self.saldo_dompet:,.2f}")
        return True


# --- DEMONSTRASI EKSEKUSI ---
if __name__ == "__main__":
    print("====================================================================")
    print("LATIHAN MANDIRI 1: PEMODELAN ENTITAS SISTEM KASIR TOKO ONLINE")
    print("Praktikan: Febrian Yoel Anggara Saputra (124140031) - Kelas RB")
    print("====================================================================")

    # 1. Inisialisasi Produk
    p1 = Produk("PRD-001", "Keyboard Mekanikal TKL", 450000, stok=10)
    p2 = Produk("PRD-002", "Mouse Wireless Silent", 185000, stok=15)
    p3 = Produk("PRD-003", "Mousepad Deskmat XL", 95000, stok=5)

    print("\n--- Katalog Produk Toko ---")
    print(p1)
    print(p2)
    print(p3)

    # 2. Inisialisasi Pengguna & Keranjang
    pembeli = Pengguna("USR-101", "Febrian Yoel", "yoel@if.itera.ac.id", saldo_awal=500000)
    cart = Keranjang("CRT-2026", pembeli.nama)

    # 3. Menambahkan produk ke keranjang
    cart.tambah_produk(p1, 1)
    cart.tambah_produk(p2, 1)
    cart.tambah_produk(p3, 1)
    cart.tampilkan_rincian()

    # 4. Uji Checkout pertama (saldo kurang)
    pembeli.checkout(cart)

    # 5. Topup saldo dan checkout ulang
    pembeli.topup_saldo(300000)
    pembeli.checkout(cart)

    # 6. Verifikasi sisa stok produk setelah checkout
    print("\n--- Sisa Stok Produk Pasca Checkout ---")
    print(p1)
    print(p2)
    print(p3)
