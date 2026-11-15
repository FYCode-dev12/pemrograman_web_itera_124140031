# ==============================================================================
# Berkas: library.py
# Deskripsi: Class Library - Pengelolaan Koleksi, Member, Transaksi & Polimorfisme
# Praktikan: Febrian Yoel Anggara Saputra (124140031) - Kelas RB
# Praktikum Pengembangan Aplikasi Web - Pertemuan 5
# ==============================================================================

from typing import Dict, List, Optional, Tuple
from datetime import datetime
from library_item import LibraryItem
from member import Member


class Library:
    """Class Library yang mengelola katalog item, keanggotaan, serta transaksi peminjaman.

    Menerapkan 4 pilar OOP:
    - Encapsulation: Koleksi item dan data member diisolasi dalam atribut private (__koleksi, __daftar_member).
    - Abstraction: Berinteraksi dengan LibraryItem melalui antarmuka abstrak tanpa memedulikan detail internal subclass.
    - Polymorphism: Menampilkan detail item dan menghitung denda secara polimorfik lintas Book, Magazine, dan DigitalMedia.
    """

    def __init__(self, nama_perpustakaan: str):
        self.__nama_perpustakaan = str(nama_perpustakaan).strip()

        # Atribut Private: Menampung data item dalam bentuk dictionary {item_id: LibraryItem}
        self.__koleksi: Dict[str, LibraryItem] = {}

        # Atribut Private: Menampung anggota {id_member: Member}
        self.__daftar_member: Dict[str, Member] = {}

        # Atribut Private: Riwayat log transaksi perpustakaan
        self.__riwayat_transaksi: List[dict] = []

    # --------------------------------------------------------------------------
    # PROPERTY GETTERS (Enkapsulasi Data Perpustakaan)
    # --------------------------------------------------------------------------
    @property
    def nama_perpustakaan(self) -> str:
        """Mengembalikan nama resmi perpustakaan."""
        return self.__nama_perpustakaan

    @property
    def total_koleksi(self) -> int:
        """Mengembalikan total seluruh koleksi item yang terdaftar."""
        return len(self.__koleksi)

    @property
    def total_tersedia(self) -> int:
        """Mengembalikan jumlah item yang saat ini berstatus TERSEDIA (belum dipinjam)."""
        return sum(1 for item in self.__koleksi.values() if not item.is_dipinjam)

    @property
    def total_dipinjam(self) -> int:
        """Mengembalikan jumlah item yang saat ini sedang DIPINJAM."""
        return sum(1 for item in self.__koleksi.values() if item.is_dipinjam)

    @property
    def total_member(self) -> int:
        """Mengembalikan jumlah anggota terdaftar di perpustakaan."""
        return len(self.__daftar_member)

    # --------------------------------------------------------------------------
    # MANAJEMEN KOLEKSI ITEM
    # --------------------------------------------------------------------------
    def tambah_item(self, item: LibraryItem) -> bool:
        """Menambahkan objek koleksi baru (Book, Magazine, dsb) ke perpustakaan.

        Args:
            item (LibraryItem): Objek yang mewarisi class abstrak LibraryItem.

        Returns:
            bool: True jika berhasil ditambahkan, False jika ID duplikat / invalid.
        """
        # Validasi polimorfik: Memastikan objek mematuhi turunan LibraryItem
        if not isinstance(item, LibraryItem):
            raise TypeError("Objek yang ditambahkan wajib merupakan turunan dari LibraryItem!")

        if item.item_id in self.__koleksi:
            print(f"[Library] Gagal: Item dengan ID '{item.item_id}' sudah terdaftar dalam sistem!")
            return False

        self.__koleksi[item.item_id] = item
        print(f"[Library] Berhasil menambahkan [{item.tipe_item}] '{item.judul}' (ID: {item.item_id}).")
        return True

    def tampilkan_katalog(self, hanya_tersedia: bool = False) -> None:
        """Menampilkan daftar katalog perpustakaan secara rapi dan polimorfik.

        Args:
            hanya_tersedia (bool): Jika True, hanya menampilkan item yang siap dipinjam.
        """
        status_katalog = "TERSEDIA DI RAK" if hanya_tersedia else "SELURUH KOLEKSI"
        print("\n" + "=" * 90)
        print(f"       KATALOG PERPUSTAKAAN: {self.__nama_perpustakaan.upper()} ({status_katalog})")
        print("=" * 90)
        print(f"{'No.':<4} {'ID':<8} {'Tipe':<14} {'Tahun':<7} {'Status':<12} {'Judul Item':<40}")
        print("-" * 90)

        daftar = [
            item for item in self.__koleksi.values()
            if not (hanya_tersedia and item.is_dipinjam)
        ]

        if not daftar:
            print("  (Tidak ada koleksi perpustakaan yang sesuai kriteria)")
            print("-" * 90)
            return

        for idx, item in enumerate(daftar, 1):
            status = "DIPINJAM" if item.is_dipinjam else "TERSEDIA"
            judul_potong = item.judul[:38] + ".." if len(item.judul) > 38 else item.judul
            print(f"{idx:<4} {item.item_id:<8} {item.tipe_item:<14} {item.tahun_terbit:<7} {status:<12} {judul_potong:<40}")

        print("-" * 90)
        print(f"Total Item: {len(daftar)} | Tersedia: {self.total_tersedia} | Dipinjam: {self.total_dipinjam}")
        print("=" * 90)

    def cari_item_by_id(self, item_id: str) -> Optional[LibraryItem]:
        """Mencari item perpustakaan berdasarkan ID unik secara O(1)."""
        item_id_bersih = str(item_id).strip()
        return self.__koleksi.get(item_id_bersih)

    def cari_item_by_judul(self, kata_kunci: str) -> List[LibraryItem]:
        """Mencari seluruh item yang judulnya memuat kata kunci (case-insensitive)."""
        kata_bersih = str(kata_kunci).strip().lower()
        hasil = [
            item for item in self.__koleksi.values()
            if kata_bersih in item.judul.lower()
        ]
        return hasil

    # --------------------------------------------------------------------------
    # MANAJEMEN ANGGOTA (MEMBER)
    # --------------------------------------------------------------------------
    def tambah_member(self, member: Member) -> bool:
        """Mendaftarkan anggota baru ke dalam sistem perpustakaan."""
        if not isinstance(member, Member):
            raise TypeError("Objek yang didaftarkan harus berupa instance dari Member!")

        if member.id_member in self.__daftar_member:
            print(f"[Library] Gagal: Anggota dengan ID '{member.id_member}' sudah terdaftar!")
            return False

        self.__daftar_member[member.id_member] = member
        print(f"[Library] Anggota baru terdaftar: [{member.id_member}] {member.nama} ({member.tipe_member}).")
        return True

    def cari_member_by_id(self, id_member: str) -> Optional[Member]:
        """Mencari data anggota berdasarkan ID."""
        return self.__daftar_member.get(str(id_member).strip())

    def tampilkan_daftar_member(self) -> None:
        """Mencetak daftar seluruh anggota terdaftar di perpustakaan."""
        print("\n" + "=" * 76)
        print(f"             DAFTAR ANGGOTA: {self.__nama_perpustakaan.upper()}")
        print("=" * 76)
        print(f"{'No.':<4} {'ID Member':<12} {'Kategori':<12} {'Pinjaman':<12} {'Nama Anggota':<32}")
        print("-" * 76)
        for idx, m in enumerate(self.__daftar_member.values(), 1):
            status_pinjam = f"{m.jumlah_pinjaman}/{m.maks_pinjaman} item"
            print(f"{idx:<4} {m.id_member:<12} {m.tipe_member:<12} {status_pinjam:<12} {m.nama:<32}")
        print("-" * 76)
        print(f"Total Anggota Terdaftar: {self.total_member} orang")
        print("=" * 76)

    # --------------------------------------------------------------------------
    # PROSES TRANSAKSI (PEMINJAMAN & PENGEMBALIAN POLIMORFIK)
    # --------------------------------------------------------------------------
    def pinjam_item(self, item_id: str, id_member: str) -> bool:
        """Memproses transaksi peminjaman item oleh anggota terdaftar.

        Args:
            item_id (str): ID unik koleksi yang hendak dipinjam.
            id_member (str): ID anggota peminjam.

        Returns:
            bool: True jika transaksi peminjaman berhasil diproses.
        """
        print(f"\n[Transaksi Peminjaman] Memproses Item '{item_id}' untuk Member '{id_member}'...")

        # 1. Validasi Keberadaan Item
        item = self.cari_item_by_id(item_id)
        if item is None:
            print(f" -> Transaksi Gagal: Item dengan ID '{item_id}' tidak ditemukan di perpustakaan!")
            return False

        # 2. Validasi Ketersediaan Item
        if item.is_dipinjam:
            print(f" -> Transaksi Gagal: Item '{item.judul}' saat ini sedang dipinjam oleh [{item.peminjam_id}]!")
            return False

        # 3. Validasi Keberadaan Member
        member = self.cari_member_by_id(id_member)
        if member is None:
            print(f" -> Transaksi Gagal: Member dengan ID '{id_member}' tidak terdaftar!")
            return False

        # 4. Validasi Kuota Member
        if not member.bisa_pinjam():
            print(f" -> Transaksi Gagal: Member '{member.nama}' telah mencapai batas kuota pinjaman ({member.maks_pinjaman} item)!")
            return False

        # 5. Eksekusi Peminjaman
        item.tandai_dipinjam(member.id_member)
        member.tambah_pinjaman(item)

        # Catat Log Transaksi
        log_entry = {
            "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "tipe": "PINJAM",
            "item_id": item.item_id,
            "judul": item.judul,
            "id_member": member.id_member,
            "nama_member": member.nama,
            "durasi_maksimal": item.get_durasi_maksimal_pinjam()
        }
        self.__riwayat_transaksi.append(log_entry)

        print(f" -> Peminjaman SUKSES! Batas pengembalian: {item.get_durasi_maksimal_pinjam()} hari kalender.")
        return True

    def kembalikan_item(self, item_id: str, id_member: str, hari_terlambat: int = 0) -> Tuple[bool, float]:
        """Memproses transaksi pengembalian item dan perhitungan denda keterlambatan secara polimorfik.

        Args:
            item_id (str): ID koleksi yang dikembalikan.
            id_member (str): ID anggota yang mengembalikan.
            hari_terlambat (int): Jumlah hari keterlambatan (0 jika tepat waktu).

        Returns:
            Tuple[bool, float]: (Status keberhasilan, Nominal denda yang harus dibayar).
        """
        print(f"\n[Transaksi Pengembalian] Memproses Item '{item_id}' dari Member '{id_member}'...")

        # 1. Validasi Keberadaan Item & Member
        item = self.cari_item_by_id(item_id)
        if item is None:
            print(f" -> Pengembalian Gagal: Item ID '{item_id}' tidak ditemukan di perpustakaan!")
            return (False, 0.0)

        member = self.cari_member_by_id(id_member)
        if member is None:
            print(f" -> Pengembalian Gagal: Member ID '{id_member}' tidak ditemukan!")
            return (False, 0.0)

        # 2. Validasi apakah benar item dipinjam oleh member ini
        if not item.is_dipinjam or item.peminjam_id != member.id_member:
            print(f" -> Pengembalian Gagal: Item '{item.judul}' tidak tercatat sedang dipinjam oleh [{member.id_member}]!")
            return (False, 0.0)

        # 3. Proses Pengembalian pada Objek Member dan Item
        member.kembalikan_pinjaman(item.item_id)
        item.tandai_dikembalikan()

        # 4. PERHITUNGAN DENDA POLIMORFIK (Memanggil hitung_denda sesuai subclass)
        denda = item.hitung_denda(hari_terlambat)

        # Catat Log Transaksi
        log_entry = {
            "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "tipe": "KEMBALI",
            "item_id": item.item_id,
            "judul": item.judul,
            "id_member": member.id_member,
            "nama_member": member.nama,
            "keterlambatan_hari": max(0, hari_terlambat),
            "denda": denda
        }
        self.__riwayat_transaksi.append(log_entry)

        if hari_terlambat > 0:
            print(
                f" -> Item '{item.judul}' terlambat dikembalikan {hari_terlambat} hari!\n"
                f"    Dikenakan DENDA ({item.tipe_item}): Rp {denda:,.2f}."
            )
        else:
            print(f" -> Item '{item.judul}' dikembalikan TEPAT WAKTU. Tidak dikenakan denda (Rp 0.00).")

        print(" -> Pengembalian SUKSES! Status item kini TERSEDIA kembali.")
        return (True, denda)

    # --------------------------------------------------------------------------
    # LAPORAN & AUDIT LOG PERPUSTAKAAN
    # --------------------------------------------------------------------------
    def tampilkan_statistik(self) -> None:
        """Mencetak ringkasan metrik statistik operasional perpustakaan."""
        persen_tersedia = (self.total_tersedia / self.total_koleksi * 100) if self.total_koleksi > 0 else 0.0
        print("\n" + "=" * 54)
        print(f"       STATISTIK SISTEM PERPUSTAKAAN")
        print("=" * 54)
        print(f" Nama Perpustakaan    : {self.__nama_perpustakaan}")
        print(f" Total Koleksi Item   : {self.total_koleksi} item")
        print(f" Koleksi Tersedia     : {self.total_tersedia} item ({persen_tersedia:.1f}%)")
        print(f" Koleksi Dipinjam     : {self.total_dipinjam} item")
        print(f" Total Member Aktif   : {self.total_member} anggota")
        print(f" Total Transaksi Log  : {len(self.__riwayat_transaksi)} aktivitas")
        print("=" * 54)

    def tampilkan_audit_log(self) -> None:
        """Mencetak seluruh rekap aktivitas transaksi peminjaman dan pengembalian."""
        print("\n" + "=" * 80)
        print("               LOG RIWAYAT TRANSAKSI PERPUSTAKAAN")
        print("=" * 80)
        if not self.__riwayat_transaksi:
            print("Belum ada riwayat transaksi yang tercatat.")
            print("=" * 80)
            return

        for idx, log in enumerate(self.__riwayat_transaksi, 1):
            if log["tipe"] == "PINJAM":
                print(
                    f"{idx:02d}. [{log['waktu']}] PINJAM  | Item: {log['item_id']} - '{log['judul'][:25]}' "
                    f"-> Member: {log['nama_member']} (Batas: {log['durasi_maksimal']} hari)"
                )
            else:
                denda_str = f"Rp {log['denda']:,.2f}" if log['denda'] > 0 else "Nihil (Rp 0)"
                print(
                    f"{idx:02d}. [{log['waktu']}] KEMBALI | Item: {log['item_id']} - '{log['judul'][:25]}' "
                    f"<- Member: {log['nama_member']} (Telat: {log['keterlambatan_hari']} hr | Denda: {denda_str})"
                )
        print("=" * 80)
