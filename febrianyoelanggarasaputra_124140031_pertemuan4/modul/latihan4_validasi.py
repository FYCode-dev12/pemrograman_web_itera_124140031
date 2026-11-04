# ===================================================
# Berkas: latihan4_validasi.py
# Deskripsi: Fungsi validator password sederhana
# ===================================================


def validasi_password(password: str) -> bool:
    """Memvalidasi kekuatan password.

    Password dianggap valid bila panjangnya minimal 8 karakter dan
    mengandung setidaknya satu karakter angka.

    Args:
        password (str): Password yang akan diuji.

    Returns:
        bool: True jika valid, False jika tidak.
    """
    if len(password) < 8:
        return False
    return any(karakter.isdigit() for karakter in password)


def main() -> None:
    """Menguji fungsi validasi_password dengan beberapa contoh."""
    daftar_uji = [
        "rahasia1",      # valid: 8 karakter dan ada angka
        "P@ssw0rd2026",  # valid
        "pendek1",       # tidak valid: hanya 7 karakter
        "tanpaangka",    # tidak valid: tidak ada angka
        "",              # tidak valid: kosong
    ]

    print("=== UJI FUNGSI VALIDASI PASSWORD ===")
    print(f"{'Password':<16} | {'Panjang':>7} | {'Valid?':>6}")
    print("-" * 36)

    for password in daftar_uji:
        tampil = password if password else "(kosong)"
        status = "YA" if validasi_password(password) else "TIDAK"
        print(f"{tampil:<16} | {len(password):>7} | {status:>6}")

    # Uji interaktif
    print("\nCoba password Anda sendiri:")
    kandidat = input("Password: ")
    if validasi_password(kandidat):
        print("Password VALID (minimal 8 karakter dan mengandung angka).")
    else:
        print(
            "Password TIDAK VALID "
            "(butuh minimal 8 karakter dan satu angka)."
        )


if __name__ == "__main__":
    main()
