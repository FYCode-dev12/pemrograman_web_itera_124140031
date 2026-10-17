export const demoVariables = () => {
    let status = 'aktif';
    const student = { name: 'Febrian Yoel', semester: 5 };
    status = 'belajar';
    student.focus = 'JavaScript Next Gen';
    return { status, student };
};

export const demoTemplateLiterals = (student, taskCount) => `Halo, ${student.name}! Kamu memiliki ${taskCount} tugas aktif.`;

export const demoDestructuring = ({ name, focus = 'belajar' }) => ({ name, focus });

export const demoSpreadRest = (tasks, ...newTasks) => [...tasks, ...newTasks];

export const demoArrayMethods = (tasks) => ({
    titles: tasks.map(({ title }) => title),
    active: tasks.filter(({ completed }) => !completed),
    first: tasks.find(({ completed }) => !completed),
    total: tasks.reduce((sum) => sum + 1, 0),
    hasCompleted: tasks.some(({ completed }) => completed),
    allHaveTitle: tasks.every(({ title }) => Boolean(title))
});
