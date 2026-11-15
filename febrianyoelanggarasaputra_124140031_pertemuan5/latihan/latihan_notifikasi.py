# ==============================================================================
# Berkas: latihan_notifikasi.py
# Deskripsi: Latihan Mandiri 5 - Engine Dispatcher Multi-Saluran Notifikasi (Polymorphism)
# Praktikan: Febrian Yoel Anggara Saputra (124140031) - Kelas RB
# Praktikum Pengembangan Aplikasi Web - Pertemuan 5
# ==============================================================================

class NotifikasiEmail:
    """Channel pengiriman notifikasi berbasis protokol SMTP Surel (Email)."""

    def __init__(self, smtp_server: str = "smtp.itera.ac.id"):
        self.smtp_server = smtp_server
        self.nama_channel = "Email Gateway"

    def kirim(self, pesan: str, penerima: str) -> bool:
        """Mengirim surel ke alamat email tujuan."""
        print(f"[{self.nama_channel}] Menghubungkan ke server {self.smtp_server}...")
        print(f" -> Kepada : <{penerima}>")
        print(f" -> Subjek : Pemberitahuan Sistem Web")
        print(f" -> Isi    : \"{pesan}\"")
        print(f" -> Status : TERKIRIM (250 OK - Message accepted for delivery)\n")
        return True


class NotifikasiSMS:
    """Channel pengiriman pesan singkat seluler via SMS Gateway Telco."""

    def __init__(self, provider: str = "Telkomsel"):
        self.provider = provider
        self.nama_channel = f"SMS Gateway ({self.provider})"

    def kirim(self, pesan: str, penerima: str) -> bool:
        """Mengirim pesan teks ke nomor ponsel seluler."""
        # Memotong pesan jika lebih dari 160 karakter standar SMS
        teks_sms = pesan[:157] + "..." if len(pesan) > 160 else pesan
        print(f"[{self.nama_channel}] Mengirim pesan GSM...")
        print(f" -> No. HP : {penerima}")
        print(f" -> Pesan  : \"{teks_sms}\"")
        print(f" -> Status : TERKIRIM (SMS Delivered via GSM BTS)\n")
        return True


class NotifikasiWhatsApp:
    """Channel pengiriman pesan instan via WhatsApp Business Cloud API."""

    def __init__(self, api_version: str = "v18.0"):
        self.api_version = api_version
        self.nama_channel = "WhatsApp Business API"

    def kirim(self, pesan: str, penerima: str) -> bool:
        """Mengirim pesan terenkripsi ke nomor WhatsApp tujuan."""
        print(f"[{self.nama_channel}] Mengirim pesan REST API {self.api_version}...")
        print(f" -> Akun WA: https://wa.me/{penerima}")
        print(f" -> Pesan  : \"{pesan}\"")
        print(f" -> Status : TERKIRIM (WhatsApp Message Sent [status: read])\n")
        return True


# ------------------------------------------------------------------------------
# FUNGSI DISPATCHER POLIMORFIK (Duck Typing / Polymorphism)
# ------------------------------------------------------------------------------
def broadcast_pengumuman(daftar_channel: list, pesan: str, kontak_tujuan: dict = None) -> int:
    """Mengirim pesan siaran darurat ke seluruh kanal notifikasi secara heterogen.

    Fungsi ini tidak peduli apakah objek bertipe Email, SMS, atau WhatsApp,
    selama objek tersebut mematuhi kontrak method kirim(pesan, penerima).

    Args:
        daftar_channel (list): Koleksi objek pengirim pesan heterogen.
        pesan (str): Isi pesan pengumuman / darurat.
        kontak_tujuan (dict): Pemetaan channel ke kontak tujuan spesifik (opsional).

    Returns:
        int: Jumlah kanal yang berhasil memproses pengiriman.
    """
    print("\n" + "=" * 68)
    print("        DISPATCHER SIARAN PENGUMUMAN MULTI-KANAL (BROADCAST)")
    print("=" * 68)
    print(f"Pesan Siaran: \"{pesan}\"")
    print(f"Total Kanal Siaran: {len(daftar_channel)} channel")
    print("-" * 68 + "\n")

    sukses_count = 0
    default_kontak = {
        "Email Gateway": "mahasiswa.paw@itera.ac.id",
        "SMS Gateway": "+6281234567890",
        "WhatsApp Business API": "6281234567890"
    }

    for idx, channel in enumerate(daftar_channel, 1):
        nama = getattr(channel, "nama_channel", type(channel).__name__)
        # Menentukan penerima yang sesuai
        if kontak_tujuan and nama in kontak_tujuan:
            penerima = kontak_tujuan[nama]
        elif "SMS" in nama:
            penerima = "+6281234567890"
        elif "Email" in nama:
            penerima = "febrian.124140031@student.itera.ac.id"
        else:
            penerima = "6281234567890"

        print(f"--- [Channel {idx}/{len(daftar_channel)}: {nama}] ---")
        try:
            # PEMANGGILAN POLIMORFIK: Duck Typing seragam
            if channel.kirim(pesan, penerima):
                sukses_count += 1
        except Exception as err:
            print(f"Gagal mengirim via {nama}: {err}\n")

    print("-" * 68)
    print(f"Rekap Siaran: {sukses_count}/{len(daftar_channel)} kanal berhasil terdistribusi.")
    print("=" * 68 + "\n")
    return sukses_count


# --- DEMONSTRASI EKSEKUSI ---
if __name__ == "__main__":
    print("====================================================================")
    print("LATIHAN MANDIRI 5: ENGINE DISPATCHER NOTIFIKASI (POLYMORPHISM)")
    print("Praktikan: Febrian Yoel Anggara Saputra (124140031) - Kelas RB")
    print("====================================================================")

    # 1. Inisialisasi masing-masing service pengiriman
    email_service = NotifikasiEmail(smtp_server="smtp.itera.ac.id")
    sms_service = NotifikasiSMS(provider="Telkomsel Orbit")
    wa_service = NotifikasiWhatsApp(api_version="v18.0")

    # 2. Uji coba pengiriman individual
    print("\n--- Pengujian Pengiriman Satu Per Satu ---")
    email_service.kirim(
        pesan="Selamat, akun praktikum PAW Anda telah aktif.",
        penerima="febrian.124140031@student.itera.ac.id"
    )

    # 3. Pengujian Broadcast Siaran Darurat ke Seluruh Channel
    semua_channel = [email_service, sms_service, wa_service]
    pesan_darurat = "PERINGATAN: Server Lab Praktikum akan mengalami pemeliharaan rutin pada pukul 23:00 WIB."

    broadcast_pengumuman(semua_channel, pesan_darurat)

