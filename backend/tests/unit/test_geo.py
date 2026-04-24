import pytest
from backend.app.services import geo_service

def test_haversine_distance():
    # London to Paris (roughly)
    london = (51.5074, -0.1278)
    paris = (48.8566, 2.3522)
    dist = geo_service.haversine_distance(london, paris)
    assert 300 < dist < 400

def test_get_country_centroids():
    centroids = geo_service.get_country_centroids(["SD", "SY", "XX"])
    assert "SD" in centroids
    assert "SY" in centroids
    assert "XX" not in centroids
    assert centroids["SD"] == (12.8628, 30.2176)

def test_calculate_geospatial_proximity():
    # Sudan and South Sudan (Adjacent)
    proximity = geo_service.calculate_geospatial_proximity(["SD"], ["SS"])
    assert proximity["min_distance_km"] < 1000
    assert proximity["is_adjacent"] is True
    
    # Sudan and Colombia (Far)
    proximity = geo_service.calculate_geospatial_proximity(["SD"], ["CO"])
    assert proximity["min_distance_km"] > 10000
    assert proximity["is_adjacent"] is False
