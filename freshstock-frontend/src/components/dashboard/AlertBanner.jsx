import React from 'react';
import { AlertTriangle, X } from 'lucide-react';

const AlertBanner = ({ message, type = "warning", onClose }) => {
  const styles = {
    warning: "bg-amber-50 border-amber-200 text-amber-800",
    critical: "bg-red-50 border-red-200 text-red-800",
  };

  const iconColors = {
    warning: "text-amber-500",
    critical: "text-red-500",
  };

  return (
    <div className={`flex items-center justify-between p-4 mb-6 rounded-xl border ${styles[type]}`}>
      <div className="flex items-center space-x-3">
        <AlertTriangle className={iconColors[type]} size={24} />
        <p className="font-medium">{message}</p>
      </div>
      {onClose && (
        <button onClick={onClose} className="opacity-70 hover:opacity-100 transition-opacity">
          <X size={20} />
        </button>
      )}
    </div>
  );
};

export default AlertBanner;
