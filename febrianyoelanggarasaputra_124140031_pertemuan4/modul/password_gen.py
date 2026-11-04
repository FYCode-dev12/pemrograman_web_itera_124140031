# ===================================================
# Berkas: password_gen.py
# Deskripsi: Modul pembuat password acak memakai random dan string
# ===================================================

import random
import string


def buat_password_acak(panjang: int = 8) -> str:
    """Membuat password acak dari huruf, angka, dan simbol.

    Password dijamin mengandung minimal satu huruf dan satu angka agar
    tidak menghasilkan kombinasi yang terlalu lemah.

    Args:
        panjang (int): Jumlah karakter password. Minimal 4 karakter.

    Returns:
        str: Password acak dengan panjang sesuai permintaan.

    Raises:
        ValueError: Jika panjang kurang dari 4.
    """
    if panjang < 4:
        raise ValueError("Panjang password minimal 4 karakter.")

    karakter = string.ascii_letters + string.digits + "!@#$%^&*"
    password = [
        random.choice(string.ascii_letters),
        random.choice(string.digits),
        random.choice("!@#$%^&*"),
    ]
    sisa = [random.choice(karakter) for _ in range(panjang - len(password))]
    password += sisa
    random.shuffle(password)
    return "".join(password)


if __name__ == "__main__":
    print("[TEST MODUL] Contoh password acak:")
    for ukuran in (8, 12, 16):
        print(f"  {ukuran} karakter -> {buat_password_acak(ukuran)}")
