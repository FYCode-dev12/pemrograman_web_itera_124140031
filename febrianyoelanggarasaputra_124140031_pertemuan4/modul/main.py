# ===================================================
# Berkas: main.py (latihan modul)
# Deskripsi: Menguji modul kustom password_gen
# ===================================================

import password_gen as pg


def main() -> None:
    """Membuat beberapa contoh password dengan panjang berbeda."""
    print("=== GENERATOR PASSWORD ACAK ===")

    for panjang in (8, 12, 16):
        password = pg.buat_password_acak(panjang)
        print(f"Panjang {panjang:>2} karakter : {password}")

    print("\nUji validasi panjang minimum:")
    try:
        pg.buat_password_acak(3)
    except ValueError as galat:
        print(f"  ValueError: {galat}")


if __name__ == "__main__":
    main()
