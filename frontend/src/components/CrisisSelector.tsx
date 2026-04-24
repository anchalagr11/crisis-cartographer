import React, { useState, useEffect } from 'react';
import { getCrises } from '../services/api';

interface CrisisSelectorProps {
  label: string;
  selectedId: string;
  onSelect: (id: string) => void;
}

const CrisisSelector: React.FC<CrisisSelectorProps> = ({ label, selectedId, onSelect }) => {
  const [crises, setCrises] = useState<any[]>([]);

  useEffect(() => {
    getCrises().then(setCrises).catch(console.error);
  }, []);

  return (
    <div className="flex flex-col space-y-2">
      <label className="text-sm font-semibold text-gray-600 uppercase tracking-wider">{label}</label>
      <select
        value={selectedId}
        onChange={(e) => onSelect(e.target.value)}
        className="block w-full px-4 py-3 bg-white border border-gray-200 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-crisis-accent focus:border-transparent transition-all duration-200 appearance-none cursor-pointer"
      >
        <option value="">Select a Crisis</option>
        {crises.map((c) => (
          <option key={c.crisis_id} value={c.crisis_id}>
            {c.name}
          </option>
        ))}
      </select>
    </div>
  );
};

export default CrisisSelector;
