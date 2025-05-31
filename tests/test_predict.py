import joblib
import numpy as np
import pytest

def test_model_predict_shape():
    model = joblib.load("models/model.pkl")
    sample = np.array([[5.1, 3.5, 1.4, 0.2]])
    prediction = model.predict(sample)
    assert prediction.shape == (1,), "Prediction output shape is incorrect."

def test_model_predict_invalid_input():
    model = joblib.load("models/model.pkl")
    with pytest.raises(ValueError):
        model.predict(np.array([[1.0, 2.0]]))  # Invalid shape