# ===================================================
# Berkas: latihan5_kontak.py
# Deskripsi: Katalog kontak sederhana memakai dictionary
# ===================================================

kontak: dict[str, str] = {
    "Budi Santoso": "0812-3456-7890",
    "Siti Rahma": "0857-1122-3344",
    "Andi Pratama": "0821-9988-7766",
}


def tambah_kontak(nama: str, nomor: str) -> str:
    """Menambahkan atau memperbarui kontak pada katalog.

    Args:
        nama (str): Nama kontak.
        nomor (str): Nomor telepon kontak.

    Returns:
        str: Pesan hasil operasi.
    """
    nama_rapi = nama.strip().title()
    if not nama_rapi or not nomor.strip():
        return "Nama dan nomor tidak boleh kosong."

    status = "diperbarui" if nama_rapi in kontak else "ditambahkan"
    kontak[nama_rapi] = nomor.strip()
    return f"Kontak {nama_rapi} berhasil {status}."


def cari_kontak(nama: str) -> str:
    """Mencari nomor telepon berdasarkan nama kontak memakai .get().

    Args:
        nama (str): Nama kontak yang dicari.

    Returns:
        str: Nomor telepon, atau pesan bila kontak tidak ditemukan.
    """
    nomor = kontak.get(nama.strip().title(), "Kontak tidak ditemukan.")
    return nomor


def tampilkan_kontak() -> None:
    """Menampilkan seluruh kontak yang tersimpan.

    Returns:
        None
    """
    print(f"\nDaftar Kontak ({len(kontak)} kontak)")
    print("-" * 38)
    for nomor_urut, (nama, nomor) in enumerate(kontak.items(), start=1):
        print(f"{nomor_urut:>2}. {nama:<20} : {nomor}")
    print("-" * 38)


def main() -> None:
    """Menjalankan menu interaktif katalog kontak."""
    while True:
        print("\n=== KATALOG KONTAK ===")
        print("1. Tambah kontak")
        print("2. Cari nomor telepon")
        print("3. Tampilkan semua kontak")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            nama = input("Nama kontak  : ")
            nomor = input("Nomor telepon: ")
            print(tambah_kontak(nama, nomor))
        elif pilihan == "2":
            nama = input("Nama yang dicari: ")
            print(f"Nomor telepon: {cari_kontak(nama)}")
        elif pilihan == "3":
            tampilkan_kontak()
        elif pilihan == "4":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()
