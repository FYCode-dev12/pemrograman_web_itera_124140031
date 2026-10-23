import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './BookForm.css';

function BookForm({ onSubmit, initialData = null, onCancel = null, submitButtonText = 'Simpan Buku' }) {
  const [formData, setFormData] = useState({
    title: '',
    author: '',
    status: 'milik',
    year: '',
    category: '',
    notes: '',
  });

  const [errors, setErrors] = useState({});
  const [touched, setTouched] = useState({});

  useEffect(() => {
    if (initialData) {
      setFormData({
        title: initialData.title || '',
        author: initialData.author || '',
        status: initialData.status || 'milik',
        year: initialData.year || '',
        category: initialData.category || '',
        notes: initialData.notes || '',
      });
      setErrors({});
    }
  }, [initialData]);

  // Validasi form
  const validate = (data) => {
    const newErrors = {};
    if (!data.title || !data.title.trim()) {
      newErrors.title = 'Judul buku wajib diisi!';
    } else if (data.title.trim().length < 2) {
      newErrors.title = 'Judul buku minimal 2 karakter.';
    }

    if (!data.author || !data.author.trim()) {
      newErrors.author = 'Nama penulis wajib diisi!';
    }

    if (data.year && (isNaN(data.year) || data.year < 1500 || data.year > 2100)) {
      newErrors.year = 'Tahun harus berupa 4 digit angka yang valid.';
    }

    return newErrors;
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));

    if (touched[name]) {
      const fieldErrors = validate({ ...formData, [name]: value });
      setErrors((prev) => ({ ...prev, [name]: fieldErrors[name] }));
    }
  };

  const handleBlur = (e) => {
    const { name } = e.target;
    setTouched((prev) => ({ ...prev, [name]: true }));
    const formErrors = validate(formData);
    setErrors(formErrors);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setTouched({ title: true, author: true, year: true });
    const validationErrors = validate(formData);
    setErrors(validationErrors);

    if (Object.keys(validationErrors).length > 0) {
      return;
    }

    onSubmit({
      ...formData,
      title: formData.title.trim(),
      author: formData.author.trim(),
      year: formData.year ? parseInt(formData.year, 10) : null,
      category: formData.category.trim(),
      notes: formData.notes.trim(),
    });

    if (!initialData) {
      setFormData({
        title: '',
        author: '',
        status: 'milik',
        year: '',
        category: '',
        notes: '',
      });
      setTouched({});
      setErrors({});
    }
  };

  return (
    <form className="book-form" onSubmit={handleSubmit} noValidate>
      {/* Input Judul Buku */}
      <div className={`form-group ${errors.title && touched.title ? 'has-error' : ''}`}>
        <label htmlFor="title">
          Judul Buku <span className="required-star">*</span>
        </label>
        <input
          id="title"
          name="title"
          type="text"
          placeholder="Contoh: Belajar React Modern"
          value={formData.title}
          onChange={handleChange}
          onBlur={handleBlur}
          className={errors.title && touched.title ? 'input-error' : ''}
        />
        {errors.title && touched.title && (
          <span className="error-message" role="alert">
            {errors.title}
          </span>
        )}
      </div>

      {/* Input Penulis Buku */}
      <div className={`form-group ${errors.author && touched.author ? 'has-error' : ''}`}>
        <label htmlFor="author">
          Nama Penulis <span className="required-star">*</span>
        </label>
        <input
          id="author"
          name="author"
          type="text"
          placeholder="Contoh: Dan Abramov"
          value={formData.author}
          onChange={handleChange}
          onBlur={handleBlur}
          className={errors.author && touched.author ? 'input-error' : ''}
        />
        {errors.author && touched.author && (
          <span className="error-message" role="alert">
            {errors.author}
          </span>
        )}
      </div>

      {/* Baris Status & Tahun */}
      <div className="form-row">
        <div className="form-group flex-1">
          <label htmlFor="status">Status Buku</label>
          <select id="status" name="status" value={formData.status} onChange={handleChange}>
            <option value="milik">Dimiliki (Milik)</option>
            <option value="baca">Sedang Dibaca (Baca)</option>
            <option value="beli">Rencana Beli (Beli)</option>
          </select>
        </div>

        <div className={`form-group flex-1 ${errors.year && touched.year ? 'has-error' : ''}`}>
          <label htmlFor="year">Tahun Terbit (Opsional)</label>
          <input
            id="year"
            name="year"
            type="number"
            placeholder="Contoh: 2024"
            value={formData.year}
            onChange={handleChange}
            onBlur={handleBlur}
            className={errors.year && touched.year ? 'input-error' : ''}
          />
          {errors.year && touched.year && (
            <span className="error-message">{errors.year}</span>
          )}
        </div>
      </div>

      {/* Kategori */}
      <div className="form-group">
        <label htmlFor="category">Kategori / Genre (Opsional)</label>
        <input
          id="category"
          name="category"
          type="text"
          placeholder="Contoh: Pemrograman, Fiksi, Sains"
          value={formData.category}
          onChange={handleChange}
        />
      </div>

      {/* Catatan Tambahan */}
      <div className="form-group">
        <label htmlFor="notes">Catatan Tambahan (Opsional)</label>
        <textarea
          id="notes"
          name="notes"
          rows="3"
          placeholder="Tuliskan catatan, bab bacaan, atau ulasan singkat..."
          value={formData.notes}
          onChange={handleChange}
        ></textarea>
      </div>

      {/* Tombol Aksi */}
      <div className="form-actions">
        {onCancel && (
          <button type="button" className="btn btn-secondary" onClick={onCancel}>
            Batal
          </button>
        )}
        <button type="submit" className="btn btn-primary">
          {submitButtonText}
        </button>
      </div>
    </form>
  );
}

BookForm.propTypes = {
  onSubmit: PropTypes.func.isRequired,
  initialData: PropTypes.shape({
    id: PropTypes.number,
    title: PropTypes.string,
    author: PropTypes.string,
    status: PropTypes.string,
    year: PropTypes.oneOfType([PropTypes.number, PropTypes.string]),
    category: PropTypes.string,
    notes: PropTypes.string,
  }),
  onCancel: PropTypes.func,
  submitButtonText: PropTypes.string,
};

export default BookForm;
