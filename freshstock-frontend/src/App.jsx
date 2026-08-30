import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Sidebar from './components/layout/Sidebar';
import Topbar from './components/layout/Topbar';

// Pages
import Overview from './pages/Overview';
import IngestionPortal from './pages/IngestionPortal';
import Analytics from './pages/Analytics';
import ForecastBilling from './pages/ForecastBilling';
import Settings from './pages/Settings';

function App() {
  return (
    <div className="flex h-screen bg-gray-50/30 overflow-hidden font-sans">
      {/* Fixed Sidebar */}
      <Sidebar />
      
      {/* Main Content Area */}
      <div className="flex-1 flex flex-col ml-64 overflow-hidden">
        <Topbar />
        
        {/* Scrollable Page Content */}
        <main className="flex-1 overflow-x-hidden overflow-y-auto bg-gray-50/30">
          <Routes>
            <Route path="/" element={<Overview />} />
            <Route path="/ingestion" element={<IngestionPortal />} />
            <Route path="/analytics" element={<Analytics />} />
            <Route path="/forecast" element={<ForecastBilling />} />
            <Route path="/settings" element={<Settings />} />
          </Routes>
        </main>
      </div>
    </div>
  );
}

export default App;
