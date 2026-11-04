"""
Modul Matematika Python.

Menyediakan fungsi luas dan keliling bangun datar (persegi, persegi
panjang, lingkaran) serta konversi temperatur suhu.

Modul ini tidak menjalankan apa pun saat diimpor; seluruh fungsi hanya
aktif ketika dipanggil oleh program lain seperti main.py.
"""

import math

# Konstanta phi yang dipakai untuk perhitungan lingkaran
PI = 3.14159


# ------------------------------------------------------------------
# Bangun datar: persegi
# ------------------------------------------------------------------
def luas_persegi(sisi: float) -> float:
    """Menghitung luas persegi.

    Args:
        sisi (float): Panjang sisi persegi.

    Returns:
        float: Luas persegi (sisi * sisi).

    Raises:
        ValueError: Jika sisi kurang dari atau sama dengan nol.
    """
    if sisi <= 0:
        raise ValueError("Sisi persegi harus lebih besar dari 0.")
    return sisi * sisi


def keliling_persegi(sisi: float) -> float:
    """Menghitung keliling persegi.

    Args:
        sisi (float): Panjang sisi persegi.

    Returns:
        float: Keliling persegi (4 * sisi).

    Raises:
        ValueError: Jika sisi kurang dari atau sama dengan nol.
    """
    if sisi <= 0:
        raise ValueError("Sisi persegi harus lebih besar dari 0.")
    return 4 * sisi


# ------------------------------------------------------------------
# Bangun datar: persegi panjang
# ------------------------------------------------------------------
def luas_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung luas persegi panjang.

    Args:
        panjang (float): Panjang persegi panjang.
        lebar (float): Lebar persegi panjang.

    Returns:
        float: Luas persegi panjang (panjang * lebar).

    Raises:
        ValueError: Jika panjang atau lebar tidak positif.
    """
    if panjang <= 0 or lebar <= 0:
        raise ValueError("Panjang dan lebar harus lebih besar dari 0.")
    return panjang * lebar


def keliling_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung keliling persegi panjang.

    Args:
        panjang (float): Panjang persegi panjang.
        lebar (float): Lebar persegi panjang.

    Returns:
        float: Keliling persegi panjang (2 * (panjang + lebar)).

    Raises:
        ValueError: Jika panjang atau lebar tidak positif.
    """
    if panjang <= 0 or lebar <= 0:
        raise ValueError("Panjang dan lebar harus lebih besar dari 0.")
    return 2 * (panjang + lebar)


# ------------------------------------------------------------------
# Bangun datar: lingkaran
# ------------------------------------------------------------------
def luas_lingkaran(jari_jari: float) -> float:
    """Menghitung luas lingkaran.

    Args:
        jari_jari (float): Jari-jari lingkaran.

    Returns:
        float: Luas lingkaran (PI * r^2).

    Raises:
        ValueError: Jika jari-jari tidak positif.
    """
    if jari_jari <= 0:
        raise ValueError("Jari-jari harus lebih besar dari 0.")
    return PI * jari_jari ** 2


def keliling_lingkaran(jari_jari: float) -> float:
    """Menghitung keliling (circumference) lingkaran.

    Args:
        jari_jari (float): Jari-jari lingkaran.

    Returns:
        float: Keliling lingkaran (2 * PI * r).

    Raises:
        ValueError: Jika jari-jari tidak positif.
    """
    if jari_jari <= 0:
        raise ValueError("Jari-jari harus lebih besar dari 0.")
    return 2 * PI * jari_jari


# ------------------------------------------------------------------
# Konversi temperatur
# ------------------------------------------------------------------
def celsius_ke_fahrenheit(celsius: float) -> float:
    """Mengonversi suhu Celsius ke Fahrenheit.

    Args:
        celsius (float): Suhu dalam derajat Celsius.

    Returns:
        float: Suhu dalam derajat Fahrenheit (C * 9/5 + 32).
    """
    return (celsius * 9 / 5) + 32


def celsius_ke_kelvin(celsius: float) -> float:
    """Mengonversi suhu Celsius ke Kelvin.

    Args:
        celsius (float): Suhu dalam derajat Celsius.

    Returns:
        float: Suhu dalam Kelvin (C + 273.15).

    Raises:
        ValueError: Jika suhu di bawah nol mutlak (-273.15 C).
    """
    if celsius < -273.15:
        raise ValueError("Suhu tidak boleh di bawah nol mutlak (-273.15 C).")
    return celsius + 273.15


def fahrenheit_ke_celsius(fahrenheit: float) -> float:
    """Mengonversi suhu Fahrenheit ke Celsius.

    Args:
        fahrenheit (float): Suhu dalam derajat Fahrenheit.

    Returns:
        float: Suhu dalam derajat Celsius ((F - 32) * 5/9).
    """
    return (fahrenheit - 32) * 5 / 9


def kelvin_ke_celsius(kelvin: float) -> float:
    """Mengonversi suhu Kelvin ke Celsius.

    Args:
        kelvin (float): Suhu dalam Kelvin.

    Returns:
        float: Suhu dalam derajat Celsius (K - 273.15).

    Raises:
        ValueError: Jika suhu Kelvin negatif.
    """
    if kelvin < 0:
        raise ValueError("Suhu Kelvin tidak boleh negatif.")
    return kelvin - 273.15


def akar_kuadrat(angka: float) -> float:
    """Menghitung akar kuadrat memakai modul math standar.

    Args:
        angka (float): Bilangan yang akan dicari akarnya.

    Returns:
        float: Akar kuadrat dari angka.

    Raises:
        ValueError: Jika angka negatif.
    """
    if angka < 0:
        raise ValueError("Akar kuadrat hanya untuk bilangan non-negatif.")
    return math.sqrt(angka)
