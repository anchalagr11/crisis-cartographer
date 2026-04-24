import React from 'react';
import MetricCard from './MetricCard';
import ParallelTimeline from './ParallelTimeline';
import CrisisMap from './CrisisMap';
import CrisisGraph from './CrisisGraph';
import ForecastCard from './ForecastCard';

interface ComparisonViewProps {
  data: any;
}

const ComparisonView: React.FC<ComparisonViewProps> = ({ data }) => {
  const handleExport = () => {
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `Crisis_Report_${data.crisis_a}_vs_${data.crisis_b}.json`;
    a.click();
  };

  if (!data) return null;

  return (
    <div className="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Comparison Summary */}
        <div className="lg:col-span-3 bg-white rounded-3xl p-8 shadow-sm border border-gray-100 mb-8">
          <div className="flex flex-col md:flex-row justify-between items-center mb-8 gap-4">
            <h2 className="text-4xl font-black text-crisis-primary tracking-tight">
              {data.crisis_a} <span className="text-gray-300 mx-2">vs</span> {data.crisis_b}
            </h2>
            <div className="flex items-center space-x-4">
              <div className="flex items-center space-x-2 bg-green-50 px-4 py-2 rounded-full border border-green-100">
                <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
                <span className="text-xs font-bold text-green-700 uppercase tracking-widest">Live Analysis</span>
              </div>
              <button 
                onClick={handleExport}
                className="bg-gray-900 text-white px-6 py-2 rounded-xl font-bold text-[10px] uppercase tracking-widest hover:bg-crisis-primary transition-all shadow-lg hover:shadow-crisis-primary/20"
              >
                Export Report
              </button>
            </div>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-12">
            <div className="space-y-4">
              <h3 className="text-sm font-bold text-gray-800 uppercase tracking-widest flex items-center">
                <span className="w-2 h-4 bg-crisis-primary rounded-sm mr-2"></span> Key Similarities
              </h3>
              <ul className="space-y-3">
                {data.key_similarities.map((s: string, i: number) => (
                  <li key={i} className="flex items-start">
                    <svg className="h-5 w-5 text-green-500 mr-2 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                    <span className="text-gray-600 font-medium">{s}</span>
                  </li>
                ))}
              </ul>
            </div>
            <div className="space-y-4">
              <h3 className="text-sm font-bold text-gray-800 uppercase tracking-widest flex items-center">
                <span className="w-2 h-4 bg-crisis-accent rounded-sm mr-2"></span> Key Differences
              </h3>
              <ul className="space-y-3">
                {data.key_differences.map((d: string, i: number) => (
                  <li key={i} className="flex items-start">
                    <svg className="h-5 w-5 text-crisis-accent mr-2 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                    </svg>
                    <span className="text-gray-600 font-medium">{d}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>

        {/* Metric Cards */}
        <MetricCard 
          label="Structural Similarity" 
          valueA={(data.metrics.tag_similarity * 100).toFixed(0)} 
          valueB="%" 
          unit="Jaccard Coefficient"
        />
        <MetricCard 
          label="Timeline Overlap" 
          valueA={(data.metrics.timeline_overlap * 100).toFixed(0)} 
          valueB="%" 
          unit="Temporal Intersection"
        />
        <MetricCard 
          label="Intensity Gap" 
          valueA={data.metrics.casualty_ratio.toFixed(2)} 
          valueB="Ratio" 
          unit="Casualty Intensity"
          ratio={data.metrics.casualty_ratio}
        />
      </div>

      {/* Temporal Mapping */}
      {data.aligned_events && Object.keys(data.aligned_events).length >= 2 && (
        <ParallelTimeline 
          crisisA={data.crisis_a}
          crisisB={data.crisis_b}
          eventsA={data.aligned_events[Object.keys(data.aligned_events)[0]]}
          eventsB={data.aligned_events[Object.keys(data.aligned_events)[1]]}
        />
      )}

      {/* Geospatial Mapping */}
      {data.region_coordinates && Object.keys(data.region_coordinates).length >= 2 && (
        <CrisisMap 
          crisisA={data.crisis_a}
          crisisB={data.crisis_b}
          coordsA={data.region_coordinates[Object.keys(data.region_coordinates)[0]]}
          coordsB={data.region_coordinates[Object.keys(data.region_coordinates)[1]]}
          geoMetrics={data.metrics.geospatial_metrics}
        />
      )}

      {/* Relational Intelligence */}
      {data.recommendations && Object.keys(data.recommendations).length >= 2 && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <CrisisGraph 
            mainCrisis={data.crisis_a}
            similarCrises={data.recommendations[Object.keys(data.recommendations)[0]]}
          />
          <CrisisGraph 
            mainCrisis={data.crisis_b}
            similarCrises={data.recommendations[Object.keys(data.recommendations)[1]]}
          />
        </div>
      )}

      {/* Predictive Synthesis */}
      {data.forecasts && Object.keys(data.forecasts).length >= 2 && (
        <div className="mt-8">
          <div className="mb-8">
            <h2 className="text-2xl font-black text-crisis-primary tracking-tight">Predictive Synthesis</h2>
            <p className="text-sm text-gray-400 font-medium mt-1">Probabilistic trajectory forecasting (12-month window)</p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <ForecastCard 
              crisisName={data.crisis_a}
              forecast={data.forecasts[Object.keys(data.forecasts)[0]]}
              color="primary"
            />
            <ForecastCard 
              crisisName={data.crisis_b}
              forecast={data.forecasts[Object.keys(data.forecasts)[1]]}
              color="accent"
            />
          </div>
        </div>
      )}
    </div>
  );
};

export default ComparisonView;
