import json
import os
from typing import List
from ..models.crisis import Crisis

DATA_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../data/crises")
)


def load_crisis(crisis_id: str) -> Crisis:
    file_path = os.path.join(DATA_DIR, f"{crisis_id}.json")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Crisis file not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return Crisis(**data)


def load_all_crises() -> List[Crisis]:
    crises = []
    if not os.path.exists(DATA_DIR):
        return []
    for file in os.listdir(DATA_DIR):
        if file.endswith(".json"):
            crisis_id = file[:-5]
            try:
                crises.append(load_crisis(crisis_id))
            except Exception as e:
                print(f"Error loading {file}: {e}")
    return crises
