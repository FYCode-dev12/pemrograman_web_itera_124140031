// State untuk keranjang belanja
let cart = JSON.parse(localStorage.getItem('cart')) || [];

// Referensi DOM
const addItemForm = document.getElementById('add-item-form');
const namaBarangInput = document.getElementById('namaBarang');
const hargaSatuanInput = document.getElementById('hargaSatuan');
const qtyInput = document.getElementById('qty');
const cartBody = document.getElementById('cart-body');
const totalBelanjaEl = document.getElementById('total-belanja');
const diskonEl = document.getElementById('diskon');
const totalAkhirEl = document.getElementById('total-akhir');
const btnReset = document.getElementById('btn-reset');
const uangBayarInput = document.getElementById('uangBayar');
const btnBayar = document.getElementById('btn-bayar');
const kembalianEl = document.getElementById('kembalian');
const paymentFeedback = document.getElementById('payment-feedback');

// Fungsi untuk format rupiah
function formatRupiah(number) {
    return new Intl.NumberFormat('id-ID', { style: 'currency', currency: 'IDR' }).format(number);
}

// Fungsi untuk menyimpan ke localStorage
function saveCart() {
    localStorage.setItem('cart', JSON.stringify(cart));
}

// Fungsi merender tabel keranjang dan menghitung total
function renderCart() {
    cartBody.innerHTML = '';
    let totalBelanja = 0;

    cart.forEach((item, index) => {
        const subtotal = item.harga * item.qty;
        totalBelanja += subtotal;

        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${index + 1}</td>
            <td>${item.nama}</td>
            <td>${formatRupiah(item.harga)}</td>
            <td>${item.qty}</td>
            <td>${formatRupiah(subtotal)}</td>
            <td><button class="btn-hapus" data-index="${index}" style="background-color: #dc3545;">Hapus</button></td>
        `;
        cartBody.appendChild(row);
    });

    // Event listener untuk tombol hapus
    const hapusButtons = document.querySelectorAll('.btn-hapus');
    hapusButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            const index = this.getAttribute('data-index');
            hapusItem(index);
        });
    });

    hitungTotal(totalBelanja);
}

// Fungsi menghitung diskon dan total akhir
let totalAkhirState = 0;
function hitungTotal(totalBelanja) {
    totalBelanjaEl.textContent = formatRupiah(totalBelanja);
    
    let diskon = 0;
    if (totalBelanja >= 50000) {
        diskon = totalBelanja * 0.10;
    }
    
    diskonEl.textContent = formatRupiah(diskon);
    
    totalAkhirState = totalBelanja - diskon;
    totalAkhirEl.textContent = formatRupiah(totalAkhirState);

    // Reset payment area whenever total changes
    uangBayarInput.value = '';
    kembalianEl.textContent = 'Rp 0';
    paymentFeedback.textContent = '';
}

// Fungsi hapus item
function hapusItem(index) {
    cart.splice(index, 1);
    saveCart();
    renderCart();
}

// Event handler untuk tambah barang
addItemForm.addEventListener('submit', function(e) {
    e.preventDefault();

    // Reset pesan error
    document.getElementById('error-nama').textContent = '';
    document.getElementById('error-harga').textContent = '';
    document.getElementById('error-qty').textContent = '';

    const nama = namaBarangInput.value.trim();
    const harga = parseFloat(hargaSatuanInput.value);
    const qty = parseInt(qtyInput.value);

    let isValid = true;

    // Validasi Nama Barang (min 3 karakter)
    if (nama.length < 3) {
        document.getElementById('error-nama').textContent = 'Nama barang minimal 3 karakter.';
        isValid = false;
    }

    // Validasi Harga Satuan (angka positif, minimal 500)
    if (isNaN(harga) || harga < 500) {
        document.getElementById('error-harga').textContent = 'Harga satuan minimal Rp 500.';
        isValid = false;
    }

    // Validasi Jumlah / Qty (angka bulat minimal 1)
    if (isNaN(qty) || qty < 1) {
        document.getElementById('error-qty').textContent = 'Jumlah minimal 1.';
        isValid = false;
    }

    if (isValid) {
        cart.push({
            nama: nama,
            harga: harga,
            qty: qty
        });
        saveCart();
        renderCart();
        addItemForm.reset();
    }
});

// Event handler untuk bayar
btnBayar.addEventListener('click', function() {
    const uangBayar = parseFloat(uangBayarInput.value);
    
    if (isNaN(uangBayar)) {
        paymentFeedback.textContent = 'Masukkan nominal uang yang valid.';
        paymentFeedback.style.color = 'red';
        kembalianEl.textContent = 'Rp 0';
        return;
    }

    if (uangBayar < totalAkhirState) {
        paymentFeedback.textContent = 'Uang belum mencukupi.';
        paymentFeedback.style.color = 'red';
        kembalianEl.textContent = 'Rp 0';
    } else {
        const kembalian = uangBayar - totalAkhirState;
        paymentFeedback.textContent = 'Pembayaran berhasil.';
        paymentFeedback.style.color = 'green';
        kembalianEl.textContent = formatRupiah(kembalian);
    }
});

// Event handler untuk reset
btnReset.addEventListener('click', function() {
    if(confirm('Apakah Anda yakin ingin memulai transaksi baru? Semua data keranjang akan dihapus.')) {
        cart = [];
        localStorage.removeItem('cart');
        renderCart();
    }
});

// Inisialisasi awal
renderCart();
