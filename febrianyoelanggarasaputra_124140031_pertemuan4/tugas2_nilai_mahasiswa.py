"""
Program Pengelolaan Data Nilai Mahasiswa.

Program menyimpan data 6 mahasiswa dalam sebuah list berisi dictionary,
menghitung nilai akhir dengan bobot 30% UTS + 40% UAS + 30% Tugas,
menentukan grade A-E, menampilkan tabel rapi, lalu melaporkan mahasiswa
dengan nilai akhir tertinggi dan terendah.
"""

from typing import Any

# Bobot penilaian (total 100%)
BOBOT_UTS = 0.30
BOBOT_UAS = 0.40
BOBOT_TUGAS = 0.30

# Data mentah: list berisi minimal 5 dictionary mahasiswa
DATA_MAHASISWA: list[dict[str, Any]] = [
    {
        "nama": "Andi Pratama",
        "nim": "124140001",
        "nilai_uts": 78,
        "nilai_uas": 85,
        "nilai_tugas": 90,
    },
    {
        "nama": "Siti Rahma",
        "nim": "124140002",
        "nilai_uts": 92,
        "nilai_uas": 88,
        "nilai_tugas": 95,
    },
    {
        "nama": "Budi Santoso",
        "nim": "124140003",
        "nilai_uts": 55,
        "nilai_uas": 62,
        "nilai_tugas": 70,
    },
    {
        "nama": "Dewi Lestari",
        "nim": "124140004",
        "nilai_uts": 80,
        "nilai_uas": 74,
        "nilai_tugas": 78,
    },
    {
        "nama": "Rian Kurniawan",
        "nim": "124140005",
        "nilai_uts": 45,
        "nilai_uas": 50,
        "nilai_tugas": 60,
    },
    {
        "nama": "Eko Wijaya",
        "nim": "124140006",
        "nilai_uts": 68,
        "nilai_uas": 72,
        "nilai_tugas": 75,
    },
]


def hitung_nilai_akhir(mahasiswa: dict[str, Any]) -> float:
    """Menghitung nilai akhir seorang mahasiswa.

    Args:
        mahasiswa (dict): Dictionary berisi kunci nilai_uts, nilai_uas,
            dan nilai_tugas.

    Returns:
        float: Nilai akhir berbobot (30% UTS + 40% UAS + 30% Tugas).
    """
    return (
        BOBOT_UTS * mahasiswa["nilai_uts"]
        + BOBOT_UAS * mahasiswa["nilai_uas"]
        + BOBOT_TUGAS * mahasiswa["nilai_tugas"]
    )


def tentukan_grade(nilai_akhir: float) -> str:
    """Menentukan grade A-E dari nilai akhir.

    Args:
        nilai_akhir (float): Nilai akhir mahasiswa (0-100).

    Returns:
        str: Grade berupa "A", "B", "C", "D", atau "E".
    """
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"


def olah_data(data: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Menambahkan nilai akhir dan grade ke setiap data mahasiswa.

    Args:
        data (list[dict]): Daftar dictionary mahasiswa mentah.

    Returns:
        list[dict]: Salinan data dengan kunci tambahan nilai_akhir dan grade.
    """
    hasil = []
    for mahasiswa in data:
        nilai_akhir = hitung_nilai_akhir(mahasiswa)
        baris = dict(mahasiswa)
        baris["nilai_akhir"] = nilai_akhir
        baris["grade"] = tentukan_grade(nilai_akhir)
        hasil.append(baris)
    return hasil


def cetak_tabel(baris_data: list[dict[str, Any]]) -> None:
    """Mencetak data mahasiswa dalam bentuk tabel rata di terminal.

    Args:
        baris_data (list[dict]): Data mahasiswa yang sudah diolah.

    Returns:
        None
    """
    kolom = [
        ("No", 2, "kiri"),
        ("Nama", 18, "kiri"),
        ("NIM", 11, "kiri"),
        ("UTS", 5, "kanan"),
        ("UAS", 5, "kanan"),
        ("Tugas", 6, "kanan"),
        ("Nilai Akhir", 11, "kanan"),
        ("Grade", 5, "tengah"),
    ]

    def garis(pengisi: str = "-") -> str:
        potongan = []
        for _, lebar, _ in kolom:
            potongan.append(pengisi * (lebar + 2))
        return "+" + "+".join(potongan) + "+"

    def baris_teks(nilai: list[str]) -> str:
        sel = []
        for (_, lebar, rata), isi in zip(kolom, nilai):
            if rata == "kanan":
                sel.append(f" {isi:>{lebar}} ")
            elif rata == "tengah":
                sel.append(f" {isi:^{lebar}} ")
            else:
                sel.append(f" {isi:<{lebar}} ")
        return "|" + "|".join(sel) + "|"

    print(garis("="))
    print(baris_teks([judul for judul, _, _ in kolom]))
    print(garis("="))

    for nomor, mahasiswa in enumerate(baris_data, start=1):
        print(baris_teks([
            str(nomor),
            mahasiswa["nama"],
            mahasiswa["nim"],
            f"{mahasiswa['nilai_uts']:.0f}",
            f"{mahasiswa['nilai_uas']:.0f}",
            f"{mahasiswa['nilai_tugas']:.0f}",
            f"{mahasiswa['nilai_akhir']:.2f}",
            mahasiswa["grade"],
        ]))

    print(garis("-"))


def cari_ekstrem(baris_data: list[dict[str, Any]]) -> tuple[list, list]:
    """Mencari mahasiswa dengan nilai akhir tertinggi dan terendah.

    Args:
        baris_data (list[dict]): Data mahasiswa yang sudah diolah.

    Returns:
        tuple[list, list]: Pasangan (daftar nilai tertinggi, daftar nilai
            terendah). Daftar dipakai agar nilai seri tetap tertangani.
    """
    nilai_tertinggi = max(mahasiswa["nilai_akhir"] for mahasiswa in baris_data)
    nilai_terendah = min(mahasiswa["nilai_akhir"] for mahasiswa in baris_data)

    tertinggi = [m for m in baris_data if m["nilai_akhir"] == nilai_tertinggi]
    terendah = [m for m in baris_data if m["nilai_akhir"] == nilai_terendah]
    return tertinggi, terendah


def main() -> None:
    """Menjalankan alur utama pengolahan nilai mahasiswa."""
    data_olah = olah_data(DATA_MAHASISWA)

    print("=" * 78)
    print("        PENGELOLAAN DATA NILAI MAHASISWA".center(78))
    print("=" * 78)
    print("Bobot: UTS 30% | UAS 40% | Tugas 30%")
    print()

    cetak_tabel(data_olah)

    tertinggi, terendah = cari_ekstrem(data_olah)

    print()
    print("NILAI AKHIR TERTINGGI")
    for mahasiswa in tertinggi:
        print(
            f"  -> {mahasiswa['nama']} ({mahasiswa['nim']}) "
            f"= {mahasiswa['nilai_akhir']:.2f} | Grade {mahasiswa['grade']}"
        )

    print("NILAI AKHIR TERENDAH")
    for mahasiswa in terendah:
        print(
            f"  -> {mahasiswa['nama']} ({mahasiswa['nim']}) "
            f"= {mahasiswa['nilai_akhir']:.2f} | Grade {mahasiswa['grade']}"
        )

    jumlah_lulus = sum(1 for m in data_olah if m["grade"] != "E")
    print()
    print(f"Total mahasiswa : {len(data_olah)} orang")
    print(f"Lulus (A-D)     : {jumlah_lulus} orang")
    print(f"Tidak lulus (E) : {len(data_olah) - jumlah_lulus} orang")
    print("=" * 78)


if __name__ == "__main__":
    main()
