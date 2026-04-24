import React from 'react';

interface ForecastData {
  casualties: number;
  displacement: number;
  trend: string;
  confidence_score: number;
  risk_factors: string[];
}

interface ForecastCardProps {
  crisisName: string;
  forecast: ForecastData;
  color: 'primary' | 'accent';
}

const ForecastCard: React.FC<ForecastCardProps> = ({ crisisName, forecast, color }) => {
  const isPrimary = color === 'primary';
  
  return (
    <div className={`p-6 rounded-3xl border ${isPrimary ? 'bg-blue-50 border-blue-100' : 'bg-teal-50 border-teal-100'}`}>
      <div className="flex justify-between items-start mb-6">
        <div>
          <h4 className={`text-xs font-black uppercase tracking-widest ${isPrimary ? 'text-crisis-primary' : 'text-crisis-accent'}`}>
            12-Month Projection
          </h4>
          <h3 className="text-lg font-black text-gray-900 truncate max-w-[200px]">{crisisName}</h3>
        </div>
        <div className={`px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-tighter ${forecast.trend === 'escalating' ? 'bg-red-100 text-red-600' : 'bg-green-100 text-green-600'}`}>
          {forecast.trend}
        </div>
      </div>

      <div className="grid grid-cols-2 gap-4 mb-6">
        <div>
          <div className="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-1">Proj. Casualties</div>
          <div className="text-xl font-black text-gray-900">{forecast.casualties.toLocaleString()}</div>
        </div>
        <div>
          <div className="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-1">Proj. Displacement</div>
          <div className="text-xl font-black text-gray-900">{forecast.displacement.toLocaleString()}</div>
        </div>
      </div>

      <div className="space-y-2">
        <div className="flex justify-between items-center mb-1">
          <span className="text-[10px] font-bold text-gray-400 uppercase tracking-widest">Confidence Score</span>
          <span className="text-[10px] font-black text-gray-700">{Math.round(forecast.confidence_score * 100)}%</span>
        </div>
        <div className="w-full bg-gray-200 rounded-full h-1">
          <div 
            className={`h-1 rounded-full ${isPrimary ? 'bg-crisis-primary' : 'bg-crisis-accent'}`} 
            style={{ width: `${forecast.confidence_score * 100}%` }}
          ></div>
        </div>
      </div>

      {forecast.risk_factors.length > 0 && (
        <div className="mt-6 pt-6 border-t border-white/50">
          <h5 className="text-[10px] font-black text-gray-400 uppercase tracking-widest mb-2">Key Risk Factors</h5>
          <ul className="space-y-2">
            {forecast.risk_factors.map((risk, idx) => (
              <li key={idx} className="text-[10px] font-medium text-gray-600 leading-relaxed flex gap-2">
                <span className={isPrimary ? 'text-crisis-primary' : 'text-crisis-accent'}>•</span>
                {risk}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default ForecastCard;
