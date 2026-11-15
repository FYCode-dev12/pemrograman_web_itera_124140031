# ==============================================================================
# Berkas: member.py
# Deskripsi: Class Member (Anggota Perpustakaan) dengan Enkapsulasi Kuota & Pinjaman
# Praktikan: Febrian Yoel Anggara Saputra (124140031) - Kelas RB
# Praktikum Pengembangan Aplikasi Web - Pertemuan 5
# ==============================================================================

from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from library_item import LibraryItem


class Member:
    """Class Member yang mengelola data anggota perpustakaan dan koleksi pinjamannya.

    Menerapkan Enkapsulasi ketat melalui atribut private (__), validasi batas kuota pinjam,
    dan decorator @property untuk membatasi akses langsung ke data sensitif.
    """

    def __init__(self, id_member: str, nama: str, email: str, tipe_member: str = "Mahasiswa"):
        # 1. Atribut Private: Terproteksi dengan Name Mangling
        self.__id_member = str(id_member).strip()
        self.__nama = str(nama).strip()
        self.__email = str(email).strip()
        self.__tipe_member = str(tipe_member).strip()

        # Batas maksimal peminjaman berbeda sesuai profil keanggotaan
        if self.__tipe_member.lower() in ["dosen", "peneliti"]:
            self.__maks_pinjaman = 5
        else:
            self.__maks_pinjaman = 3  # Standar mahasiswa / umum

        # Koleksi item yang sedang dipinjam oleh anggota ini
        self.__daftar_pinjaman: List["LibraryItem"] = []

    # --------------------------------------------------------------------------
    # PROPERTY GETTERS (Enkapsulasi Read-Only)
    # --------------------------------------------------------------------------
    @property
    def id_member(self) -> str:
        """Mengembalikan ID unik anggota."""
        return self.__id_member

    @property
    def nama(self) -> str:
        """Mengembalikan nama lengkap anggota."""
        return self.__nama

    @property
    def email(self) -> str:
        """Mengembalikan alamat surel anggota."""
        return self.__email

    @property
    def tipe_member(self) -> str:
        """Mengembalikan kategori keanggotaan (Mahasiswa/Dosen)."""
        return self.__tipe_member

    @property
    def maks_pinjaman(self) -> int:
        """Mengembalikan kuota maksimal peminjaman."""
        return self.__maks_pinjaman

    @property
    def daftar_pinjaman(self) -> List["LibraryItem"]:
        """Mengembalikan salinan list item yang sedang dipinjam (defensive copy)."""
        return list(self.__daftar_pinjaman)

    @property
    def jumlah_pinjaman(self) -> int:
        """Mengembalikan jumlah item yang sedang aktif dipinjam saat ini."""
        return len(self.__daftar_pinjaman)

    @property
    def sisa_kuota(self) -> int:
        """Mengembalikan sisa kuota item yang masih dapat dipinjam."""
        return self.__maks_pinjaman - len(self.__daftar_pinjaman)

    # --------------------------------------------------------------------------
    # METODE OPERASIONAL PEMINJAMAN ANGGOTA
    # --------------------------------------------------------------------------
    def bisa_pinjam(self) -> bool:
        """Memeriksa apakah anggota masih memiliki sisa kuota peminjaman."""
        return len(self.__daftar_pinjaman) < self.__maks_pinjaman

    def tambah_pinjaman(self, item: "LibraryItem") -> bool:
        """Menambahkan item perpustakaan ke daftar pinjaman aktif anggota.

        Args:
            item (LibraryItem): Objek koleksi perpustakaan yang dipinjam.

        Returns:
            bool: True jika sukses ditambahkan, False jika kuota penuh atau duplikat.
        """
        if not self.bisa_pinjam():
            print(
                f"[Member {self.__id_member} - {self.__nama}] GAGAL PINJAM: "
                f"Kuota pinjaman sudah mencapai batas maksimal ({self.__maks_pinjaman} item)!"
            )
            return False

        # Cek apakah item sudah pernah dipinjam anggota ini
        for dipinjam in self.__daftar_pinjaman:
            if dipinjam.item_id == item.item_id:
                print(f"[Member {self.__id_member}] Item '{item.judul}' sudah ada di daftar pinjaman Anda!")
                return False

        self.__daftar_pinjaman.append(item)
        print(
            f"[Member {self.__id_member}] Berhasil meminjam '{item.judul}'. "
            f"(Pinjaman aktif: {self.jumlah_pinjaman}/{self.__maks_pinjaman})"
        )
        return True

    def kembalikan_pinjaman(self, item_id: str) -> Optional["LibraryItem"]:
        """Menghapus item dari daftar pinjaman saat dikembalikan ke perpustakaan.

        Args:
            item_id (str): ID unik koleksi yang ingin dikembalikan.

        Returns:
            Optional[LibraryItem]: Objek item yang dikembalikan, atau None jika tidak ditemukan.
        """
        for idx, item in enumerate(self.__daftar_pinjaman):
            if item.item_id == item_id:
                item_dikembalikan = self.__daftar_pinjaman.pop(idx)
                print(
                    f"[Member {self.__id_member}] Berhasil mengembalikan '{item_dikembalikan.judul}'. "
                    f"(Sisa pinjaman aktif: {self.jumlah_pinjaman}/{self.__maks_pinjaman})"
                )
                return item_dikembalikan

        print(f"[Member {self.__id_member}] Gagal: Item ID '{item_id}' tidak tercatat dalam pinjaman Anda!")
        return None

    def tampilkan_daftar_pinjaman(self) -> None:
        """Mencetak kartu informasi daftar pinjaman buku/majalah milik anggota."""
        print(f"\n=== DAFTAR PINJAMAN ANGGOTA [{self.__id_member}] {self.__nama} ===")
        print(f"Kategori : {self.__tipe_member} | Kuota: {self.jumlah_pinjaman}/{self.__maks_pinjaman} item")
        if not self.__daftar_pinjaman:
            print(" -> Tidak ada item yang sedang dipinjam saat ini.")
            return

        for idx, item in enumerate(self.__daftar_pinjaman, 1):
            print(f"  {idx}. [{item.tipe_item}] {item.item_id} - '{item.judul}' ({item.tahun_terbit})")

    # --------------------------------------------------------------------------
    # DUNDER METHODS
    # --------------------------------------------------------------------------
    def __str__(self) -> str:
        return f"Member({self.__id_member} - {self.__nama} [{self.__tipe_member}] | Pinjam: {self.jumlah_pinjaman}/{self.__maks_pinjaman})"

    def __repr__(self) -> str:
        return f"Member(id='{self.__id_member}', nama='{self.__nama}', tipe='{self.__tipe_member}')"

    def __len__(self) -> int:
        """Mengembalikan jumlah pinjaman aktif saat len(member) dipanggil."""
        return len(self.__daftar_pinjaman)

    def __bool__(self) -> bool:
        """Objek Member selalu bernilai True dalam evaluasi kebenaran."""
        return True
