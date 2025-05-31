from sklearn.datasets import load_iris
from src.utils import some_processing_function

def test_data_shape():
    X, y = load_iris(return_X_y=True)
    assert X.shape[0] == len(y)

def test_data_features():
    X, _ = load_iris(return_X_y=True)
    assert X.shape[1] == 4, "Iris dataset should have 4 features."

def test_some_processing_function():
    result = some_processing_function([1, 2, 3])
    assert result == 6