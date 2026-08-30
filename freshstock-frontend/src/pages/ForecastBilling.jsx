import React from 'react';
import { generatePurchaseOrderPDF } from '../utils/pdfGenerator';
import { FileText, Download } from 'lucide-react';

const ForecastBilling = () => {
  const handleGenerateBill = () => {
    const orderData = {
      id: 'PO-2026-8921',
      date: new Date().toLocaleDateString(),
      items: [
        { name: 'Tomatoes', qty: 150, price: 45 },
        { name: 'Milk', qty: 80, price: 60 }
      ]
    };
    generatePurchaseOrderPDF(orderData);
  };

  return (
    <div className="p-8 space-y-8">
      <h2 className="text-2xl font-bold text-gray-800">AI Forecasting & Billing</h2>
      
      <div className="bg-white p-6 rounded-2xl shadow-[0_4px_20px_-4px_rgba(0,0,0,0.02)] border border-gray-50 h-80 flex flex-col items-center justify-center text-gray-400">
        <span>[Recharts Line Chart: Projected Demand vs Current Stock over next 30 days]</span>
      </div>

      <div className="bg-blue-50 p-6 rounded-2xl border border-blue-100 flex items-center justify-between">
        <div>
          <h3 className="text-lg font-bold text-blue-900">Automated Purchase Order</h3>
          <p className="text-blue-700 text-sm mt-1">Generate a formal PDF bill based on AI-predicted shortages for the upcoming week.</p>
        </div>
        <button 
          onClick={handleGenerateBill}
          className="flex items-center space-x-2 bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-xl font-medium transition-colors shadow-sm"
        >
          <FileText size={18} />
          <span>Generate PO (PDF)</span>
          <Download size={16} className="ml-2 opacity-70" />
        </button>
      </div>
    </div>
  );
};

export default ForecastBilling;
