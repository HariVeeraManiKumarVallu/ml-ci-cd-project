# ML CI/CD Project

## Overview
This project implements a Continuous Integration and Continuous Deployment (CI/CD) pipeline for machine learning models using GitHub Actions. The primary focus is on training and evaluating a RandomForestClassifier on the Iris dataset.

## Project Structure
```
ml-ci-cd-project/
├── .github/
│   └── workflows/
│       └── ci.yml          # CI/CD workflow configuration
├── data/                   # Directory for datasets
├── models/                 # Directory for saving trained models
├── src/                    # Source code for training and evaluation
│   ├── train.py            # Script to train the model
│   ├── evaluate.py         # Script to evaluate the model
│   ├── app.py              # FastAPI application
│   └── utils.py            # Utility functions
├── tests/                  # Directory for tests
│   ├── test_api.py         # API endpoint tests
│   ├── test_evaluate.py    # Evaluation tests
│   ├── test_predict.py     # Model prediction tests
│   ├── test_train.py       # Model training tests
│   └── test_utils.py       # Utility function tests
├── requirements.txt        # Python dependencies
├── evaluation.txt          # Model evaluation report (generated)
└── README.md               # Project documentation
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd ml-ci-cd-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
- To train the model, run:
  ```
  python src/train.py
  ```

- To evaluate the model, run:
  ```
  python src/evaluate.py
  ```

## API Usage

- Start the API server:
  ```
  uvicorn src.app:app --reload
  ```
- Access the interactive API documentation at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### `/predict` Endpoint

- **Method:** POST  
- **URL:** `/predict`  
- **Request Body:**  
  ```json
  {
    "data": [5.1, 3.5, 1.4, 0.2]
  }
  ```
- **Response:**  
  ```json
  {
    "prediction": 0
  }
  ```

### `/health` Endpoint

- **Method:** GET  
- **URL:** `/health`  
- **Response:**  
  ```json
  {
    "status": "ok"
  }
  ```

### `/model-info` Endpoint

- **Method:** GET  
- **URL:** `/model-info`  
- **Response Example:**  
  ```json
  {
    "version": "1.0",
    "trained_on": "2025-05-31T12:34:56"
  }
  ```

## CI/CD Pipeline
The CI/CD pipeline is defined in `.github/workflows/ci.yml`. It automatically triggers on pushes and pull requests to the main branch, ensuring that tests are run, the model is trained, and evaluation reports are generated. Artifacts such as the trained model, evaluation report, and coverage report are uploaded for review.

## Testing
To run the tests, use:
```
pytest tests/
```
To check test coverage:
```
pytest --cov=src tests/
```

## License
This project is licensed under the MIT License.