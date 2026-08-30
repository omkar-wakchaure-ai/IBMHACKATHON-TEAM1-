import React, { createContext, useState, useContext } from 'react';

const AppContext = createContext();

export const AppProvider = ({ children }) => {
  const [globalDateRange, setGlobalDateRange] = useState('7d');
  const [warehouseId, setWarehouseId] = useState('WH-01');

  return (
    <AppContext.Provider value={{ globalDateRange, setGlobalDateRange, warehouseId, setWarehouseId }}>
      {children}
    </AppContext.Provider>
  );
};

export const useAppContext = () => useContext(AppContext);
