import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getCrises = async () => {
  const response = await api.get('/crises');
  return response.data;
};

export const getCrisis = async (id: string) => {
  const response = await api.get(`/crises/${id}`);
  return response.data;
};

export const searchCrises = async (query: string, filters: any = {}) => {
  const response = await api.post('/search', { query, filters });
  return response.data;
};

export const compareCrises = async (crisisIds: string[]) => {
  const response = await api.post('/compare', { crisis_ids: crisisIds });
  return response.data;
};

export default api;