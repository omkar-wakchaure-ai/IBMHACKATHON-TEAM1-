import React, { useState } from 'react';
import StatCard from '../components/dashboard/StatCard';
import AlertBanner from '../components/dashboard/AlertBanner';
import { Package, TrendingDown, AlertTriangle, DollarSign } from 'lucide-react';
import ChatWidget from '../components/ai/ChatWidget';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const Overview = () => {
  const [selectedProduct, setSelectedProduct] = useState('Tomatoes');

  // Mock data for the high-level summary chart
  const overviewData = [
    { name: 'Tomatoes', stock: 200, demand: 350 },
    { name: 'Milk', stock: 80, demand: 75 },
    { name: 'Chicken', stock: 100, demand: 95 },
    { name: 'Potatoes', stock: 300, demand: 280 },
    { name: 'Bread', stock: 50, demand: 60 },
  ];

  // Filter data to only show the selected product
  const chartData = overviewData.filter(item => item.name === selectedProduct);
  const unit = selectedProduct === 'Milk' ? 'L' : 'kg';

  return (
    <div className="p-8 space-y-8">
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <StatCard title="Total Inventory" value="12,450 kg" icon={Package} colorClass="blue" />
        <StatCard title="Expected Demand" value="8,920 kg" icon={TrendingDown} trend="12%" isPositive={false} colorClass="amber" />
        <StatCard title="Spoilage Risk" value="8.4%" icon={AlertTriangle} trend="2.1%" isPositive={true} colorClass="red" />
        <StatCard title="Est. Value at Risk" value="₹45,200" icon={DollarSign} colorClass="red" />
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2 space-y-6">
          <h3 className="text-xl font-bold text-gray-800">Action Required</h3>
          <AlertBanner type="critical" message="CRITICAL: 200 kg Tomatoes expiring in 2 days. 150 kg shortage expected." />
          <AlertBanner type="warning" message="WARNING: Milk stock falling below safety threshold by Thursday." />
          
          <div className="bg-white p-6 rounded-2xl shadow-[0_4px_20px_-4px_rgba(0,0,0,0.02)] border border-gray-50 h-[380px]">
            <div className="flex justify-between items-center mb-6">
              <h3 className="text-lg font-semibold text-gray-800">Current Stock vs. Expected Demand</h3>
              <select 
                value={selectedProduct}
                onChange={(e) => setSelectedProduct(e.target.value)}
                className="px-4 py-2 bg-gray-50 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-100"
              >
                {overviewData.map((item) => (
                  <option key={item.name} value={item.name}>{item.name}</option>
                ))}
              </select>
            </div>
            
            <div className="h-64 w-full">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={chartData} margin={{ top: 0, right: 10, left: -20, bottom: 0 }}>
                  <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#f3f4f6" />
                  <XAxis dataKey="name" axisLine={false} tickLine={false} tick={{fill: '#9ca3af', fontSize: 12}} dy={10} />
                  <YAxis axisLine={false} tickLine={false} tick={{fill: '#9ca3af', fontSize: 12}} />
                  <Tooltip 
                    cursor={{fill: '#f9fafb'}} 
                    contentStyle={{ borderRadius: '12px', border: 'none', boxShadow: '0 4px 6px rgba(0,0,0,0.05)' }}
                    formatter={(value, name) => [`${value} ${unit}`, name]} 
                  />
                  <Legend verticalAlign="top" height={36} iconType="circle" wrapperStyle={{ fontSize: '12px' }}/>
                  <Bar dataKey="stock" name={`Current Stock (${unit})`} fill="#3B82F6" radius={[4, 4, 0, 0]} barSize={80} />
                  <Bar dataKey="demand" name={`Expected Demand (${unit})`} fill="#EF4444" radius={[4, 4, 0, 0]} barSize={80} />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </div>
        </div>
        
        <div className="lg:col-span-1">
          <ChatWidget />
        </div>
      </div>
    </div>
  );
};

export default Overview;
