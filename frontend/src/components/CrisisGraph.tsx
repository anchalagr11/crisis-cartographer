import React from 'react';

interface SimilarCrisis {
  crisis_id: string;
  name: string;
  similarity_score: number;
  common_tags: string[];
}

interface CrisisGraphProps {
  mainCrisis: string;
  similarCrises: SimilarCrisis[];
}

const CrisisGraph: React.FC<CrisisGraphProps> = ({ mainCrisis, similarCrises }) => {
  return (
    <div className="bg-white rounded-3xl p-8 shadow-sm border border-gray-100 mt-8">
      <div className="mb-8 text-center md:text-left">
        <h2 className="text-2xl font-black text-crisis-primary tracking-tight">Relational Network</h2>
        <p className="text-sm text-gray-400 font-medium mt-1">Cross-crisis structural similarities</p>
      </div>

      <div className="relative h-[300px] flex items-center justify-center">
        {/* Main Node */}
        <div className="z-10 bg-crisis-primary text-white p-6 rounded-3xl shadow-xl border-4 border-white transform hover:scale-105 transition-transform cursor-pointer">
          <span className="font-black text-sm uppercase tracking-widest">{mainCrisis}</span>
        </div>

        {/* SVG Connections */}
        <svg className="absolute inset-0 w-full h-full pointer-events-none">
          {similarCrises.map((_, idx) => {
            const angle = (idx * (360 / similarCrises.length)) * (Math.PI / 180);
            const x2 = 50 + 35 * Math.cos(angle);
            const y2 = 50 + 35 * Math.sin(angle);
            return (
              <line 
                key={idx}
                x1="50%" y1="50%" 
                x2={`${x2}%`} y2={`${y2}%`} 
                stroke="#e2e8f0" 
                strokeWidth="2" 
                strokeDasharray="5,5" 
              />
            );
          })}
        </svg>

        {/* Similar Nodes */}
        {similarCrises.map((crisis, idx) => {
          const angle = (idx * (360 / similarCrises.length)) * (Math.PI / 180);
          const x = 50 + 35 * Math.cos(angle);
          const y = 50 + 35 * Math.sin(angle);
          
          return (
            <div 
              key={crisis.crisis_id}
              className="absolute z-10 group"
              style={{ left: `${x}%`, top: `${y}%`, transform: 'translate(-50%, -50%)' }}
            >
              <div className="bg-white border-2 border-gray-100 p-4 rounded-2xl shadow-sm hover:border-crisis-accent transition-colors cursor-help">
                <div className="text-[10px] font-black text-crisis-accent uppercase tracking-tighter mb-1">
                  {Math.round(crisis.similarity_score * 100)}% Similar
                </div>
                <div className="text-xs font-bold text-gray-700 truncate max-w-[100px]">
                  {crisis.name}
                </div>
              </div>
              
              {/* Tooltip on hover */}
              <div className="hidden group-hover:block absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2 w-48 bg-gray-900 text-white p-3 rounded-xl text-[10px] z-50 shadow-2xl">
                <p className="font-bold mb-1 uppercase tracking-widest text-crisis-accent">Common Drivers</p>
                <div className="flex flex-wrap gap-1">
                  {crisis.common_tags.map(tag => (
                    <span key={tag} className="bg-white/10 px-1.5 py-0.5 rounded uppercase">#{tag}</span>
                  ))}
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default CrisisGraph;
