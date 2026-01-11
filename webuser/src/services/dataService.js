import api from './api';

export const farmService = {
  getAll: () => api.get('/farms/'),
  getById: (id) => api.get(`/farms/${id}/`),
  create: (data) => api.post('/farms/', data),
  update: (id, data) => api.put(`/farms/${id}/`, data),
  delete: (id) => api.delete(`/farms/${id}/`),
};

export const animalService = {
  getAll: () => api.get('/animals/'),
  getById: (id) => api.get(`/animals/${id}/`),
  create: (data) => api.post('/animals/', data),
  update: (id, data) => api.put(`/animals/${id}/`, data),
  delete: (id) => api.delete(`/animals/${id}/`),
};

export const vaccinationService = {
  getAll: () => api.get('/vaccinations/'),
  getById: (id) => api.get(`/vaccinations/${id}/`),
  create: (data) => api.post('/vaccinations/', data),
  update: (id, data) => api.put(`/vaccinations/${id}/`, data),
  delete: (id) => api.delete(`/vaccinations/${id}/`),
};

export const productService = {
  getAll: () => api.get('/marketplace/'),
  getById: (id) => api.get(`/marketplace/${id}/`),
  create: (data) => api.post('/marketplace/', data),
  update: (id, data) => api.put(`/marketplace/${id}/`, data),
  delete: (id) => api.delete(`/marketplace/${id}/`),
};

export const notificationService = {
  getAll: () => api.get('/notifications/'),
  markAsRead: (id) => api.post(`/notifications/${id}/mark_as_read/`),
  markAllAsRead: () => api.post('/notifications/mark_all_as_read/'),
};
