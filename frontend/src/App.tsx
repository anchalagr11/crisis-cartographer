import React, { useState } from 'react';
import CrisisSelector from './components/CrisisSelector';
import ComparisonView from './components/ComparisonView';
import { compareCrises } from './services/api';

const App: React.FC = () => {
  const [idA, setIdA] = useState('');
  const [idB, setIdB] = useState('');
  const [comparison, setComparison] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleCompare = async () => {
    if (!idA || !idB) {
      setError('Please select two crises to compare.');
      return;
    }
    if (idA === idB) {
      setError('Please select two different crises.');
      return;
    }

    setLoading(true);
    setError('');
    try {
      const result = await compareCrises([idA, idB]);
      setComparison(result);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'An error occurred while comparing crises.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col">
      {/* Header */}
      <nav className="bg-white border-b border-gray-100 py-6">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center">
          <div className="flex items-center space-x-3">
            <div className="w-10 h-10 bg-crisis-primary rounded-xl flex items-center justify-center shadow-lg transform -rotate-3 hover:rotate-0 transition-transform duration-300">
              <span className="text-white font-black text-xl italic">C</span>
            </div>
            <h1 className="text-2xl font-black text-crisis-primary tracking-tighter">
              Crisis<span className="text-crisis-accent">Cartographer</span>
            </h1>
          </div>
          <div className="hidden md:flex space-x-8 text-xs font-bold uppercase tracking-widest text-gray-400">
            <a href="#" className="hover:text-crisis-primary transition-colors">Explorer</a>
            <a href="#" className="hover:text-crisis-primary transition-colors">Methods</a>
            <a href="#" className="hover:text-crisis-primary transition-colors">Data</a>
          </div>
        </div>
      </nav>

      <main className="flex-grow">
        {/* Hero & Selection */}
        <section className="bg-white border-b border-gray-100 py-16">
          <div className="max-w-4xl mx-auto px-4 text-center">
            <h2 className="text-5xl font-black text-crisis-primary mb-6 leading-tight">
              Uncover hidden patterns in <br/>
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-crisis-primary to-crisis-accent">
                global crisis dynamics
              </span>
            </h2>
            <p className="text-lg text-gray-500 font-medium mb-12 max-w-2xl mx-auto leading-relaxed">
              Select any two historical or active crises to start a deterministic, schema-normalized comparison powered by our relational intelligence engine.
            </p>

            <div className="bg-gray-50 p-4 rounded-3xl border border-gray-100 shadow-sm max-w-3xl mx-auto">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <CrisisSelector label="Crisis Alpha" selectedId={idA} onSelect={setIdA} />
                <CrisisSelector label="Crisis Beta" selectedId={idB} onSelect={setIdB} />
              </div>
              <button
                onClick={handleCompare}
                disabled={loading}
                className="mt-6 w-full py-4 bg-crisis-primary text-white font-black uppercase tracking-widest rounded-2xl hover:bg-opacity-90 hover:scale-[1.01] active:scale-[0.99] transition-all duration-200 shadow-xl shadow-blue-900/10 disabled:bg-gray-400"
              >
                {loading ? 'Analyzing Data...' : 'Start Comparison Analysis'}
              </button>
            </div>

            {error && (
              <div className="mt-6 p-4 bg-red-50 text-red-600 rounded-xl border border-red-100 text-sm font-bold animate-shake">
                {error}
              </div>
            )}
          </div>
        </section>

        {/* Comparison Result */}
        {comparison && <ComparisonView data={comparison} />}
      </main>

      <footer className="bg-white border-t border-gray-100 py-12">
        <div className="max-w-7xl mx-auto px-4 text-center">
          <p className="text-xs font-bold text-gray-400 uppercase tracking-widest">
            © 2024 CrisisCartographer — Intelligence for a Complex World
          </p>
        </div>
      </footer>
    </div>
  );
};

export default App;