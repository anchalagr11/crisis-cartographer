from typing import List, Dict, Any, Tuple
import math

# Centroids for common regions in the dataset (ISO 3166-1 alpha-2)
COUNTRY_CENTROIDS = {
    "SD": (12.8628, 30.2176),  # Sudan
    "SY": (34.8021, 38.9968),  # Syria
    "RW": (-1.9403, 29.8739),  # Rwanda
    "BA": (43.9159, 17.6791),  # Bosnia
    "YE": (15.5527, 48.5164),  # Yemen
    "UA": (48.3794, 31.1656),  # Ukraine
    "PS": (31.9522, 35.2332),  # Palestine/Gaza
    "MM": (21.9162, 95.9560),  # Myanmar
    "ET": (9.1450, 40.4897),   # Ethiopia
    "CD": (-4.0383, 21.7587),  # DRC
    "HT": (18.9712, -72.2852), # Haiti
    "AF": (33.9391, 67.7100),  # Afghanistan
    "SS": (6.8770, 31.3070),   # South Sudan
    "SO": (5.1521, 46.1996),   # Somalia
    "IQ": (33.2232, 43.6793),  # Iraq
    "LY": (26.3351, 17.2283),  # Libya
    "LK": (7.8731, 80.7718),   # Sri Lanka
    "CO": (4.5709, -74.2973),  # Colombia
    "CF": (6.6111, 20.9394),   # CAR
}

def get_country_centroids(country_codes: List[str]) -> Dict[str, Tuple[float, float]]:
    """Return lat/lng for a list of country codes."""
    return {code: COUNTRY_CENTROIDS[code] for code in country_codes if code in COUNTRY_CENTROIDS}

def haversine_distance(coord1: Tuple[float, float], coord2: Tuple[float, float]) -> float:
    """Calculate the great-circle distance between two points in kilometers."""
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    R = 6371  # Earth radius in km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def calculate_geospatial_proximity(crisis_a_regions: List[str], crisis_b_regions: List[str]) -> Dict[str, Any]:
    """Analyze the geographical relationship between two crises."""
    shared_regions = list(set(crisis_a_regions) & set(crisis_b_regions))
    
    centroids_a = get_country_centroids(crisis_a_regions)
    centroids_b = get_country_centroids(crisis_b_regions)
    
    if not centroids_a or not centroids_b:
        return {
            "min_distance_km": None,
            "shared_regions": shared_regions,
            "geographical_overlap": len(shared_regions) > 0
        }
    
    # Calculate min distance between any two affected regions
    min_dist = float('inf')
    for c1 in centroids_a.values():
        for c2 in centroids_b.values():
            dist = haversine_distance(c1, c2)
            if dist < min_dist:
                min_dist = dist
                
    return {
        "min_distance_km": round(min_dist, 2),
        "shared_regions": shared_regions,
        "geographical_overlap": len(shared_regions) > 0,
        "is_adjacent": min_dist < 1000  # Arbitrary threshold for 'regional proximity'
    }
