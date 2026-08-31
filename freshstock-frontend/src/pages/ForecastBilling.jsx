import React, { useState } from 'react';
import { generatePurchaseOrderPDF } from '../utils/pdfGenerator';
import { FileText, Download, CheckCircle2, Clock, ReceiptText } from 'lucide-react';
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const ForecastBilling = () => {
  const [selectedProduct, setSelectedProduct] = useState('Tomatoes');

  // Determine the unit based on the selected product
  const unit = selectedProduct === 'Milk' ? 'L' : 'kg';

  // Mock forecasting data predicting stock-outs over the next week
  const forecastData = {
    Tomatoes: [
      { date: 'Aug 30', predictedDemand: 280, currentStock: 150 },
      { date: 'Aug 31', predictedDemand: 300, currentStock: 100 },
      { date: 'Sep 01', predictedDemand: 310, currentStock: 50 },
      { date: 'Sep 02', predictedDemand: 290, currentStock: 0 },
      { date: 'Sep 03', predictedDemand: 330, currentStock: 0 },
      { date: 'Sep 04', predictedDemand: 350, currentStock: 0 },
      { date: 'Sep 05', predictedDemand: 340, currentStock: 0 },
    ],
    Milk: [
      { date: 'Aug 30', predictedDemand: 90, currentStock: 80 },
      { date: 'Aug 31', predictedDemand: 95, currentStock: 50 },
      { date: 'Sep 01', predictedDemand: 100, currentStock: 20 },
      { date: 'Sep 02', predictedDemand: 110, currentStock: 0 },
      { date: 'Sep 03', predictedDemand: 105, currentStock: 0 },
      { date: 'Sep 04', predictedDemand: 115, currentStock: 0 },
      { date: 'Sep 05', predictedDemand: 120, currentStock: 0 },
    ]
  };

  // Mock Billing History
  const mockBillingHistory = [
    { id: 'PO-2026-8920', date: 'Aug 28, 2026', supplier: 'FreshFarms Ltd', items: 'Tomatoes, Potatoes', amount: '₹12,450', status: 'Completed' },
    { id: 'PO-2026-8919', date: 'Aug 25, 2026', supplier: 'DairyCo', items: 'Milk', amount: '₹4,800', status: 'Completed' },
    { id: 'PO-2026-8918', date: 'Aug 21, 2026', supplier: 'AgriMeat', items: 'Chicken', amount: '₹15,400', status: 'Pending' },
    { id: 'PO-2026-8917', date: 'Aug 18, 2026', supplier: 'LocalBakery', items: 'Bread', amount: '₹2,000', status: 'Completed' },
  ];

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

      <div className="bg-white p-6 rounded-2xl shadow-[0_4px_20px_-4px_rgba(0,0,0,0.02)] border border-gray-50">
        <div className="flex justify-between items-center mb-6">
          <h3 className="text-lg font-semibold text-gray-800">Demand Projection vs. Inventory Runway</h3>
          <select
            value={selectedProduct}
            onChange={(e) => setSelectedProduct(e.target.value)}
            className="px-4 py-2 bg-gray-50 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-100"
          >
            <option value="Tomatoes">Tomatoes</option>
            <option value="Milk">Milk</option>
          </select>
        </div>

        <div className="h-80 w-full">
          <ResponsiveContainer width="100%" height="100%">
            <AreaChart data={forecastData[selectedProduct]}>
              <defs>
                <linearGradient id="colorDemand" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#EF4444" stopOpacity={0.3}/>
                  <stop offset="95%" stopColor="#EF4444" stopOpacity={0}/>
                </linearGradient>
                <linearGradient id="colorStock" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#3B82F6" stopOpacity={0.3}/>
                  <stop offset="95%" stopColor="#3B82F6" stopOpacity={0}/>
                </linearGradient>
              </defs>
              <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#f3f4f6" />
              <XAxis dataKey="date" axisLine={false} tickLine={false} tick={{fill: '#9ca3af', fontSize: 12}} />
              <YAxis axisLine={false} tickLine={false} tick={{fill: '#9ca3af', fontSize: 12}} />
              <Tooltip 
                contentStyle={{ borderRadius: '12px', border: 'none', boxShadow: '0 4px 6px rgba(0,0,0,0.05)' }} 
                formatter={(value, name) => [`${value} ${unit}`, name]} 
              />
              <Legend verticalAlign="top" height={36} iconType="circle" />
              <Area type="monotone" dataKey="predictedDemand" name="AI Predicted Demand" stroke="#EF4444" fillOpacity={1} fill="url(#colorDemand)" />
              <Area type="monotone" dataKey="currentStock" name="Projected Stock Level" stroke="#3B82F6" fillOpacity={1} fill="url(#colorStock)" />
            </AreaChart>
          </ResponsiveContainer>
        </div>
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

      {/* Billing History Table */}
      <div className="bg-white p-6 rounded-2xl shadow-[0_4px_20px_-4px_rgba(0,0,0,0.02)] border border-gray-50">
        <div className="flex items-center space-x-3 mb-6">
          <div className="p-2 bg-gray-50 rounded-lg text-gray-500">
            <ReceiptText size={20} />
          </div>
          <h3 className="text-lg font-semibold text-gray-800">Billing & Purchase Order History</h3>
        </div>
        
        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="border-b border-gray-100 text-gray-500 text-sm">
                <th className="py-3 px-4 font-medium">Order ID</th>
                <th className="py-3 px-4 font-medium">Date Generated</th>
                <th className="py-3 px-4 font-medium">Supplier & Items</th>
                <th className="py-3 px-4 font-medium">Total Amount</th>
                <th className="py-3 px-4 font-medium">Status</th>
                <th className="py-3 px-4 font-medium text-right">Action</th>
              </tr>
            </thead>
            <tbody>
              {mockBillingHistory.map((order, idx) => (
                <tr key={idx} className="border-b border-gray-50 last:border-0 hover:bg-gray-50/50 transition-colors">
                  <td className="py-4 px-4 text-sm font-semibold text-gray-800">{order.id}</td>
                  <td className="py-4 px-4 text-sm text-gray-600">{order.date}</td>
                  <td className="py-4 px-4">
                    <p className="text-sm font-medium text-gray-800">{order.supplier}</p>
                    <p className="text-xs text-gray-500 mt-0.5">{order.items}</p>
                  </td>
                  <td className="py-4 px-4 text-sm font-semibold text-gray-800">{order.amount}</td>
                  <td className="py-4 px-4">
                    <span className={`inline-flex items-center space-x-1.5 px-2.5 py-1 rounded-full text-xs font-medium ${
                      order.status === 'Completed' ? 'bg-emerald-50 text-emerald-700 border border-emerald-100' : 'bg-amber-50 text-amber-700 border border-amber-100'
                    }`}>
                      {order.status === 'Completed' ? <CheckCircle2 size={14} /> : <Clock size={14} />}
                      <span>{order.status}</span>
                    </span>
                  </td>
                  <td className="py-4 px-4 text-right">
                    <button className="p-2 text-gray-400 hover:text-blue-600 hover:bg-blue-50 rounded-lg transition-colors">
                      <Download size={18} />
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

    </div>
  );
};

export default ForecastBilling;