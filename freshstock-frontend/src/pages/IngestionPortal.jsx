import React from 'react';
import ProductEntryForm from '../components/forms/ProductEntryForm';

const IngestionPortal = () => {
  return (
    <div className="p-8">
      <div className="max-w-2xl mb-8">
        <h2 className="text-2xl font-bold text-gray-800 mb-2">Ingestion Portal</h2>
        <p className="text-gray-500">Add new supplier deliveries here. The system will automatically calculate shelf-life constraints and update ML forecasting parameters.</p>
      </div>
      <ProductEntryForm />
    </div>
  );
};

export default IngestionPortal;
