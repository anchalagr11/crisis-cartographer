import React, { useState } from 'react';

interface TimelineEvent {
  date: string;
  relative_month: number;
  description: string;
  type: string;
}

interface ParallelTimelineProps {
  crisisA: string;
  crisisB: string;
  eventsA: TimelineEvent[];
  eventsB: TimelineEvent[];
}

const ParallelTimeline: React.FC<ParallelTimelineProps> = ({ crisisA, crisisB, eventsA, eventsB }) => {
  const [useRelative, setUseRelative] = useState(true);

  // Combine and sort events for the combined view
  const allEvents = [...eventsA.map(e => ({ ...e, crisis: 'A' })), ...eventsB.map(e => ({ ...e, crisis: 'B' }))]
    .sort((a, b) => useRelative ? a.relative_month - b.relative_month : new Date(a.date).getTime() - new Date(b.date).getTime());

  return (
    <div className="bg-white rounded-3xl p-8 shadow-sm border border-gray-100 mt-8">
      <div className="flex justify-between items-center mb-8">
        <div>
          <h2 className="text-2xl font-black text-crisis-primary tracking-tight">Temporal Mapping</h2>
          <p className="text-sm text-gray-400 font-medium mt-1">Comparing event progression and intensity</p>
        </div>
        <div className="flex bg-gray-100 p-1 rounded-xl">
          <button 
            onClick={() => setUseRelative(true)}
            className={`px-4 py-2 text-xs font-bold uppercase tracking-widest rounded-lg transition-all ${useRelative ? 'bg-white text-crisis-primary shadow-sm' : 'text-gray-400 hover:text-gray-600'}`}
          >
            Relative
          </button>
          <button 
            onClick={() => setUseRelative(false)}
            className={`px-4 py-2 text-xs font-bold uppercase tracking-widest rounded-lg transition-all ${!useRelative ? 'bg-white text-crisis-primary shadow-sm' : 'text-gray-400 hover:text-gray-600'}`}
          >
            Absolute
          </button>
        </div>
      </div>

      <div className="relative pt-8 pb-12">
        {/* Timeline Axis */}
        <div className="absolute left-1/2 transform -translate-x-1/2 h-full w-0.5 bg-gray-100 hidden md:block"></div>
        
        <div className="space-y-12">
          {allEvents.map((event, idx) => (
            <div key={idx} className={`flex items-center w-full ${event.crisis === 'A' ? 'flex-row md:flex-row-reverse' : 'flex-row'}`}>
              <div className="w-full md:w-1/2 flex px-4">
                <div className={`p-5 rounded-2xl border ${event.crisis === 'A' ? 'bg-blue-50 border-blue-100' : 'bg-teal-50 border-teal-100'} w-full relative`}>
                  {/* Connector Dot */}
                  <div className={`absolute top-1/2 w-3 h-3 rounded-full border-2 border-white shadow-sm hidden md:block ${event.crisis === 'A' ? 'right-[-22px] bg-crisis-primary' : 'left-[-22px] bg-crisis-accent'}`}></div>
                  
                  <div className="flex justify-between items-start mb-2">
                    <span className={`text-[10px] font-black uppercase tracking-tighter px-2 py-0.5 rounded-md ${event.crisis === 'A' ? 'bg-crisis-primary text-white' : 'bg-crisis-accent text-white'}`}>
                      {useRelative ? `Month ${event.relative_month}` : event.date}
                    </span>
                    <span className="text-[10px] font-bold text-gray-400 uppercase tracking-widest">{event.type}</span>
                  </div>
                  <p className="text-sm font-medium text-gray-700 leading-relaxed">{event.description}</p>
                </div>
              </div>
              <div className="hidden md:block md:w-1/2"></div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default ParallelTimeline;
