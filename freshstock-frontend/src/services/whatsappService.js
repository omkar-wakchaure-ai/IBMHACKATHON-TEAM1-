import { apiClient } from './api';

export const sendWhatsAppOrder = async (supplierId, productName, quantity) => {
  const response = await apiClient.post('/whatsapp/send', {
    supplier_id: supplierId,
    product_name: productName,
    quantity: quantity
  });
  return response.data;
};
