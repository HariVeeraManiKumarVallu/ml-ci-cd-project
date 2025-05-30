# ML CI/CD Project

## Overview
This project implements a Continuous Integration and Continuous Deployment (CI/CD) pipeline for machine learning models using GitHub Actions. The primary focus is on training and evaluating a RandomForestClassifier on the Iris dataset.

## Project Structure
```
ml-ci-cd-project/
├── .github/
│   └── workflows/
│       └── ci.yml          # CI/CD workflow configuration
├── data/                    # Directory for datasets
├── models/                  # Directory for saving trained models
├── src/                     # Source code for training and evaluation
│   ├── train.py             # Script to train the model
│   ├── evaluate.py          # Script to evaluate the model
│   └── utils.py             # Utility functions (to be implemented)
├── tests/                   # Directory for tests
│   └── test_utils.py        # Unit tests for the project
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
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

## CI/CD Pipeline
The CI/CD pipeline is defined in `.github/workflows/ci.yml`. It automatically triggers on pushes and pull requests to the main branch, ensuring that tests are run, the model is trained, and evaluation reports are generated.

## Testing
To run the tests, use:
```
pytest tests/
```

## License
This project is licensed under the MIT License.