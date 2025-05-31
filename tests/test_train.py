import os
import joblib

def test_model_file_exists():
    assert os.path.exists("models/model.pkl"), "Trained model file does not exist."

def test_model_loadable():
    model = joblib.load("models/model.pkl")
    assert model is not None, "Model could not be loaded."