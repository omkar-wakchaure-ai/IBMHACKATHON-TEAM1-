import React from 'react';
import { Bell, User, Search } from 'lucide-react';

const Topbar = ({ title = "Dashboard" }) => {
  return (
    <header className="h-20 bg-white border-b border-gray-100 flex items-center justify-between px-8 sticky top-0 z-10">
      <h2 className="text-2xl font-semibold text-gray-800">{title}</h2>
      
      <div className="flex items-center space-x-6">
        <div className="relative">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" size={18} />
          <input 
            type="text" 
            placeholder="Search inventory..." 
            className="pl-10 pr-4 py-2 bg-gray-50 border-none rounded-full text-sm focus:ring-2 focus:ring-blue-100 outline-none w-64 transition-all"
          />
        </div>
        
        <button className="relative p-2 text-gray-400 hover:text-gray-600 transition-colors">
          <Bell size={20} />
          <span className="absolute top-1 right-1 w-2.5 h-2.5 bg-red-400 rounded-full border-2 border-white"></span>
        </button>
        
        <div className="h-9 w-9 bg-blue-50 rounded-full flex items-center justify-center text-blue-600 cursor-pointer hover:bg-blue-100 transition-colors">
          <User size={18} />
        </div>
      </div>
    </header>
  );
};

export default Topbar;
