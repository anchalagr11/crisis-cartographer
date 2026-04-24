import pytest
from backend.app.services import normalization, similarity

def test_normalization_duration():
    # Sudan: 2023-04-15 to now (~0.9 years as of March 2024)
    duration = normalization.calculate_duration("2023-04-15", "2024-03-27")
    assert 0.9 <= duration <= 1.0

def test_jaccard_similarity():
    s1 = ["ethnic", "political"]
    s2 = ["political", "territorial"]
    # intersection: 1 (political), union: 3 (ethnic, political, territorial)
    # 1/3 = 0.33
    sim = similarity.calculate_jaccard_similarity(s1, s2)
    assert sim == 0.33

def test_timeline_overlap():
    # Crisis A: 2010-2015
    # Crisis B: 2012-2017
    # Overlap: 2012-2015 (3 years)
    # Total span: 2010-2017 (7 years)
    # Ratio: 3/7 = 0.43
    overlap = similarity.calculate_timeline_overlap("2010-01-01", "2015-01-01", "2012-01-01", "2017-01-01")
    assert overlap == 0.43

def test_metric_ratio():
    assert similarity.calculate_metric_ratio(100, 200) == 0.5
    assert similarity.calculate_metric_ratio(500, 100) == 0.2
    assert similarity.calculate_metric_ratio(0, 0) == 1.0
