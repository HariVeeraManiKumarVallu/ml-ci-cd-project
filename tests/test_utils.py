from sklearn.datasets import load_iris

def test_data_shape():
    X, y = load_iris(return_X_y=True)
    assert X.shape[0] == len(y)

def test_data_features():
    X, _ = load_iris(return_X_y=True)
    assert X.shape[1] == 4, "Iris dataset should have 4 features."