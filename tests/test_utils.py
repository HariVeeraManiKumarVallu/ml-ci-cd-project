from sklearn.datasets import load_iris
import numpy as np

def test_data_shape():
    X, y = load_iris(return_X_y=True)
    assert X.shape[0] == len(y)