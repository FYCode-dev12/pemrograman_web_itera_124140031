import { API_ENDPOINTS } from './modules/data.js';
import { escapeHtml, formatDate, formatShortDate } from './modules/utils.js';

const STORAGE_KEY = 'studyflow_tasks_v1';

export class TaskItem {
    constructor({ id = crypto.randomUUID(), title, category = 'Kuliah', dueDate, priority = 'medium', completed = false }) {
        Object.assign(this, { id, title, category, dueDate, priority, completed });
    }
}

export class DashboardApp {
    constructor() {
        this.tasks = this.loadTasks();
        this.filter = 'all';
        this.query = '';
        this.cacheDom();
        this.bindEvents();
        this.render();
        this.loadExternalData();
    }

    cacheDom() {
        this.dom = {
            form: document.querySelector('#task-form'), title: document.querySelector('#task-title'), category: document.querySelector('#task-category'), due: document.querySelector('#task-due'), editingId: document.querySelector('#editing-id'), taskList: document.querySelector('#task-list'), empty: document.querySelector('#empty-state'), taskCount: document.querySelector('#task-count'), completed: document.querySelector('#completed-count'), completedCaption: document.querySelector('#completed-caption'), pending: document.querySelector('#pending-count'), search: document.querySelector('#search-input'), formTitle: document.querySelector('#form-title'), cancelEdit: document.querySelector('#cancel-edit'), quote: document.querySelector('#quote-text'), author: document.querySelector('#quote-author'), temperature: document.querySelector('#weather-temperature'), condition: document.querySelector('#weather-condition'), wind: document.querySelector('#weather-wind')
        };
    }

    bindEvents() {
        this.dom.form.addEventListener('submit', (event) => { event.preventDefault(); this.saveTask(); });
        this.dom.cancelEdit.addEventListener('click', () => this.resetForm());
        this.dom.search.addEventListener('input', ({ target }) => { this.query = target.value.toLowerCase(); this.renderTasks(); });
        document.querySelector('#focus-add-task').addEventListener('click', () => { this.dom.title.focus(); document.querySelector('#add-panel').scrollIntoView({ behavior: 'smooth', block: 'center' }); });
        document.querySelector('#refresh-quote').addEventListener('click', () => this.fetchQuote());
        document.querySelectorAll('.filter-tab').forEach((button) => button.addEventListener('click', () => { this.filter = button.dataset.filter; document.querySelectorAll('.filter-tab').forEach((tab) => tab.classList.toggle('active', tab === button)); this.renderTasks(); }));
        this.dom.taskList.addEventListener('click', (event) => { const action = event.target.closest('[data-action]'); if (!action) return; const { action: type, id } = action.dataset; if (type === 'delete') this.deleteTask(id); if (type === 'edit') this.editTask(id); });
        this.dom.taskList.addEventListener('change', (event) => { if (event.target.matches('.task-check')) this.toggleTask(event.target.dataset.id); });
    }

    loadTasks() { try { return JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]').map((task) => new TaskItem(task)); } catch { return []; } }
    persist() { localStorage.setItem(STORAGE_KEY, JSON.stringify(this.tasks)); }

    saveTask() {
        const title = this.dom.title.value.trim();
        if (!title || !this.dom.due.value) return;
        const priority = document.querySelector('input[name="priority"]:checked').value;
        const taskData = { title, category: this.dom.category.value, dueDate: this.dom.due.value, priority };
        const id = this.dom.editingId.value;
        this.tasks = id ? this.tasks.map((task) => task.id === id ? new TaskItem({ ...task, ...taskData }) : task) : [...this.tasks, new TaskItem(taskData)];
        this.persist(); this.resetForm(); this.render();
    }

    toggleTask(id) { this.tasks = this.tasks.map((task) => task.id === id ? new TaskItem({ ...task, completed: !task.completed }) : task); this.persist(); this.render(); }
    deleteTask(id) { this.tasks = this.tasks.filter(({ id: taskId }) => taskId !== id); this.persist(); this.render(); }

    editTask(id) {
        const task = this.tasks.find(({ id: taskId }) => taskId === id); if (!task) return;
        this.dom.editingId.value = task.id; this.dom.title.value = task.title; this.dom.category.value = task.category; this.dom.due.value = task.dueDate; document.querySelector(`input[name="priority"][value="${task.priority}"]`).checked = true; this.dom.formTitle.textContent = 'Edit tugas'; this.dom.cancelEdit.hidden = false; this.dom.title.focus(); document.querySelector('#add-panel').scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    resetForm() { this.dom.form.reset(); this.dom.editingId.value = ''; this.dom.formTitle.textContent = 'Tugas baru'; this.dom.cancelEdit.hidden = true; document.querySelector('input[name="priority"][value="medium"]').checked = true; }
    getVisibleTasks() { return this.tasks.filter(({ title, completed }) => { const statusMatch = this.filter === 'all' || (this.filter === 'active' && !completed) || (this.filter === 'completed' && completed); return statusMatch && title.toLowerCase().includes(this.query); }); }
    render() { document.querySelector('#current-date').textContent = formatDate(new Date()); this.renderStats(); this.renderTasks(); }

    renderStats() { const completed = this.tasks.filter(({ completed }) => completed).length; const pending = this.tasks.length - completed; this.dom.completed.textContent = completed; this.dom.pending.textContent = pending; this.dom.completedCaption.textContent = `dari ${this.tasks.length} tugas`; this.dom.taskCount.textContent = `${this.tasks.length} tugas`; }

    renderTasks() {
        const tasks = this.getVisibleTasks(); this.dom.empty.hidden = tasks.length > 0; this.dom.taskList.innerHTML = tasks.map((task) => `
            <article class="task-item ${task.completed ? 'done' : ''}">
                <input class="task-check" type="checkbox" data-id="${task.id}" ${task.completed ? 'checked' : ''} aria-label="Tandai ${escapeHtml(task.title)} selesai">
                <div class="task-info"><p class="task-title">${escapeHtml(task.title)}</p><div class="task-meta"><span class="category">${escapeHtml(task.category)}</span><span>Deadline: ${formatShortDate(task.dueDate)}</span><span class="priority ${task.priority}" title="Prioritas ${task.priority}"></span></div></div>
                <div class="task-actions"><button class="icon-button" data-action="edit" data-id="${task.id}" aria-label="Edit tugas">Edit</button><button class="icon-button" data-action="delete" data-id="${task.id}" aria-label="Hapus tugas">Hapus</button></div>
            </article>`).join('');
    }

    async loadExternalData() { await Promise.allSettled([this.fetchQuote(), this.fetchWeather()]); }
    async fetchQuote() { try { const response = await fetch(API_ENDPOINTS.quote); if (!response.ok) throw new Error('Quote request failed'); const { quote, author } = await response.json(); this.dom.quote.textContent = quote; this.dom.author.textContent = `— ${author}`; } catch { this.dom.quote.textContent = 'Konsistensi kecil setiap hari menghasilkan perubahan besar.'; this.dom.author.textContent = '— StudyFlow'; } }
    async fetchWeather() { try { const response = await fetch(API_ENDPOINTS.weather); if (!response.ok) throw new Error('Weather request failed'); const { current_weather: weather } = await response.json(); this.dom.temperature.textContent = `${Math.round(weather.temperature)}°C`; this.dom.condition.textContent = 'Cerah / kondisi lokal'; this.dom.wind.textContent = `${weather.windspeed} km/j`; } catch { this.dom.condition.textContent = 'Data tidak tersedia'; } }
}
