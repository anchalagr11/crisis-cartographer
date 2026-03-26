import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api/v1',
});

export const getCrises = () => api.get('/crises');
export const compareCrises = (data: any) => api.post('/compare', data);

export default api;