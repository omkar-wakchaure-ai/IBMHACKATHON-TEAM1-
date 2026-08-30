import React from 'react';
import StatCard from '../components/dashboard/StatCard';
import AlertBanner from '../components/dashboard/AlertBanner';
import { Package, TrendingDown, AlertTriangle, DollarSign } from 'lucide-react';
import ChatWidget from '../components/ai/ChatWidget';

const Overview = () => {
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
          
          <div className="bg-white p-6 rounded-2xl shadow-[0_4px_20px_-4px_rgba(0,0,0,0.02)] border border-gray-50 h-64 flex items-center justify-center text-gray-400">
            [High-Level Inventory Summary Chart Placeholder]
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
