import React from 'react';

interface MetricCardProps {
  label: string;
  valueA: number | string;
  valueB: number | string;
  unit?: string;
  ratio?: number;
}

const MetricCard: React.FC<MetricCardProps> = ({ label, valueA, valueB, unit, ratio }) => {
  return (
    <div className="bg-white p-6 rounded-2xl shadow-sm border border-gray-100 hover:shadow-md transition-shadow duration-300">
      <h3 className="text-xs font-bold text-gray-400 uppercase tracking-widest mb-4">{label}</h3>
      <div className="grid grid-cols-2 gap-8 items-end">
        <div className="flex flex-col">
          <span className="text-3xl font-extrabold text-crisis-primary">
            {typeof valueA === 'number' ? valueA.toLocaleString() : valueA}
          </span>
          <span className="text-xs text-gray-400 mt-1">{unit || ''}</span>
        </div>
        <div className="flex flex-col text-right">
          <span className="text-3xl font-extrabold text-crisis-accent">
            {typeof valueB === 'number' ? valueB.toLocaleString() : valueB}
          </span>
          <span className="text-xs text-gray-400 mt-1">{unit || ''}</span>
        </div>
      </div>
      {ratio !== undefined && (
        <div className="mt-6">
          <div className="h-2 w-full bg-gray-100 rounded-full overflow-hidden flex">
            <div 
              className="h-full bg-crisis-primary transition-all duration-500" 
              style={{ width: `${(1 / (1 + ratio)) * 100}%` }}
            />
            <div 
              className="h-full bg-crisis-accent transition-all duration-500" 
              style={{ width: `${(ratio / (1 + ratio)) * 100}%` }}
            />
          </div>
          <div className="flex justify-between text-[10px] font-bold text-gray-400 mt-2 uppercase tracking-tighter">
            <span>Crisis A Intensity</span>
            <span>Crisis B Intensity</span>
          </div>
        </div>
      )}
    </div>
  );
};

export default MetricCard;
