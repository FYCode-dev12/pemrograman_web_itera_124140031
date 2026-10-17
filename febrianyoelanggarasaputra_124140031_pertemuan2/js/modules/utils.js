export const formatDate = (date) => new Intl.DateTimeFormat('id-ID', { day: 'numeric', month: 'long', year: 'numeric' }).format(date);

export const formatShortDate = (dateString) => {
    const date = new Date(`${dateString}T00:00:00`);
    return Number.isNaN(date.getTime()) ? 'Tanpa deadline' : new Intl.DateTimeFormat('id-ID', { day: 'numeric', month: 'short' }).format(date);
};

export const escapeHtml = (value) => String(value).replace(/[&<>'"]/g, (character) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#039;', '"': '&quot;' }[character]));
