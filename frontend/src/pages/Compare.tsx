import React from 'react';
import ComparisonView from '../components/ComparisonView';

const Compare: React.FC = () => {
  return (
    <div>
      <h1>Compare Crises</h1>
      <ComparisonView data={null} />
    </div>
  );
};

export default Compare;