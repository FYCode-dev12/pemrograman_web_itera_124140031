"""
Program utama penggunaan modul math_operations.

Mendemonstrasikan dua cara impor sekaligus:
1. `import math_operations` lalu memanggil dengan awalan nama modul.
2. `from math_operations import ...` untuk memakai fungsi secara langsung.

Seluruh fungsi pada modul (luas & keliling 3 bangun datar, konversi
temperatur, dan konstanta PI) dipanggil di sini dengan beberapa nilai uji.
"""

# Cara impor 1: impor seluruh modul dengan alias pendek
import math_operations as mo

# Cara impor 2: impor fungsi dan konstanta secara langsung
from math_operations import celsius_ke_fahrenheit, celsius_ke_kelvin, PI

GARIS = "=" * 58


def judul(teks: str) -> None:
    """Mencetak subjudul bagian agar keluaran terminal mudah dibaca.

    Args:
        teks (str): Judul bagian yang akan dicetak.

    Returns:
        None
    """
    print()
    print(teks)
    print("-" * len(teks))


def bagian_bangun_datar() -> None:
    """Menampilkan hasil perhitungan luas dan keliling bangun datar.

    Returns:
        None
    """
    judul("1. BANGUN DATAR")

    # Persegi
    sisi = 7.0
    print(f"Persegi (sisi = {sisi})")
    print(f"  Luas     : {mo.luas_persegi(sisi):.2f}")
    print(f"  Keliling : {mo.keliling_persegi(sisi):.2f}")

    # Persegi panjang
    panjang, lebar = 12.0, 5.5
    print(f"\nPersegi panjang (panjang = {panjang}, lebar = {lebar})")
    print(f"  Luas     : {mo.luas_persegi_panjang(panjang, lebar):.2f}")
    print(f"  Keliling : {mo.keliling_persegi_panjang(panjang, lebar):.2f}")

    # Lingkaran
    jari_jari = 10.0
    print(f"\nLingkaran (jari-jari = {jari_jari}, PI = {PI})")
    print(f"  Luas     : {mo.luas_lingkaran(jari_jari):.2f}")
    print(f"  Keliling : {mo.keliling_lingkaran(jari_jari):.2f}")


def bagian_temperatur() -> None:
    """Menampilkan hasil konversi temperatur suhu.

    Returns:
        None
    """
    judul("2. KONVERSI TEMPERATUR")

    # Memakai fungsi hasil `from ... import ...`
    suhu_celsius = [0.0, 25.0, 37.0, 100.0]
    print(f"{'Celsius':>10} | {'Fahrenheit':>12} | {'Kelvin':>10}")
    print("-" * 38)
    for celsius in suhu_celsius:
        fahrenheit = celsius_ke_fahrenheit(celsius)
        kelvin = celsius_ke_kelvin(celsius)
        print(f"{celsius:>10.2f} | {fahrenheit:>12.2f} | {kelvin:>10.2f}")

    # Konversi balik memakai cara impor modul
    fahrenheit = 212.0
    kelvin = 300.0
    print()
    print(f"{fahrenheit:.2f} F = {mo.fahrenheit_ke_celsius(fahrenheit):.2f} C")
    print(f"{kelvin:.2f} K   = {mo.kelvin_ke_celsius(kelvin):.2f} C")


def bagian_uji_galat() -> None:
    """Menunjukkan penanganan galat (error handling) pada modul.

    Returns:
        None
    """
    judul("3. UJI VALIDASI INPUT")

    kasus_uji = [
        ("Sisi persegi -3", lambda: mo.luas_persegi(-3)),
        ("Jari-jari 0", lambda: mo.luas_lingkaran(0)),
        ("Suhu -300 C ke Kelvin", lambda: mo.celsius_ke_kelvin(-300)),
    ]

    for keterangan, aksi in kasus_uji:
        try:
            hasil = aksi()
            print(f"  {keterangan:<24} -> {hasil}")
        except ValueError as galat:
            print(f"  {keterangan:<24} -> ValueError: {galat}")


def main() -> None:
    """Menjalankan seluruh demonstrasi modul math_operations."""
    print(GARIS)
    print("   DEMO MODUL MATEMATIKA (math_operations.py)".center(58))
    print(GARIS)

    bagian_bangun_datar()
    bagian_temperatur()
    bagian_uji_galat()

    print()
    print(GARIS)
    print("Selesai: seluruh fungsi modul berhasil dipanggil.")
    print(GARIS)


if __name__ == "__main__":
    main()
