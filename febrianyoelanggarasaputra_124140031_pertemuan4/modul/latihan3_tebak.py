# ===================================================
# Berkas: latihan3_tebak.py
# Deskripsi: Game tebak angka rahasia dengan while loop dan break
# ===================================================

import random


def main() -> None:
    """Menjalankan permainan tebak angka 1 sampai 20."""
    angka_rahasia = random.randint(1, 20)
    percobaan = 0

    print("=== GAME TEBAK ANGKA RAHASIA ===")
    print("Saya menyimpan angka antara 1 sampai 20.")
    print("Ketik 0 untuk menyerah.\n")

    while True:
        try:
            tebakan = int(input("Masukkan tebakan Anda: "))
        except ValueError:
            print("Input harus berupa bilangan bulat!\n")
            continue

        if tebakan == 0:
            print(f"Anda menyerah. Angka rahasianya adalah {angka_rahasia}.")
            break

        percobaan += 1

        if tebakan < angka_rahasia:
            print("Terlalu kecil!")
        elif tebakan > angka_rahasia:
            print("Terlalu besar!")
        else:
            print(
                "Selamat, tebakan benar! "
                f"Anda berhasil dalam {percobaan} percobaan."
            )
            break

        print()


if __name__ == "__main__":
    main()
