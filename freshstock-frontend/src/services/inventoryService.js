import { apiClient } from './api';

export const getInventory = async () => {
  const response = await apiClient.get('/products');
  return response.data;
};

export const addProduct = async (productData) => {
  const response = await apiClient.post('/products', productData);
  return response.data;
};
