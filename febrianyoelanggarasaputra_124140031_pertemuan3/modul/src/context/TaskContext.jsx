import React, { createContext, useContext } from 'react';
import PropTypes from 'prop-types';
import useLocalStorage from '../hooks/useLocalStorage';

const TaskContext = createContext();

export function useTasks() {
  const context = useContext(TaskContext);
  if (!context) {
    throw new Error('useTasks harus digunakan di dalam TaskProvider');
  }
  return context;
}

export function TaskProvider({ children }) {
  const [tasks, setTasks] = useLocalStorage('tasks_data', [
    { id: 1, title: 'Mempelajari Komponen dan Props React', completed: true },
    { id: 2, title: 'Eksplorasi useState dan useEffect Hooks', completed: false },
    { id: 3, title: 'Implementasi Global State Context API', completed: false }
  ]);

  const addTask = (newTask) => {
    setTasks([...tasks, newTask]);
  };

  const deleteTask = (taskId) => {
    setTasks(tasks.filter((t) => t.id !== taskId));
  };

  const toggleComplete = (taskId) => {
    setTasks(
      tasks.map((t) => (t.id === taskId ? { ...t, completed: !t.completed } : t))
    );
  };

  const clearAllTasks = () => {
    setTasks([]);
  };

  const completedCount = tasks.filter((t) => t.completed).length;

  const value = {
    tasks,
    setTasks,
    addTask,
    deleteTask,
    toggleComplete,
    clearAllTasks,
    stats: {
      total: tasks.length,
      completed: completedCount,
      remaining: tasks.length - completedCount,
      completionRate: tasks.length > 0 ? (completedCount / tasks.length) * 100 : 0,
    },
  };

  return <TaskContext.Provider value={value}>{children}</TaskContext.Provider>;
}

TaskProvider.propTypes = {
  children: PropTypes.node.isRequired,
};
