# Decision Tree Classifier with Hyperparameter Tuning

This project demonstrates building a decision tree classifier with hyperparameter tuning using scikit-learn and GridSearchCV.

## Introduction

The project includes the following components:

- **Decision Tree Classifier (`decision_tree_classifier.py`)**: This script loads a dataset (`Car_Safety.csv`), preprocesses the data, including encoding categorical features using ordinal encoding, performs hyperparameter tuning using GridSearchCV, and evaluates the model's performance.

## Dataset

- **Car_Safety.csv**: This CSV file contains data related to car safety features and decisions.

## Usage

1. **Data Preparation**: The dataset is loaded from the `Car_Safety.csv` file. The features (`X`) and target (`y`) are separated.

2. **Data Preprocessing**: Categorical features are encoded using ordinal encoding with the `category_encoders` library.

3. **Hyperparameter Tuning**: GridSearchCV is used to perform an exhaustive search over the hyperparameter grid defined in the `param_grid`. The best parameters and best estimator are obtained.

4. **Model Evaluation**: The model's accuracy score is calculated using the best estimator on the test data.

5. **Visualization**: A visualization of the decision tree is generated using `matplotlib` and `tree.plot_tree()`.

## Requirements

- Python 3.x
- pandas
- scikit-learn
- category_encoders
- matplotlib

## How to Run

1. Clone this repository to your local machine.

2. Install the required dependencies using pip:

    ```
    pip install pandas scikit-learn category_encoders matplotlib
    ```

3. Run the script `decision_tree_classifier.py`.

