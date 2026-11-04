"""
Program Penghitung BMI (Body Mass Index) Sederhana.

Program menerima berat badan (kg) dan tinggi badan (m) dari pengguna,
menghitung nilai BMI dengan rumus:

    BMI = berat / (tinggi * tinggi)

lalu menampilkan nilai BMI (2 angka desimal) beserta kategori status
berat badan sesuai ambang batas WHO.
"""


def baca_angka(prompt: str) -> float:
    """Membaca satu angka positif dari pengguna.

    Args:
        prompt (str): Teks yang ditampilkan sebelum kolom input.

    Returns:
        float: Nilai numerik yang lebih besar dari nol.
    """
    while True:
        try:
            nilai = float(input(prompt))
        except ValueError:
            print("  [!] Input tidak valid. Masukkan angka, contoh: 65.5")
            continue

        if nilai <= 0:
            print("  [!] Nilai harus lebih besar dari 0.")
            continue

        return nilai


def hitung_bmi(berat_kg: float, tinggi_m: float) -> float:
    """Menghitung nilai BMI.

    Args:
        berat_kg (float): Berat badan dalam kilogram.
        tinggi_m (float): Tinggi badan dalam meter.

    Returns:
        float: Nilai BMI hasil perhitungan.

    Raises:
        ValueError: Jika tinggi badan nol atau negatif.
    """
    if tinggi_m <= 0:
        raise ValueError("Tinggi badan harus lebih besar dari 0 meter.")
    return berat_kg / (tinggi_m ** 2)


def kategori_bmi(bmi: float) -> str:
    """Menentukan kategori status berat badan berdasarkan nilai BMI.

    Args:
        bmi (float): Nilai BMI yang sudah dihitung.

    Returns:
        str: Kategori berat badan (kurang, normal, berlebih, atau obesitas).
    """
    if bmi < 18.5:
        return "Berat badan kurang"
    elif bmi < 25:
        return "Berat badan normal"
    elif bmi < 30:
        return "Berat badan berlebih"
    else:
        return "Obesitas"


def main() -> None:
    """Menjalankan alur utama program penghitung BMI."""
    garis = "=" * 48

    print(garis)
    print("      KALKULATOR BMI (BODY MASS INDEX)".center(48))
    print(garis)

    berat = baca_angka("Masukkan berat badan (kg) : ")
    tinggi = baca_angka("Masukkan tinggi badan (m) : ")

    # Tinggi harus dalam meter. Nilai seperti 170 (cm) membuat BMI mendekati 0
    # sehingga ditolak dengan pesan yang jelas, bukan dibiarkan lolos.
    while tinggi > 3:
        print("  [!] Tinggi badan harus dalam meter, bukan sentimeter.")
        print("      Contoh: 170 cm ditulis 1.70")
        tinggi = baca_angka("Masukkan tinggi badan (m) : ")

    bmi = hitung_bmi(berat, tinggi)
    kategori = kategori_bmi(bmi)

    print("-" * 48)
    print(f"Berat badan  : {berat:.2f} kg")
    print(f"Tinggi badan : {tinggi:.2f} m")
    print(f"Nilai BMI    : {bmi}")
    print(f"Kategori     : {kategori}")
    print(garis)


if __name__ == "__main__":
    main()
