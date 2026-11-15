# ==============================================================================
# Berkas: main.py
# Deskripsi: Program Utama Pengujian Sistem Manajemen Perpustakaan Berbasis OOP
# Praktikan: Febrian Yoel Anggara Saputra (124140031) - Kelas RB
# Praktikum Pengembangan Aplikasi Web - Pertemuan 5
# ==============================================================================

import sys
from library_item import LibraryItem, Book, Magazine, DigitalMedia
from member import Member
from library import Library


def cetak_banner_identitas():
    """Mencetak header identitas resmi praktikan ITERA."""
    print("=" * 86)
    print("      PRAKTIKUM PENGEMBANGAN APLIKASI WEB - PERTEMUAN 5 (PYTHON OOP)")
    print("                   INSTITUT TEKNOLOGI SUMATERA (ITERA)")
    print("=" * 86)
    print("  Nama Lengkap    : Febrian Yoel Anggara Saputra")
    print("  NIM             : 124140031")
    print("  Kelas Praktikum : RB")
    print("  Materi Pokok    : Class, Inheritance, Encapsulation, Polymorphism, Abstract Class")
    print("=" * 86)


def jalankan_demonstrasi():
    """Menjalankan seluruh skenario pengujian komprehensif sistem perpustakaan."""
    cetak_banner_identitas()

    # --------------------------------------------------------------------------
    # 1. INISIALISASI PERPUSTAKAAN & PENDAFTARAN KOLEKSI
    # --------------------------------------------------------------------------
    print("\n>>> BAGIAN 1: INISIALISASI PERPUSTAKAAN & REGISTRASI KOLEKSI <<<")
    perpus = Library("Perpustakaan Pintar ITERA")

    # Membuat beberapa objek Book
    buku1 = Book(
        item_id="BK-001",
        judul="Clean Code: A Handbook of Agile Software Craftsmanship",
        tahun_terbit=2008,
        penulis="Robert C. Martin",
        isbn="978-0132350884",
        jumlah_halaman=464,
        genre="Software Engineering"
    )

    buku2 = Book(
        item_id="BK-002",
        judul="Design Patterns: Elements of Reusable Object-Oriented Software",
        tahun_terbit=1994,
        penulis="Erich Gamma et al. (Gang of Four)",
        isbn="978-0201633610",
        jumlah_halaman=395,
        genre="Software Architecture"
    )

    buku3 = Book(
        item_id="BK-003",
        judul="Fluent Python: Clear, Concise, and Effective Programming",
        tahun_terbit=2022,
        penulis="Luciano Ramalho",
        isbn="978-1492056355",
        jumlah_halaman=1014,
        genre="Programming Language"
    )

    # Membuat objek Magazine
    majalah1 = Magazine(
        item_id="MG-001",
        judul="National Geographic Indonesia",
        tahun_terbit=2026,
        edisi="Vol. 22 No. 11 - Ekspedisi Selat Sunda",
        penerbit="Gramedia Media",
        kategori="Sains & Alam",
        frekuensi_terbit="Bulanan"
    )

    majalah2 = Magazine(
        item_id="MG-002",
        judul="IEEE Software Magazine",
        tahun_terbit=2026,
        edisi="Issue 5 - Modern Web Architectures",
        penerbit="IEEE Computer Society",
        kategori="Teknologi Informasi",
        frekuensi_terbit="Dua Bulanan"
    )

    # Membuat objek DigitalMedia (Nilai Plus)
    digital1 = DigitalMedia(
        item_id="DG-001",
        judul="Audiobook: The Pragmatic Programmer 20th Anniversary",
        tahun_terbit=2020,
        format_media="Audio FLAC Hi-Res",
        ukuran_mb=480.5,
        durasi_menit=580
    )

    # Mendaftarkan seluruh item ke perpustakaan
    for item in [buku1, buku2, buku3, majalah1, majalah2, digital1]:
        perpus.tambah_item(item)

    # --------------------------------------------------------------------------
    # 2. MENAMPILKAN KATALOG KOLEKSI (POLIMORFISME)
    # --------------------------------------------------------------------------
    print("\n>>> BAGIAN 2: MENAMPILKAN SELURUH KATALOG KOLEKSI PERPUSTAKAAN <<<")
    perpus.tampilkan_katalog(hanya_tersedia=False)

    # --------------------------------------------------------------------------
    # 3. PENCARIAN ITEM BERDASARKAN ID & KATA KUNCI JUDUL
    # --------------------------------------------------------------------------
    print("\n>>> BAGIAN 3: PENCARIAN ITEM BERDASARKAN ID & KATA KUNCI JUDUL <<<")

    # Pencarian ID yang ada
    print("\n[Pencarian Berdasarkan ID: 'BK-002']")
    item_ditemukan = perpus.cari_item_by_id("BK-002")
    if item_ditemukan:
        print(f"Hasil Ditemukan: {item_ditemukan}")
        print("\nDetail Lengkap Objek:")
        print(item_ditemukan.get_detail())
    else:
        print("Item tidak ditemukan!")

    # Pencarian ID yang tidak ada
    print("\n[Pencarian Berdasarkan ID Fiktif: 'BK-999']")
    item_fiktif = perpus.cari_item_by_id("BK-999")
    print(f"Hasil: {item_fiktif} (Terbukti None)")

    # Pencarian berdasarkan kata kunci judul
    kata_kunci = "Python"
    print(f"\n[Pencarian Berdasarkan Kata Kunci Judul: '{kata_kunci}']")
    hasil_judul = perpus.cari_item_by_judul(kata_kunci)
    print(f"Ditemukan {len(hasil_judul)} item yang memuat '{kata_kunci}':")
    for res in hasil_judul:
        print(f" -> [{res.tipe_item}] {res.item_id} | {res.judul}")

    kata_kunci_2 = "Software"
    print(f"\n[Pencarian Berdasarkan Kata Kunci Judul: '{kata_kunci_2}']")
    hasil_judul_2 = perpus.cari_item_by_judul(kata_kunci_2)
    print(f"Ditemukan {len(hasil_judul_2)} item yang memuat '{kata_kunci_2}':")
    for res in hasil_judul_2:
        print(f" -> [{res.tipe_item}] {res.item_id} | {res.judul}")

    # --------------------------------------------------------------------------
    # 4. REGISTRASI ANGGOTA (MEMBER)
    # --------------------------------------------------------------------------
    print("\n>>> BAGIAN 4: REGISTRASI ANGGOTA PERPUSTAKAAN (MEMBER) <<<")
    member1 = Member("MBR-001", "Febrian Yoel Anggara Saputra", "febrian.124140031@student.itera.ac.id", "Mahasiswa")
    member2 = Member("MBR-002", "Dr. Eng. Ir. Hendra Saputra", "hendra.saputra@if.itera.ac.id", "Dosen")

    perpus.tambah_member(member1)
    perpus.tambah_member(member2)
    perpus.tampilkan_daftar_member()

    # --------------------------------------------------------------------------
    # 5. DEMONSTRASI PEMINJAMAN ITEM & VALIDASI KUOTA
    # --------------------------------------------------------------------------
    print("\n>>> BAGIAN 5: TRANSAKSI PEMINJAMAN ITEM & VALIDASI KUOTA <<<")

    # Member 1 meminjam 3 item (mencapai batas kuota maksimal mahasiswa = 3 item)
    perpus.pinjam_item("BK-001", "MBR-001")
    perpus.pinjam_item("MG-001", "MBR-001")
    perpus.pinjam_item("DG-001", "MBR-001")

    # Member 1 mencoba meminjam item ke-4 (harus DITOLAK karena kuota penuh)
    print("\n[Uji Validasi Kuota: Mencoba meminjam melebihi kuota 3 item]")
    perpus.pinjam_item("BK-002", "MBR-001")

    # Member 2 (Dosen) meminjam item yang baru saja ditolak untuk member 1
    print("\n[Member 2 (Dosen - Kuota 5) meminjam 'BK-002']")
    perpus.pinjam_item("BK-002", "MBR-002")

    # Uji coba meminjam buku yang sedang dipinjam orang lain
    print("\n[Uji Validasi Ketersediaan: Mencoba meminjam buku yang sedang dipinjam]")
    perpus.pinjam_item("BK-001", "MBR-002")

    # Menampilkan daftar pinjaman masing-masing member
    member1.tampilkan_daftar_pinjaman()
    member2.tampilkan_daftar_pinjaman()

    # --------------------------------------------------------------------------
    # 6. KATALOG ITEM YANG MASIH TERSEDIA (FILTER POLIMORFIK)
    # --------------------------------------------------------------------------
    print("\n>>> BAGIAN 6: STATUS KATALOG TERSEDIA SETELAH PEMINJAMAN <<<")
    perpus.tampilkan_katalog(hanya_tersedia=True)

    # --------------------------------------------------------------------------
    # 7. PENGEMBALIAN ITEM & PERHITUNGAN DENDA POLIMORFIK
    # --------------------------------------------------------------------------
    print("\n>>> BAGIAN 7: PENGEMBALIAN ITEM & PERHITUNGAN DENDA POLIMORFIK <<<")

    # Kasus 1: Buku BK-001 dikembalikan TEPAT WAKTU (0 hari telat)
    print("\n--- Kasus 1: Buku dikembalikan tepat waktu ---")
    perpus.kembalikan_item("BK-001", "MBR-001", hari_terlambat=0)

    # Kasus 2: Majalah MG-001 dikembalikan TELAT 4 HARI (Tarif Majalah: Rp 1.000/hari -> Rp 4.000)
    print("\n--- Kasus 2: Majalah dikembalikan telat 4 hari ---")
    perpus.kembalikan_item("MG-001", "MBR-001", hari_terlambat=4)

    # Kasus 3: Media Digital DG-001 dikembalikan TELAT 2 HARI (Tarif Digital: Rp 3.000/hari -> Rp 6.000)
    print("\n--- Kasus 3: Digital Media dikembalikan telat 2 hari ---")
    perpus.kembalikan_item("DG-001", "MBR-001", hari_terlambat=2)

    # Kasus 4: Buku BK-002 milik Member 2 dikembalikan TELAT 5 HARI (Tarif Buku: Rp 2.000/hari -> Rp 10.000)
    print("\n--- Kasus 4: Buku oleh Dosen dikembalikan telat 5 hari ---")
    perpus.kembalikan_item("BK-002", "MBR-002", hari_terlambat=5)

    # --------------------------------------------------------------------------
    # 8. PEMBUKTIAN ENKAPSULASI & DATA PROTECTION
    # --------------------------------------------------------------------------
    print("\n>>> BAGIAN 8: PEMBUKTIAN ENKAPSULASI & AKSES ATRIBUT PRIVATE <<<")

    # Uji 1: Membuktikan __koleksi pada Library tidak dapat diakses secara langsung
    print("\n[Uji Akses Langsung Atribut Private perpus.__koleksi]")
    try:
        print(perpus.__koleksi)
    except AttributeError as err:
        print(f"Proteksi Enkapsulasi Terbukti: {err}")

    # Uji 2: Pembuktian mekanisme Python Name Mangling
    print("\n[Pembuktian Python Name Mangling: perpus._Library__koleksi]")
    koleksi_internal = getattr(perpus, "_Library__koleksi", None)
    print(f"Tipe struktur data internal: {type(koleksi_internal)}")
    print(f"Jumlah kunci dalam kamus private: {len(koleksi_internal)} entri")

    # Uji 3: Validasi Setter Property is_dipinjam pada LibraryItem
    print("\n[Uji Setter Validation: is_dipinjam hanya menerima tipe bool]")
    try:
        buku1.is_dipinjam = "Bukan Boolean"
    except TypeError as err:
        print(f"Validasi Setter Berhasil Menolak Nilai Invalid: {err}")

    # --------------------------------------------------------------------------
    # 9. PEMBUKTIAN ENFORCEMENT ABSTRACT CLASS
    # --------------------------------------------------------------------------
    print("\n>>> BAGIAN 9: PEMBUKTIAN ENFORCEMENT ABSTRACT BASE CLASS <<<")

    # Coba instansiasi langsung dari abstract class LibraryItem
    print("\n[Uji Coba Instansiasi Langsung LibraryItem(ABC)]")
    try:
        item_abstrak = LibraryItem("ABS-001", "Item Fiktif", 2026)
    except TypeError as err:
        print(f"Python Berhasil Mencegah Instansiasi Abstract Class:\n -> {err}")

    # Coba subclass yang tidak mengimplementasikan method abstract
    print("\n[Uji Coba Subclass yang 'Lupa' Mengimplementasikan Method Abstrak]")
    class ItemCacat(LibraryItem):
        def __init__(self, item_id, judul, tahun):
            super().__init__(item_id, judul, tahun)
        # Tidak mengimplementasikan get_detail(), hitung_denda(), get_durasi_maksimal_pinjam()

    try:
        rusak = ItemCacat("BRK-001", "Koleksi Cacat", 2026)
    except TypeError as err:
        print(f"Python Berhasil Mencegah Instansiasi Subclass yang Cacat:\n -> {err}")

    # --------------------------------------------------------------------------
    # 10. REKAP STATISTIK & AUDIT LOG PERPUSTAKAAN
    # --------------------------------------------------------------------------
    print("\n>>> BAGIAN 10: REKAP STATISTIK SISTEM & LOG TRANSAKSI <<<")
    perpus.tampilkan_statistik()
    perpus.tampilkan_audit_log()

    print("\n" + "=" * 86)
    print(" SELURUH PENGUJIAN SISTEM MANAJEMEN PERPUSTAKAAN SELESAI DENGAN SUKSES 100%!")
    print("=" * 86)


def menu_interaktif():
    """Menyediakan antarmuka CLI interaktif untuk pengguna."""
    cetak_banner_identitas()
    perpus = Library("Perpustakaan Pintar ITERA (Mode Interaktif)")

    # Data awal siap pakai
    perpus.tambah_item(Book("BK-001", "Clean Code", 2008, "Robert C. Martin", "978-0132350884", 464, "Software"))
    perpus.tambah_item(Book("BK-002", "Design Patterns", 1994, "GoF", "978-0201633610", 395, "Architecture"))
    perpus.tambah_item(Magazine("MG-001", "National Geographic", 2026, "Nov 2026", "Gramedia", "Sains"))
    perpus.tambah_item(DigitalMedia("DG-001", "Python Mastery Audio", 2024, "FLAC", 350.0, 180))

    member_saya = Member("MBR-001", "Febrian Yoel Anggara Saputra", "febrian@student.itera.ac.id", "Mahasiswa")
    perpus.tambah_member(member_saya)

    while True:
        print("\n" + "=" * 48)
        print("          MENU SISTEM PERPUSTAKAAN")
        print("=" * 48)
        print("1. Tampilkan Semua Katalog Koleksi")
        print("2. Tampilkan Katalog Item Tersedia")
        print("3. Cari Item Berdasarkan Judul")
        print("4. Cari Item Berdasarkan ID")
        print("5. Pinjam Item Perpustakaan")
        print("6. Kembalikan Item Perpustakaan")
        print("7. Tampilkan Pinjaman Anggota")
        print("8. Tampilkan Ringkasan Statistik")
        print("9. Tampilkan Log Riwayat Transaksi")
        print("0. Keluar dari Program")
        print("=" * 48)

        pilihan = input("Pilih menu [0-9]: ").strip()

        if pilihan == "1":
            perpus.tampilkan_katalog(hanya_tersedia=False)
        elif pilihan == "2":
            perpus.tampilkan_katalog(hanya_tersedia=True)
        elif pilihan == "3":
            kata = input("Masukkan kata kunci judul: ").strip()
            hasil = perpus.cari_item_by_judul(kata)
            print(f"Hasil pencarian '{kata}' ({len(hasil)} item):")
            for item in hasil:
                print(f" -> {item}")
        elif pilihan == "4":
            item_id = input("Masukkan ID Item (misal: BK-001): ").strip()
            item = perpus.cari_item_by_id(item_id)
            if item:
                print("\n" + item.get_detail())
            else:
                print(f"Item dengan ID '{item_id}' tidak ditemukan!")
        elif pilihan == "5":
            item_id = input("Masukkan ID Item yang ingin dipinjam: ").strip()
            perpus.pinjam_item(item_id, member_saya.id_member)
        elif pilihan == "6":
            item_id = input("Masukkan ID Item yang dikembalikan: ").strip()
            try:
                hari = int(input("Jumlah hari keterlambatan (0 jika tepat waktu): ").strip() or "0")
            except ValueError:
                hari = 0
            perpus.kembalikan_item(item_id, member_saya.id_member, hari_terlambat=hari)
        elif pilihan == "7":
            member_saya.tampilkan_daftar_pinjaman()
        elif pilihan == "8":
            perpus.tampilkan_statistik()
        elif pilihan == "9":
            perpus.tampilkan_audit_log()
        elif pilihan == "0":
            print("\nTerima kasih telah menggunakan Sistem Perpustakaan ITERA.")
            break
        else:
            print("Pilihan menu tidak valid, silakan coba lagi!")


if __name__ == "__main__":
    # Jika dijalankan dengan argumen --interactive atau -i, masuk ke mode menu interaktif
    if len(sys.argv) > 1 and sys.argv[1] in ["--interactive", "-i"]:
        menu_interaktif()
    else:
        jalankan_demonstrasi()

