import React, { useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import WhatsAppAction from '../components/dashboard/WhatsAppAction';
import { calculateDaysRemaining } from '../utils/dateFormats';

const Analytics = () => {
  const [selectedProduct, setSelectedProduct] = useState('Tomatoes');

  // Mock data for the expiring items table
  const mockExpiringData = [
    { id: 1, name: 'Tomatoes', qty: '150 kg', supplier: 'FreshFarms Ltd', exp: '2026-09-01' },
    { id: 2, name: 'Milk', qty: '80 L', supplier: 'DairyCo', exp: '2026-09-02' },
  ];

  // Mock historical data for the chart
  const historicalData = {
    Tomatoes: [
      { date: 'Aug 24', inventory: 300, demand: 250 },
      { date: 'Aug 25', inventory: 250, demand: 260 },
      { date: 'Aug 26', inventory: 150, demand: 280 }, // Current low stock
      { date: 'Aug 27', inventory: 100, demand: 300 },
      { date: 'Aug 28', inventory: 50, demand: 310 },
    ],
    Milk: [
      { date: 'Aug 24', inventory: 150, demand: 100 },
      { date: 'Aug 25', inventory: 120, demand: 105 },
      { date: 'Aug 26', inventory: 80, demand: 110 },
      { date: 'Aug 27', inventory: 60, demand: 115 },
      { date: 'Aug 28', inventory: 20, demand: 120 },
    ]
  };

  return (
    <div className="p-8 space-y-8">
      <h2 className="text-2xl font-bold text-gray-800">Historical & Spoilage Analytics</h2>
      
      {/* Interactive Graph Section */}
      <div className="bg-white p-6 rounded-2xl shadow-[0_4px_20px_-4px_rgba(0,0,0,0.02)] border border-gray-50">
        <div className="flex justify-between items-center mb-6">
          <h3 className="text-lg font-semibold text-gray-800">Inventory vs. Demand Trends</h3>
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
            <LineChart data={historicalData[selectedProduct]}>
              <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#f3f4f6" />
              <XAxis dataKey="date" axisLine={false} tickLine={false} tick={{fill: '#9ca3af', fontSize: 12}} />
              <YAxis axisLine={false} tickLine={false} tick={{fill: '#9ca3af', fontSize: 12}} />
              <Tooltip 
                contentStyle={{ borderRadius: '12px', border: 'none', boxShadow: '0 4px 6px rgba(0,0,0,0.05)' }}
              />
              <Legend verticalAlign="top" height={36} iconType="circle" />
              <Line type="monotone" dataKey="inventory" name="Current Inventory" stroke="#3B82F6" strokeWidth={3} dot={{r: 4, strokeWidth: 2}} />
              <Line type="monotone" dataKey="demand" name="Historical Demand" stroke="#EF4444" strokeWidth={3} dot={{r: 4, strokeWidth: 2}} />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Critical Spoilage Table */}
      <div className="bg-white p-6 rounded-2xl shadow-[0_4px_20px_-4px_rgba(0,0,0,0.02)] border border-red-100">
        <h3 className="text-lg font-semibold text-red-600 mb-4">Critical Spoilage Red Zone</h3>
        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="border-b border-gray-100 text-gray-500 text-sm">
                <th className="py-3 px-4">Product</th>
                <th className="py-3 px-4">Quantity at Risk</th>
                <th className="py-3 px-4">Days Until Expiry</th>
                <th className="py-3 px-4">Action (WhatsApp Supplier)</th>
              </tr>
            </thead>
            <tbody>
              {mockExpiringData.map(item => (
                <tr key={item.id} className="border-b border-gray-50 last:border-0 hover:bg-gray-50/50">
                  <td className="py-4 px-4 font-medium text-gray-800">{item.name}</td>
                  <td className="py-4 px-4 text-red-600 font-medium">{item.qty}</td>
                  <td className="py-4 px-4">
                    <span className="px-2 py-1 bg-red-50 text-red-700 rounded-md text-sm font-semibold">
                      {calculateDaysRemaining(item.exp)} Days
                    </span>
                  </td>
                  <td className="py-4 px-4 max-w-[200px]">
                    <WhatsAppAction productName={item.name} quantity={item.qty} supplierName={item.supplier} />
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

export default Analytics;
