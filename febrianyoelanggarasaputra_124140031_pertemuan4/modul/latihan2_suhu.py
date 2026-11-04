# ===================================================
# Berkas: latihan2_suhu.py
# Deskripsi: Kalkulator konversi suhu Celsius ke Fahrenheit dan Kelvin
# ===================================================


def celsius_ke_fahrenheit(celsius: float) -> float:
    """Mengonversi Celsius ke Fahrenheit (F = C * 9/5 + 32)."""
    return (celsius * 9 / 5) + 32


def celsius_ke_kelvin(celsius: float) -> float:
    """Mengonversi Celsius ke Kelvin (K = C + 273.15)."""
    return celsius + 273.15


def main() -> None:
    """Meminta input suhu lalu mencetak hasil konversinya."""
    print("=== KONVERSI SUHU CELSIUS ===")
    celsius = float(input("Masukkan suhu dalam Celsius: "))

    fahrenheit = celsius_ke_fahrenheit(celsius)
    kelvin = celsius_ke_kelvin(celsius)

    print("\nHasil konversi:")
    print(f"  Celsius    : {celsius:.2f} C")
    print(f"  Fahrenheit : {fahrenheit:.2f} F")
    print(f"  Kelvin     : {kelvin:.2f} K")


if __name__ == "__main__":
    main()
