import React from 'react';

const Settings = () => {
  return (
    <div className="p-8 max-w-2xl space-y-8">
      <h2 className="text-2xl font-bold text-gray-800">System Configuration</h2>
      
      <div className="bg-white p-8 rounded-2xl shadow-[0_4px_20px_-4px_rgba(0,0,0,0.02)] border border-gray-50 space-y-6">
        <h3 className="text-lg font-semibold text-gray-800 border-b border-gray-100 pb-2">WhatsApp / Twilio Integrations</h3>
        
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">Twilio Account SID</label>
          <input type="password" placeholder="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" className="w-full px-4 py-3 rounded-xl bg-gray-50 border border-transparent focus:border-blue-200 focus:bg-white focus:ring-0 transition-all text-sm" />
        </div>
        
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">Default Supplier WhatsApp Number</label>
          <input type="text" placeholder="+1234567890" className="w-full px-4 py-3 rounded-xl bg-gray-50 border border-transparent focus:border-blue-200 focus:bg-white focus:ring-0 transition-all text-sm" />
        </div>

        <button className="bg-gray-800 text-white px-6 py-2 rounded-lg text-sm font-medium hover:bg-gray-700">
          Save Configuration
        </button>
      </div>
    </div>
  );
};

export default Settings;
