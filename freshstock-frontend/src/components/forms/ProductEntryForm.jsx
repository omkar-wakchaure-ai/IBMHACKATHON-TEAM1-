import React, { useState } from 'react';
import { Save } from 'lucide-react';

const ProductEntryForm = () => {
  const [formData, setFormData] = useState({
    name: '', supplier: '', price: '', mfgDate: '', expDate: '', quantity: ''
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Submitting to FastAPI backend:", formData);
    // Add Axios POST here
  };

  const inputClass = "w-full px-4 py-3 rounded-xl bg-gray-50 border border-transparent focus:border-blue-200 focus:bg-white focus:ring-0 transition-all text-sm";
  const labelClass = "block text-sm font-medium text-gray-700 mb-2";

  return (
    <form onSubmit={handleSubmit} className="bg-white p-8 rounded-2xl shadow-[0_4px_20px_-4px_rgba(0,0,0,0.02)] border border-gray-50 max-w-2xl">
      <div className="grid grid-cols-2 gap-6 mb-6">
        <div className="col-span-2 md:col-span-1">
          <label className={labelClass}>Product Name</label>
          <input type="text" name="name" value={formData.name} onChange={handleChange} className={inputClass} placeholder="e.g. Tomatoes" required />
        </div>
        <div className="col-span-2 md:col-span-1">
          <label className={labelClass}>Supplier</label>
          <input type="text" name="supplier" value={formData.supplier} onChange={handleChange} className={inputClass} placeholder="e.g. FreshFarms Ltd" required />
        </div>
        
        <div>
          <label className={labelClass}>Manufacturing Date</label>
          <input type="date" name="mfgDate" value={formData.mfgDate} onChange={handleChange} className={inputClass} required />
        </div>
        <div>
          <label className={labelClass}>Expiry Date</label>
          <input type="date" name="expDate" value={formData.expDate} onChange={handleChange} className={inputClass} required />
        </div>

        <div>
          <label className={labelClass}>Batch Quantity (kg/L)</label>
          <input type="number" name="quantity" value={formData.quantity} onChange={handleChange} className={inputClass} placeholder="100" required />
        </div>
        <div>
          <label className={labelClass}>Unit Price (₹)</label>
          <input type="number" name="price" value={formData.price} onChange={handleChange} className={inputClass} placeholder="45" required />
        </div>
      </div>
      
      <div className="flex justify-end pt-4 border-t border-gray-50">
        <button type="submit" className="flex items-center space-x-2 bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-xl font-medium transition-colors shadow-sm shadow-blue-200">
          <Save size={18} />
          <span>Ingest Inventory</span>
        </button>
      </div>
    </form>
  );
};

export default ProductEntryForm;
