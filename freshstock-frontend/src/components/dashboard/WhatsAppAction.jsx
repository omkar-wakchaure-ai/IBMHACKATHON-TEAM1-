import React, { useState } from 'react';
import { MessageCircle, CheckCircle2 } from 'lucide-react';

const WhatsAppAction = ({ productName, quantity, supplierName }) => {
  const [status, setStatus] = useState('idle'); // idle, loading, success

  const handleOrder = async () => {
    setStatus('loading');
    // Dummy API Call delay
    setTimeout(() => {
      setStatus('success');
    }, 1500);
  };

  if (status === 'success') {
    return (
      <div className="flex items-center justify-center space-x-2 w-full py-3 bg-emerald-50 text-emerald-600 rounded-xl font-medium border border-emerald-100">
        <CheckCircle2 size={18} />
        <span>Order Sent to {supplierName}</span>
      </div>
    );
  }

  return (
    <button 
      onClick={handleOrder}
      disabled={status === 'loading'}
      className="flex items-center justify-center space-x-2 w-full py-3 bg-red-50 hover:bg-red-100 text-red-600 rounded-xl font-medium transition-colors border border-red-100 disabled:opacity-70"
    >
      <MessageCircle size={18} />
      <span>{status === 'loading' ? 'Sending...' : `Approve & Order ${quantity}`}</span>
    </button>
  );
};

export default WhatsAppAction;
