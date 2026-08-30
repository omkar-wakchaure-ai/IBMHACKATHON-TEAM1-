import React from 'react';
import { LayoutDashboard, PackagePlus, LineChart, FileText, Settings, Box } from 'lucide-react';
import { NavLink } from 'react-router-dom';

const Sidebar = () => {
  const navItems = [
    { name: 'Overview', icon: LayoutDashboard, path: '/' },
    { name: 'Ingestion Portal', icon: PackagePlus, path: '/ingestion' },
    { name: 'Analytics', icon: LineChart, path: '/analytics' },
    { name: 'Forecast & Billing', icon: FileText, path: '/forecast' },
    { name: 'Settings', icon: Settings, path: '/settings' },
  ];

  return (
    <div className="w-64 h-screen bg-white border-r border-gray-100 flex flex-col shadow-sm fixed">
      <div className="p-6 flex items-center space-x-3">
        <div className="bg-blue-50 p-2 rounded-lg text-blue-600">
          <Box size={24} />
        </div>
        <h1 className="text-xl font-bold text-gray-800">FreshStock<span className="text-blue-500">AI</span></h1>
      </div>
      <nav className="flex-1 px-4 space-y-2 mt-4">
        {navItems.map((item) => (
          <NavLink
            key={item.name}
            to={item.path}
            className={({ isActive }) =>
              `flex items-center space-x-3 px-4 py-3 rounded-xl transition-all duration-200 ${
                isActive 
                  ? 'bg-blue-50 text-blue-600 font-medium' 
                  : 'text-gray-500 hover:bg-gray-50 hover:text-gray-700'
              }`
            }
          >
            <item.icon size={20} />
            <span>{item.name}</span>
          </NavLink>
        ))}
      </nav>
    </div>
  );
};

export default Sidebar;
