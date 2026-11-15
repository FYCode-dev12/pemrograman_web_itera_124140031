# ==============================================================================
# Berkas: latihan_storage.py
# Deskripsi: Latihan Mandiri 6 - Interface File Storage Service (Abstract Base Class)
# Praktikan: Febrian Yoel Anggara Saputra (124140031) - Kelas RB
# Praktikum Pengembangan Aplikasi Web - Pertemuan 5
# ==============================================================================

from abc import ABC, abstractmethod
import datetime


class FileStorage(ABC):
    """Abstract Base Class (Interface) untuk layanan penyimpanan berkas berkas aplikasi web."""

    def __init__(self, nama_storage: str):
        self.nama_storage = nama_storage

    @abstractmethod
    def upload_file(self, nama_file: str, data_bytes: bytes) -> bool:
        """Mengunggah berkas biner ke media penyimpanan."""
        pass

    @abstractmethod
    def download_file(self, nama_file: str) -> bytes | None:
        """Mengunduh berkas biner dari media penyimpanan berdasarkan nama berkas."""
        pass

    def info_penyimpanan(self) -> None:
        """Concrete method: menampilkan identitas jenis media penyimpanan."""
        print(f"[Storage Service] Menggunakan engine: {self.nama_storage}")


class LocalDiskStorage(FileStorage):
    """Implementasi konkrit penyimpanan lokal hard disk / storage server lokal."""

    def __init__(self, direktori_dasar: str = "/var/www/uploads"):
        super().__init__("Local Disk Storage System")
        self.direktori_dasar = direktori_dasar
        # Simulasi filesystem in-memory {nama_file: data_bytes}
        self.__disk_virtual = {}

    def upload_file(self, nama_file: str, data_bytes: bytes) -> bool:
        path_lengkap = f"{self.direktori_dasar}/{nama_file}"
        self.__disk_virtual[nama_file] = data_bytes
        ukuran_kb = len(data_bytes) / 1024
        print(f"[{self.nama_storage}] Menulis {nama_file} ({ukuran_kb:.2f} KB) ke {path_lengkap} -> [OK]")
        return True

    def download_file(self, nama_file: str) -> bytes | None:
        if nama_file in self.__disk_virtual:
            print(f"[{self.nama_storage}] Membaca berkas {nama_file} dari disk lokal -> [FOUND]")
            return self.__disk_virtual[nama_file]
        print(f"[{self.nama_storage}] Berkas {nama_file} tidak ditemukan di disk lokal! -> [404]")
        return None


class CloudStorage(FileStorage):
    """Implementasi konkrit penyimpanan objek berbasis Cloud (GCS / AWS S3)."""

    def __init__(self, bucket_name: str, region: str = "asia-southeast2"):
        super().__init__("Google Cloud Storage (GCS)")
        self.bucket_name = bucket_name
        self.region = region
        # Simulasi cloud object store {nama_file: {'data': bytes, 'time': datetime}}
        self.__cloud_objects = {}

    def upload_file(self, nama_file: str, data_bytes: bytes) -> bool:
        ukuran_kb = len(data_bytes) / 1024
        self.__cloud_objects[nama_file] = {
            "data": data_bytes,
            "uploaded_at": datetime.datetime.now()
        }
        cloud_uri = f"gs://{self.bucket_name}/{nama_file}"
        print(f"[{self.nama_storage}] Mengunggah objek ke bucket '{self.bucket_name}' ({self.region})")
        print(f" -> URI Cloud: {cloud_uri} ({ukuran_kb:.2f} KB) -> [UPLOAD SUCCESS 200 OK]")
        return True

    def download_file(self, nama_file: str) -> bytes | None:
        if nama_file in self.__cloud_objects:
            obj = self.__cloud_objects[nama_file]
            print(f"[{self.nama_storage}] Mengunduh {nama_file} dari bucket {self.bucket_name} -> [OK 200]")
            return obj["data"]
        print(f"[{self.nama_storage}] Error: Objek '{nama_file}' tidak ditemukan di bucket '{self.bucket_name}' -> [404]")
        return None


# ------------------------------------------------------------------------------
# FUNGSI BACKUP POLIMORFIK
# ------------------------------------------------------------------------------
def backup_dokumen(storage: FileStorage, nama_berkas: str, konten: bytes):
    """Fungsi backend yang berinteraksi secara independen terhadap implementasi storage."""
    print(f"\n--- Memulai Alur Backup: {nama_berkas} ---")
    storage.info_penyimpanan()
    storage.upload_file(nama_berkas, konten)
    konten_unduhan = storage.download_file(nama_berkas)
    if konten_unduhan:
        print(f"Verifikasi Integritas: {len(konten_unduhan)} bytes berhasil terbaca kembali.")


# --- DEMONSTRASI EKSEKUSI ---
if __name__ == "__main__":
    print("====================================================================")
    print("LATIHAN MANDIRI 6: INTERFACE FILE STORAGE SERVICE (ABSTRACT CLASS)")
    print("Praktikan: Febrian Yoel Anggara Saputra (124140031) - Kelas RB")
    print("====================================================================")

    # 1. Pembuktian Penolakan Instansiasi Langsung Abstract Class
    print("\n--- 1. Pembuktian Enforcement Abstract Class ---")
    try:
        storage_abstrak = FileStorage("Abstract Driver")
    except TypeError as err:
        print(f"Enforcement Berhasil! Python menolak instansiasi langsung:\n -> {err}")

    # 2. Inisialisasi Dua Implementasi Konkrit
    local_storage = LocalDiskStorage(direktori_dasar="/home/itera/web_app/static/media")
    cloud_storage = CloudStorage(bucket_name="paw-praktikum-2026-bucket", region="asia-southeast2")

    # 3. Data berkas simulasi
    dokumen_data = b"Laporan Praktikum Pemrograman Aplikasi Web Pertemuan 5 - ITERA 2026."

    # 4. Uji Coba Backup ke Local Storage
    backup_dokumen(local_storage, "laporan_prak5.pdf", dokumen_data)

    # 5. Uji Coba Backup ke Cloud Storage
    backup_dokumen(cloud_storage, "laporan_prak5.pdf", dokumen_data)

    # 6. Uji Kasus Berkas Hilang
    print("\n--- Pengujian Berkas Tidak Ditemukan ---")
    local_storage.download_file("file_gaib.docx")
    cloud_storage.download_file("file_gaib.docx")

