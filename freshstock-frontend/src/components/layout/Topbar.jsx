import React, { useState, useRef, useEffect } from 'react';
import { Bell, User, Search, Settings, UserCircle, AlertCircle, X, MapPin, Briefcase, Code } from 'lucide-react';
import { Link } from 'react-router-dom';

const Topbar = ({ title = "Dashboard" }) => {
  const [isNotifOpen, setIsNotifOpen] = useState(false);
  const [isProfileOpen, setIsProfileOpen] = useState(false);
  const [isProfileModalOpen, setIsProfileModalOpen] = useState(false);
  
  const notifRef = useRef(null);
  const profileRef = useRef(null);

  // Close dropdowns if user clicks outside of them
  useEffect(() => {
    const handleClickOutside = (event) => {
      if (notifRef.current && !notifRef.current.contains(event.target)) {
        setIsNotifOpen(false);
      }
      if (profileRef.current && !profileRef.current.contains(event.target)) {
        setIsProfileOpen(false);
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  const openProfileModal = () => {
    setIsProfileOpen(false);
    setIsProfileModalOpen(true);
  };

  return (
    <>
      {/* Changed justify-between to justify-end to keep items on the right */}
      <header className="h-20 bg-white border-b border-gray-100 flex items-center justify-end px-8 sticky top-0 z-20">
        
        <div className="flex items-center space-x-6">
          {/* Search Bar */}
          <div className="relative">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" size={18} />
            <input 
              type="text" 
              placeholder="Search inventory..." 
              className="pl-10 pr-4 py-2 bg-gray-50 border-none rounded-full text-sm focus:ring-2 focus:ring-blue-100 outline-none w-64 transition-all"
            />
          </div>
          
          {/* Notifications Dropdown */}
          <div className="relative" ref={notifRef}>
            <button 
              onClick={() => setIsNotifOpen(!isNotifOpen)}
              className="relative p-2 text-gray-400 hover:text-gray-600 transition-colors focus:outline-none"
            >
              <Bell size={20} />
              <span className="absolute top-1 right-1 w-2.5 h-2.5 bg-red-400 rounded-full border-2 border-white"></span>
            </button>

            {isNotifOpen && (
              <div className="absolute right-0 mt-3 w-80 bg-white rounded-xl shadow-[0_8px_30px_rgb(0,0,0,0.12)] border border-gray-50 py-2 z-50">
                <div className="px-4 py-2 border-b border-gray-50">
                  <h3 className="font-semibold text-gray-800 text-sm">Notifications</h3>
                </div>
                <div className="flex items-start space-x-3 px-4 py-3 hover:bg-red-50/50 cursor-pointer transition-colors">
                  <AlertCircle size={18} className="text-red-500 mt-0.5" />
                  <div>
                    <p className="text-sm font-medium text-gray-800">High Spoilage Risk</p>
                    <p className="text-xs text-gray-500 mt-1">200 kg Tomatoes expiring in 2 days.</p>
                  </div>
                </div>
                <div className="flex items-start space-x-3 px-4 py-3 hover:bg-amber-50/50 cursor-pointer transition-colors">
                  <AlertCircle size={18} className="text-amber-500 mt-0.5" />
                  <div>
                    <p className="text-sm font-medium text-gray-800">Low Stock Alert</p>
                    <p className="text-xs text-gray-500 mt-1">Milk expected to run out by Thursday.</p>
                  </div>
                </div>
              </div>
            )}
          </div>
          
          {/* Profile Dropdown */}
          <div className="relative" ref={profileRef}>
            <div 
              onClick={() => setIsProfileOpen(!isProfileOpen)}
              className="h-9 w-9 bg-blue-50 rounded-full flex items-center justify-center text-blue-600 cursor-pointer hover:bg-blue-100 transition-colors"
            >
              <User size={18} />
            </div>

            {isProfileOpen && (
              <div className="absolute right-0 mt-3 w-56 bg-white rounded-xl shadow-[0_8px_30px_rgb(0,0,0,0.12)] border border-gray-50 py-2 z-50">
                <div className="px-4 py-3 border-b border-gray-50 mb-1">
                  <p className="text-sm font-medium text-gray-800">System Admin</p>
                  <p className="text-xs text-gray-500 truncate">admin@freshstock.ai</p>
                </div>
                
                <button 
                  onClick={openProfileModal}
                  className="w-full flex items-center space-x-3 px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-600 transition-colors"
                >
                  <UserCircle size={16} />
                  <span>My Profile</span>
                </button>
                
                {/* Replaced button with Link to navigate to Settings page */}
                <Link 
                  to="/settings"
                  onClick={() => setIsProfileOpen(false)}
                  className="w-full flex items-center space-x-3 px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-600 transition-colors"
                >
                  <Settings size={16} />
                  <span>Account Settings</span>
                </Link>
              </div>
            )}
          </div>
          
        </div>
      </header>

      {/* Profile Modal Overlay */}
      {isProfileModalOpen && (
        <div className="fixed inset-0 bg-gray-900/40 backdrop-blur-sm z-50 flex items-center justify-center">
          <div className="bg-white rounded-2xl shadow-xl w-full max-w-md overflow-hidden relative animate-in fade-in zoom-in duration-200">
            <button 
              onClick={() => setIsProfileModalOpen(false)}
              className="absolute top-4 right-4 p-1.5 text-gray-400 hover:text-gray-600 hover:bg-gray-100 rounded-full transition-colors"
            >
              <X size={20} />
            </button>
            
            <div className="bg-gradient-to-r from-blue-600 to-blue-400 h-24 w-full"></div>
            
            <div className="px-8 pb-8">
              <div className="relative flex justify-between items-end -mt-10 mb-4">
                <div className="h-20 w-20 bg-white rounded-full p-1 shadow-md">
                  <div className="h-full w-full bg-blue-50 rounded-full flex items-center justify-center text-blue-600">
                    <User size={32} />
                  </div>
                </div>
                <span className="px-3 py-1 bg-emerald-50 text-emerald-600 text-xs font-bold rounded-full border border-emerald-200 mb-2">
                  Active Admin
                </span>
              </div>
              
              <h3 className="text-xl font-bold text-gray-900">System Architect</h3>
              <p className="text-blue-600 text-sm font-medium mb-4">admin@freshstock.ai</p>
              
              <div className="space-y-3 mt-6">
                <div className="flex items-center text-gray-600 text-sm">
                  <Briefcase size={16} className="mr-3 text-gray-400" />
                  <span>Full-Stack ML Engineer & Developer</span>
                </div>
                <div className="flex items-center text-gray-600 text-sm">
                  <MapPin size={16} className="mr-3 text-gray-400" />
                  <span>Chhatrapati Sambhajinagar, Maharashtra</span>
                </div>
                <div className="flex items-center text-gray-600 text-sm">
                  <Code size={16} className="mr-3 text-gray-400" />
                  <span>Python, Flask, React, Salesforce Agentforce</span>
                </div>
              </div>

              <div className="mt-8 pt-6 border-t border-gray-100 flex justify-end">
                <button 
                  onClick={() => setIsProfileModalOpen(false)}
                  className="px-5 py-2 bg-blue-600 hover:bg-blue-700 text-white text-sm font-medium rounded-lg transition-colors"
                >
                  Close Profile
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default Topbar;