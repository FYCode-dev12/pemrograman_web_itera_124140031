// ==========================================
// LATIHAN VARIABEL & KONDISIONAL
// ==========================================
const namaDiri = "Febrian Yoel Anggara Saputra";
let umurDiri = 20;
let kotaAsal = "Jakarta";

const divKondisional = document.getElementById('hasil-kondisional');

// Cek kelulusan
let nilaiKelulusan = 75;
let statusLulus = nilaiKelulusan >= 70 ? "Lulus" : "Tidak Lulus";

// Cek kategori umur
let kategoriUmur = "";
if (umurDiri < 12) kategoriUmur = "Anak";
else if (umurDiri >= 12 && umurDiri <= 17) kategoriUmur = "Remaja";
else if (umurDiri >= 18 && umurDiri <= 59) kategoriUmur = "Dewasa";
else kategoriUmur = "Lansia";

// Konversi hari
let angkaHari = new Date().getDay() || 7; // 1-7
let namaHariInggris = "";
switch (angkaHari) {
    case 1: namaHariInggris = "Monday"; break;
    case 2: namaHariInggris = "Tuesday"; break;
    case 3: namaHariInggris = "Wednesday"; break;
    case 4: namaHariInggris = "Thursday"; break;
    case 5: namaHariInggris = "Friday"; break;
    case 6: namaHariInggris = "Saturday"; break;
    case 7: namaHariInggris = "Sunday"; break;
}

divKondisional.innerHTML = `
    <p>Nama: ${namaDiri}, Umur: ${umurDiri} (${kategoriUmur}), Asal: ${kotaAsal}</p>
    <p>Nilai: ${nilaiKelulusan} -> ${statusLulus}</p>
    <p>Hari ini (1-7): ${angkaHari} -> ${namaHariInggris}</p>
`;

// ==========================================
// LATIHAN LOOP & FUNGSI
// ==========================================
const divLoop = document.getElementById('hasil-loop-fungsi');

// Tabel perkalian 10
let tabelPerkalian = "<strong>Perkalian 10:</strong><br>";
for (let i = 1; i <= 10; i++) {
    tabelPerkalian += `10 x ${i} = ${10 * i}<br>`;
}

// Fungsi faktorial
function faktorial(n) {
    if (n === 0 || n === 1) return 1;
    return n * faktorial(n - 1);
}

// Fungsi cek prima
function isPrima(n) {
    if (n < 2) return false;
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) return false;
    }
    return true;
}

// Kalkulator BMI
function hitungBMI(beratKg, tinggiM) {
    return (beratKg / (tinggiM * tinggiM)).toFixed(2);
}

divLoop.innerHTML = `
    <p>${tabelPerkalian}</p>
    <p>Faktorial 5: ${faktorial(5)}</p>
    <p>Apakah 7 prima? ${isPrima(7)}</p>
    <p>BMI (70kg, 1.75m): ${hitungBMI(70, 1.75)}</p>
    <p><strong>FizzBuzz (cek console log)</strong></p>
`;

// FizzBuzz 1-100 (Console)
for (let i = 1; i <= 100; i++) {
    if (i % 15 === 0) console.log("FizzBuzz");
    else if (i % 3 === 0) console.log("Fizz");
    else if (i % 5 === 0) console.log("Buzz");
    // else console.log(i); // Commented to save console space
}


// ==========================================
// LATIHAN ARRAY & OBJEK
// ==========================================
let mahasiswa = [
    { nama: "Andi", nim: "101", jurusan: "IF", nilai: 85 },
    { nama: "Budi", nim: "102", jurusan: "IF", nilai: 95 },
    { nama: "Citra", nim: "103", jurusan: "SI", nilai: 70 },
    { nama: "Dewi", nim: "104", jurusan: "SI", nilai: 88 },
    { nama: "Eka", nim: "105", jurusan: "IF", nilai: 60 }
];

function cariNilaiTertinggi(arr) {
    return arr.reduce((prev, current) => (prev.nilai > current.nilai) ? prev : current);
}

let rataRata = mahasiswa.reduce((sum, mhs) => sum + mhs.nilai, 0) / mahasiswa.length;
let diAtasRata = mahasiswa.filter(mhs => mhs.nilai > rataRata);

// Sort berdasarkan nama (ascending)
mahasiswa.sort((a, b) => a.nama.localeCompare(b.nama));

const divTabel = document.getElementById('tabel-mahasiswa');
let tableHTML = `<table><tr><th>Nama</th><th>NIM</th><th>Jurusan</th><th>Nilai</th></tr>`;
mahasiswa.forEach(mhs => {
    tableHTML += `<tr><td>${mhs.nama}</td><td>${mhs.nim}</td><td>${mhs.jurusan}</td><td>${mhs.nilai}</td></tr>`;
});
tableHTML += `</table>`;
divTabel.innerHTML = tableHTML;

document.getElementById('info-mahasiswa').innerHTML = `
    <p><strong>Nilai Tertinggi:</strong> ${cariNilaiTertinggi(mahasiswa).nama} (${cariNilaiTertinggi(mahasiswa).nilai})</p>
    <p><strong>Rata-rata:</strong> ${rataRata.toFixed(2)}</p>
    <p><strong>Di atas rata-rata:</strong> ${diAtasRata.map(m => m.nama).join(", ")}</p>
`;

// ==========================================
// LATIHAN DOM, API, TODO
// ==========================================

// Todo List dengan LocalStorage
let todos = JSON.parse(localStorage.getItem('todos')) || [];
const formTodo = document.getElementById('form-todo');
const inputTodo = document.getElementById('input-todo');
const todoList = document.getElementById('todo-list');

function renderTodos() {
    todoList.innerHTML = '';
    todos.forEach((todo, index) => {
        const li = document.createElement('li');
        li.className = todo.completed ? 'completed' : '';
        li.innerHTML = `
            <span onclick="toggleTodo(${index})" style="cursor:pointer">${todo.text}</span>
            <button onclick="deleteTodo(${index})">Hapus</button>
        `;
        todoList.appendChild(li);
    });
}

window.toggleTodo = function(index) {
    todos[index].completed = !todos[index].completed;
    localStorage.setItem('todos', JSON.stringify(todos));
    renderTodos();
}

window.deleteTodo = function(index) {
    todos.splice(index, 1);
    localStorage.setItem('todos', JSON.stringify(todos));
    renderTodos();
}

formTodo.addEventListener('submit', (e) => {
    e.preventDefault();
    if(inputTodo.value.trim() !== '') {
        todos.push({ text: inputTodo.value, completed: false });
        localStorage.setItem('todos', JSON.stringify(todos));
        inputTodo.value = '';
        renderTodos();
    }
});
renderTodos();

// Fetch API Pagination & Filter
const postsContainer = document.getElementById('posts-container');
const searchPost = document.getElementById('search-post');
const btnPrev = document.getElementById('prev-page');
const btnNext = document.getElementById('next-page');
const pageInfo = document.getElementById('page-info');

let allPosts = [];
let currentPage = 1;
const limit = 5;

async function fetchPosts() {
    try {
        const res = await fetch('https://jsonplaceholder.typicode.com/posts');
        allPosts = await res.json();
        renderPosts();
    } catch(err) {
        postsContainer.innerHTML = '<p style="color:red">Error fetching API</p>';
    }
}

function renderPosts() {
    const searchTerm = searchPost.value.toLowerCase();
    const filteredPosts = allPosts.filter(p => p.title.toLowerCase().includes(searchTerm));
    
    const start = (currentPage - 1) * limit;
    const end = start + limit;
    const paginated = filteredPosts.slice(start, end);

    pageInfo.innerText = `Halaman ${currentPage}`;
    
    postsContainer.innerHTML = '';
    paginated.forEach(post => {
        postsContainer.innerHTML += `<div><h4>${post.title}</h4><p>${post.body}</p></div>`;
    });
}

searchPost.addEventListener('input', () => {
    currentPage = 1;
    renderPosts();
});

btnPrev.addEventListener('click', () => {
    if(currentPage > 1) { currentPage--; renderPosts(); }
});

btnNext.addEventListener('click', () => {
    const searchTerm = searchPost.value.toLowerCase();
    const filteredPosts = allPosts.filter(p => p.title.toLowerCase().includes(searchTerm));
    if(currentPage * limit < filteredPosts.length) { currentPage++; renderPosts(); }
});

fetchPosts();
