import React from 'react';
import { MapContainer, TileLayer, Marker, Popup, Polyline, Circle } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

// Fix for default marker icons in Leaflet + React
// @ts-ignore
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon-2x.png',
  iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
});

interface CrisisMapProps {
  crisisA: string;
  crisisB: string;
  coordsA: Record<string, [number, number]>;
  coordsB: Record<string, [number, number]>;
  geoMetrics: any;
}

const CrisisMap: React.FC<CrisisMapProps> = ({ crisisA, crisisB, coordsA, coordsB, geoMetrics }) => {
  const allCoords = [...Object.values(coordsA), ...Object.values(coordsB)];
  
  // Calculate center of all points or default to world center
  const center: [number, number] = allCoords.length > 0 
    ? [
        allCoords.reduce((sum, c) => sum + c[0], 0) / allCoords.length,
        allCoords.reduce((sum, c) => sum + c[1], 0) / allCoords.length
      ]
    : [20, 0];

  return (
    <div className="bg-white rounded-3xl p-8 shadow-sm border border-gray-100 mt-8">
      <div className="flex justify-between items-center mb-8">
        <div>
          <h2 className="text-2xl font-black text-crisis-primary tracking-tight">Geospatial Context</h2>
          <p className="text-sm text-gray-400 font-medium mt-1">Regional impact and proximity analysis</p>
        </div>
        {geoMetrics?.min_distance_km !== null && (
          <div className="bg-blue-50 px-4 py-2 rounded-xl border border-blue-100">
            <span className="text-xs font-bold text-crisis-primary uppercase tracking-widest">
              Distance: {geoMetrics.min_distance_km.toLocaleString()} km
            </span>
          </div>
        )}
      </div>

      <div className="h-[500px] w-full rounded-2xl overflow-hidden border border-gray-100 shadow-inner z-0">
        <MapContainer center={center} zoom={2} style={{ height: '100%', width: '100%' }}>
          <TileLayer
            url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png"
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
          />
          
          {/* Crisis A Regions */}
          {Object.entries(coordsA).map(([code, pos]) => (
            <Circle 
              key={`a-${code}`}
              center={pos}
              radius={200000}
              pathOptions={{ fillColor: '#1a365d', color: '#1a365d', fillOpacity: 0.4 }}
            >
              <Popup>
                <div className="font-bold">{crisisA}</div>
                <div className="text-xs text-gray-500">Affected Region: {code}</div>
              </Popup>
            </Circle>
          ))}

          {/* Crisis B Regions */}
          {Object.entries(coordsB).map(([code, pos]) => (
            <Circle 
              key={`b-${code}`}
              center={pos}
              radius={200000}
              pathOptions={{ fillColor: '#38b2ac', color: '#38b2ac', fillOpacity: 0.4 }}
            >
              <Popup>
                <div className="font-bold">{crisisB}</div>
                <div className="text-xs text-gray-500">Affected Region: {code}</div>
              </Popup>
            </Circle>
          ))}

          {/* Proximity Line if adjacent */}
          {geoMetrics?.min_distance_km < 3000 && allCoords.length >= 2 && (
             <Polyline 
                positions={[Object.values(coordsA)[0], Object.values(coordsB)[0]]}
                pathOptions={{ color: '#cbd5e0', dashArray: '5, 10' }}
             />
          )}
        </MapContainer>
      </div>

      <div className="mt-6 grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="p-4 bg-gray-50 rounded-2xl border border-gray-100">
          <h4 className="text-xs font-bold text-gray-400 uppercase tracking-widest mb-2">Regional Connectivity</h4>
          <p className="text-sm text-gray-700 font-medium">
            {geoMetrics?.shared_regions.length > 0 
              ? `Direct overlap in ${geoMetrics.shared_regions.join(', ')}.` 
              : geoMetrics?.is_adjacent 
                ? "Crises occur in adjacent or neighboring regions, suggesting possible regional spillover."
                : "Crises are geographically isolated from each other."}
          </p>
        </div>
        <div className="p-4 bg-gray-50 rounded-2xl border border-gray-100">
          <h4 className="text-xs font-bold text-gray-400 uppercase tracking-widest mb-2">Geospatial Scale</h4>
          <p className="text-sm text-gray-700 font-medium">
            Crisis Alpha affects {Object.keys(coordsA).length} regions while Crisis Beta affects {Object.keys(coordsB).length} regions.
          </p>
        </div>
      </div>
    </div>
  );
};

export default CrisisMap;
