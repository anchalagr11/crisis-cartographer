import json
import os
from ..models.crisis import Crisis

DATA_DIR = os.path.join(os.path.dirname(__file__), '../../data/crises')

def load_crisis(crisis_id: str) -> Crisis:
    file_path = os.path.join(DATA_DIR, f"{crisis_id}.json")
    with open(file_path, 'r') as f:
        data = json.load(f)
    return Crisis(**data)

def load_all_crises() -> List[Crisis]:
    crises = []
    for file in os.listdir(DATA_DIR):
        if file.endswith('.json'):
            crisis_id = file[:-5]
            crises.append(load_crisis(crisis_id))
    return crises