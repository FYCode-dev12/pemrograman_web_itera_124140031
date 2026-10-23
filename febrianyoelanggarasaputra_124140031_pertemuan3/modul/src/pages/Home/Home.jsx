import React from 'react';
import Header from '../../components/Header/Header';
import Card from '../../components/Card/Card';
import TaskForm from '../../components/TaskForm/TaskForm';
import TaskItem from '../../components/TaskItem/TaskItem';
import { useTasks } from '../../context/TaskContext';
import useWindowSize from '../../hooks/useWindowSize';
import './Home.css';

function Home() {
  const { tasks, addTask, deleteTask, toggleComplete, clearAllTasks, stats } = useTasks();
  const { width } = useWindowSize();

  const handleClearAll = () => {
    if (window.confirm('Apakah Anda yakin ingin menghapus semua tugas?')) {
      clearAllTasks();
    }
  };

  return (
    <div className="home">
      <Header
        title="React Task Manager"
        description="Kelola tugas harian Anda secara terstruktur dengan State & Context API"
      />

      <main className="container">
        {/* Latihan Mandiri 4: useWindowSize badge */}
        <div className="responsive-badge-container">
          <span className={`device-badge ${width < 768 ? 'badge-mobile' : 'badge-desktop'}`}>
            {width < 768 ? 'Mode Layar Mobile' : 'Mode Layar Desktop'} ({width}px)
          </span>
        </div>

        {/* Panel Statistik & Latihan Mandiri 2: Tombol Bersihkan Semua */}
        <div className="stats-panel">
          <div className="stats-info">
            <p>Total: <strong>{stats.total}</strong></p>
            <p>Selesai: <strong style={{ color: '#10b981' }}>{stats.completed}</strong></p>
            <p>Belum Selesai: <strong style={{ color: '#ef4444' }}>{stats.remaining}</strong></p>
            <p>Progress: <strong>{stats.completionRate.toFixed(0)}%</strong></p>
          </div>
          {tasks.length > 0 && (
            <button className="clear-all-btn" onClick={handleClearAll}>
              Hapus Semua Tugas
            </button>
          )}
        </div>

        {/* Latihan Mandiri 1: Card dengan Children Props membungkus TaskForm */}
        <Card title="Tambah Tugas Baru">
          <TaskForm onAddTask={addTask} />
        </Card>

        <div className="task-list">
          {tasks.length === 0 ? (
            <p className="empty-message">Belum ada tugas. Tambahkan tugas baru di atas!</p>
          ) : (
            tasks.map((task) => (
              <TaskItem
                key={task.id}
                task={task}
                onDelete={deleteTask}
                onToggleComplete={toggleComplete}
              />
            ))
          )}
        </div>
      </main>
    </div>
  );
}

export default Home;
