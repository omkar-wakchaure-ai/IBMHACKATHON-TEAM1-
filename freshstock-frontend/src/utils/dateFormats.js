export const calculateDaysRemaining = (expiryDateString) => {
  const today = new Date();
  const expiry = new Date(expiryDateString);
  const diffTime = Math.abs(expiry - today);
  const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)); 
  return diffDays;
};

export const formatDate = (dateString) => {
  const options = { year: 'numeric', month: 'short', day: 'numeric' };
  return new Date(dateString).toLocaleDateString(undefined, options);
};
