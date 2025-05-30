from sklearn.datasets import load_iris
import joblib
from sklearn.metrics import classification_report
import json

X, y = load_iris(return_X_y=True)
model = joblib.load('models/model.pkl')
y_pred = model.predict(X)

report = classification_report(y, y_pred, output_dict=True)
print(report)

with open("evaluation.txt", "w") as f:
    json.dump(report, f, indent=4)