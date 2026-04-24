import pytest
import os
from backend.app.services import data_loader
from backend.app.models.crisis import Crisis


def test_load_all_crises():
    crises = data_loader.load_all_crises()
    assert len(crises) >= 5
    ids = [c.crisis_id for c in crises]
    assert "darfur-2003" in ids
    assert "syria-2011" in ids
    assert "rwanda-1994" in ids
    assert "bosnia-1992" in ids
    assert "yemen-2014" in ids


def test_load_specific_crisis():
    crisis = data_loader.load_crisis("syria-2011")
    assert isinstance(crisis, Crisis)
    assert crisis.name == "Syrian Civil War"
    assert crisis.status == "active"


def test_load_nonexistent_crisis():
    with pytest.raises(FileNotFoundError):
        data_loader.load_crisis("nonexistent-9999")
