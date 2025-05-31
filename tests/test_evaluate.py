import json
import os

def test_evaluation_file_exists():
    assert os.path.exists("evaluation.txt"), "Evaluation report does not exist."

def test_evaluation_file_format():
    with open("evaluation.txt") as f:
        report = json.load(f)
    assert "accuracy" in report, "Evaluation report missing accuracy."