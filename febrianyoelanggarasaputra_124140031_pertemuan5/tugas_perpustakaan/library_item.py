# ==============================================================================
# Berkas: library_item.py
# Deskripsi: Abstract Class LibraryItem dan Subclass Book, Magazine, DigitalMedia
# Praktikan: Febrian Yoel Anggara Saputra (124140031) - Kelas RB
# Praktikum Pengembangan Aplikasi Web - Pertemuan 5
# ==============================================================================

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional


class LibraryItem(ABC):
    """Abstract Base Class yang mendefinisikan kontrak dasar seluruh koleksi perpustakaan.

    Menerapkan 4 pilar OOP:
    - Abstraction: Menyediakan method abstrak get_detail(), hitung_denda(), durasi_pinjam.
    - Encapsulation: Mengamankan atribut menggunakan prefix protected (_) dan dekorator @property.
    """

    def __init__(self, item_id: str, judul: str, tahun_terbit: int):
        # 1. Protected Attributes: dapat diakses oleh subclass namun terlindungi dari luar
        self._item_id = str(item_id).strip()
        self._judul = str(judul).strip()
        self._tahun_terbit = int(tahun_terbit)
        self._is_dipinjam = False
        self._peminjam_id: Optional[str] = None
        self._tgl_pinjam: Optional[datetime] = None

    # --------------------------------------------------------------------------
    # PROPERTY GETTERS & SETTERS (Enkapsulasi)
    # --------------------------------------------------------------------------
    @property
    def item_id(self) -> str:
        """Mengembalikan identifier unik koleksi perpustakaan."""
        return self._item_id

    @property
    def judul(self) -> str:
        """Mengembalikan judul item perpustakaan."""
        return self._judul

    @property
    def tahun_terbit(self) -> int:
        """Mengembalikan tahun penerbitan item perpustakaan."""
        return self._tahun_terbit

    @property
    def is_dipinjam(self) -> bool:
        """Mengembalikan status ketersediaan item (True jika sedang dipinjam)."""
        return self._is_dipinjam

    @is_dipinjam.setter
    def is_dipinjam(self, status: bool):
        """Mengubah status ketersediaan item dengan validasi tipe boolean."""
        if not isinstance(status, bool):
            raise TypeError("Nilai status peminjaman harus berupa boolean (True/False)!")
        self._is_dipinjam = status
        if not status:
            self._peminjam_id = None
            self._tgl_pinjam = None

    @property
    def peminjam_id(self) -> Optional[str]:
        """Mengembalikan ID anggota yang sedang meminjam item ini."""
        return self._peminjam_id

    @property
    def tipe_item(self) -> str:
        """Mengembalikan nama jenis item secara otomatis berdasarkan nama class."""
        return self.__class__.__name__

    # --------------------------------------------------------------------------
    # ABSTRACT METHODS (Kontrak Antarmuka yang Wajib Dioverride oleh Subclass)
    # --------------------------------------------------------------------------
    @abstractmethod
    def get_detail(self) -> str:
        """Menghasilkan representasi string terstruktur rincian informasi spesifik item."""
        pass

    @abstractmethod
    def hitung_denda(self, hari_terlambat: int) -> float:
        """Menghitung besaran nominal denda keterlambatan pengembalian sesuai tarif tipe item.

        Args:
            hari_terlambat (int): Jumlah hari keterlambatan pengembalian.

        Returns:
            float: Total nominal denda dalam Rupiah.
        """
        pass

    @abstractmethod
    def get_durasi_maksimal_pinjam(self) -> int:
        """Mengembalikan batas maksimal hari durasi peminjaman untuk item bersangkutan."""
        pass

    # --------------------------------------------------------------------------
    # CONCRETE METHODS (Logika Bersama untuk Seluruh Subclass)
    # --------------------------------------------------------------------------
    def tandai_dipinjam(self, member_id: str) -> None:
        """Mencatat item telah dipinjam oleh anggota tertentu."""
        self._is_dipinjam = True
        self._peminjam_id = member_id
        self._tgl_pinjam = datetime.now()

    def tandai_dikembalikan(self) -> None:
        """Mereset status item menjadi tersedia kembali di perpustakaan."""
        self._is_dipinjam = False
        self._peminjam_id = None
        self._tgl_pinjam = None

    def __str__(self) -> str:
        status_teks = f"DIPINJAM oleh [{self._peminjam_id}]" if self._is_dipinjam else "TERSEDIA"
        return f"[{self.tipe_item}] {self._item_id} | {self._judul} ({self._tahun_terbit}) - {status_teks}"

    def __repr__(self) -> str:
        return f"{self.tipe_item}(id='{self._item_id}', judul='{self._judul}', dipinjam={self._is_dipinjam})"


class Book(LibraryItem):
    """Subclass representasi buku fisik di perpustakaan."""

    TARIF_DENDA_PER_HARI = 2000.0  # Rp 2.000 per hari keterlambatan
    DURASI_PINJAM_HARI = 14        # Batas pinjam standar: 14 hari

    def __init__(self, item_id: str, judul: str, tahun_terbit: int,
                 penulis: str, isbn: str, jumlah_halaman: int, genre: str):
        super().__init__(item_id, judul, tahun_terbit)
        self._penulis = str(penulis).strip()
        self._isbn = str(isbn).strip()
        self._jumlah_halaman = max(1, int(jumlah_halaman))
        self._genre = str(genre).strip()

    @property
    def penulis(self) -> str:
        return self._penulis

    @property
    def isbn(self) -> str:
        return self._isbn

    @property
    def jumlah_halaman(self) -> int:
        return self._jumlah_halaman

    @property
    def genre(self) -> str:
        return self._genre

    # Implementasi Abstract Method 1
    def get_detail(self) -> str:
        status_str = f"Sedang Dipinjam (Peminjam: {self._peminjam_id})" if self.is_dipinjam else "Tersedia di Rak"
        return (
            f"=== DETAIL BUKU [{self.item_id}] ===\n"
            f"  Judul Buku       : {self.judul}\n"
            f"  Penulis          : {self._penulis}\n"
            f"  Tahun Terbit     : {self.tahun_terbit}\n"
            f"  Nomor ISBN       : {self._isbn}\n"
            f"  Genre / Kategori : {self._genre}\n"
            f"  Jumlah Halaman   : {self._jumlah_halaman} hlm\n"
            f"  Batas Pinjam     : {self.DURASI_PINJAM_HARI} hari\n"
            f"  Tarif Denda      : Rp {self.TARIF_DENDA_PER_HARI:,.2f}/hari\n"
            f"  Status Koleksi   : {status_str}"
        )

    # Implementasi Abstract Method 2
    def hitung_denda(self, hari_terlambat: int) -> float:
        if hari_terlambat <= 0:
            return 0.0
        return float(hari_terlambat * self.TARIF_DENDA_PER_HARI)

    # Implementasi Abstract Method 3
    def get_durasi_maksimal_pinjam(self) -> int:
        return self.DURASI_PINJAM_HARI


class Magazine(LibraryItem):
    """Subclass representasi majalah atau jurnal berkala di perpustakaan."""

    TARIF_DENDA_PER_HARI = 1000.0  # Rp 1.000 per hari keterlambatan
    DURASI_PINJAM_HARI = 7         # Batas pinjam majalah: 7 hari

    def __init__(self, item_id: str, judul: str, tahun_terbit: int,
                 edisi: str, penerbit: str, kategori: str, frekuensi_terbit: str = "Bulanan"):
        super().__init__(item_id, judul, tahun_terbit)
        self._edisi = str(edisi).strip()
        self._penerbit = str(penerbit).strip()
        self._kategori = str(kategori).strip()
        self._frekuensi_terbit = str(frekuensi_terbit).strip()

    @property
    def edisi(self) -> str:
        return self._edisi

    @property
    def penerbit(self) -> str:
        return self._penerbit

    @property
    def kategori(self) -> str:
        return self._kategori

    @property
    def frekuensi_terbit(self) -> str:
        return self._frekuensi_terbit

    # Implementasi Abstract Method 1
    def get_detail(self) -> str:
        status_str = f"Sedang Dipinjam (Peminjam: {self._peminjam_id})" if self.is_dipinjam else "Tersedia di Rak"
        return (
            f"=== DETAIL MAJALAH [{self.item_id}] ===\n"
            f"  Nama Majalah     : {self.judul}\n"
            f"  Nomor Edisi      : {self._edisi}\n"
            f"  Penerbit         : {self._penerbit}\n"
            f"  Tahun Terbit     : {self.tahun_terbit}\n"
            f"  Topik / Kategori : {self._kategori}\n"
            f"  Frekuensi Terbit : {self._frekuensi_terbit}\n"
            f"  Batas Pinjam     : {self.DURASI_PINJAM_HARI} hari\n"
            f"  Tarif Denda      : Rp {self.TARIF_DENDA_PER_HARI:,.2f}/hari\n"
            f"  Status Koleksi   : {status_str}"
        )

    # Implementasi Abstract Method 2
    def hitung_denda(self, hari_terlambat: int) -> float:
        if hari_terlambat <= 0:
            return 0.0
        return float(hari_terlambat * self.TARIF_DENDA_PER_HARI)

    # Implementasi Abstract Method 3
    def get_durasi_maksimal_pinjam(self) -> int:
        return self.DURASI_PINJAM_HARI


class DigitalMedia(LibraryItem):
    """Subclass bonus representasi media digital (Audiobook / E-Book / DVD Dokumenter)."""

    TARIF_DENDA_PER_HARI = 3000.0  # Rp 3.000 per hari keterlambatan
    DURASI_PINJAM_HARI = 3         # Batas pinjam media digital: 3 hari

    def __init__(self, item_id: str, judul: str, tahun_terbit: int,
                 format_media: str, ukuran_mb: float, durasi_menit: int):
        super().__init__(item_id, judul, tahun_terbit)
        self._format_media = str(format_media).strip()
        self._ukuran_mb = max(0.0, float(ukuran_mb))
        self._durasi_menit = max(0, int(durasi_menit))

    @property
    def format_media(self) -> str:
        return self._format_media

    @property
    def ukuran_mb(self) -> float:
        return self._ukuran_mb

    @property
    def durasi_menit(self) -> int:
        return self._durasi_menit

    # Implementasi Abstract Method 1
    def get_detail(self) -> str:
        status_str = f"Lisensi Terpakai (User: {self._peminjam_id})" if self.is_dipinjam else "Lisensi Tersedia"
        return (
            f"=== DETAIL DIGITAL MEDIA [{self.item_id}] ===\n"
            f"  Judul Media      : {self.judul}\n"
            f"  Format File      : {self._format_media}\n"
            f"  Tahun Rilis      : {self.tahun_terbit}\n"
            f"  Ukuran File      : {self._ukuran_mb:.1f} MB\n"
            f"  Durasi Total     : {self._durasi_menit} Menit\n"
            f"  Batas Lisensi    : {self.DURASI_PINJAM_HARI} hari\n"
            f"  Tarif Denda      : Rp {self.TARIF_DENDA_PER_HARI:,.2f}/hari\n"
            f"  Status Lisensi   : {status_str}"
        )

    # Implementasi Abstract Method 2
    def hitung_denda(self, hari_terlambat: int) -> float:
        if hari_terlambat <= 0:
            return 0.0
        return float(hari_terlambat * self.TARIF_DENDA_PER_HARI)

    # Implementasi Abstract Method 3
    def get_durasi_maksimal_pinjam(self) -> int:
        return self.DURASI_PINJAM_HARI

