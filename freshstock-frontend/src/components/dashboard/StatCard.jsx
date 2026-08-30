import React from 'react';
import { TrendingUp, TrendingDown } from 'lucide-react';

const StatCard = ({ title, value, icon: Icon, trend, isPositive, colorClass = "blue" }) => {
  const colorThemes = {
    blue: "bg-blue-50 text-blue-600",
    red: "bg-red-50 text-red-600",
    green: "bg-emerald-50 text-emerald-600",
    amber: "bg-amber-50 text-amber-600"
  };

  return (
    <div className="bg-white p-6 rounded-2xl shadow-[0_4px_20px_-4px_rgba(0,0,0,0.02)] border border-gray-50 flex flex-col justify-between h-40">
      <div className="flex justify-between items-start">
        <p className="text-sm font-medium text-gray-500">{title}</p>
        <div className={`p-2 rounded-xl ${colorThemes[colorClass]}`}>
          <Icon size={20} />
        </div>
      </div>
      
      <div>
        <h3 className="text-3xl font-bold text-gray-800">{value}</h3>
        {trend && (
          <div className={`flex items-center space-x-1 text-sm mt-2 ${isPositive ? 'text-emerald-500' : 'text-red-500'}`}>
            {isPositive ? <TrendingDown size={16} /> : <TrendingUp size={16} />}
            <span className="font-medium">{trend} vs last week</span>
          </div>
        )}
      </div>
    </div>
  );
};

export default StatCard;
