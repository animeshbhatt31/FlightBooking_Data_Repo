import json
from pathlib import Path


def load_test_data_file():
    file_path = Path(__file__).parent.parent / "All_test_data" / "testing_data.json"
    with open(file_path,"r",encoding="utf-8") as f:
        json_data = json.load(f)
        return json_data