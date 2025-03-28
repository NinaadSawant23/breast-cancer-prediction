import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import confusion_matrix, classification_report
from pathlib import Path
import json


def load_data(data_path):
    """Load and prepare the dataset"""
    dataset = pd.read_csv(data_path)
    X = dataset.iloc[:, 1:-1].values
    y = dataset.iloc[:, -1].values
    return X, y


def train_model(X_train, y_train, random_state=0):
    """Train and return a logistic regression model"""
    classifier = LogisticRegression(random_state=random_state)
    classifier.fit(X_train, y_train)
    return classifier


def evaluate_model(model, X_test, y_test):
    """Evaluate model performance"""
    y_pred = model.predict(X_test)

    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:")
    print(cm)

    # Classification report
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    return {
        'confusion_matrix': cm.tolist(),
        'classification_report': classification_report(y_test, y_pred, output_dict=True)
    }


def cross_validate(model, X, y, cv=10):
    """Perform cross validation"""
    accuracies = cross_val_score(estimator=model, X=X, y=y, cv=cv)
    print(f"\nCross Validation Accuracy: {accuracies.mean() * 100:.2f}%")
    print(f"Standard Deviation: {accuracies.std() * 100:.2f}%")
    return {
        'mean_accuracy': accuracies.mean(),
        'std_deviation': accuracies.std()
    }


def save_artifacts(model, metrics, model_path, metrics_path):
    """Save model and metrics"""
    # Save model
    joblib.dump(model, model_path)

    # Save metrics
    with open(metrics_path, 'w') as f:
        json.dump(metrics, f, indent=4)


def main():
    # Configuration
    DATA_PATH = '../data/breast_cancer.csv'
    MODEL_PATH = '../model.pkl'
    METRICS_PATH = '../model_metrics.json'
    TEST_SIZE = 0.2
    RANDOM_STATE = 0
    CV_FOLDS = 10

    # Create directories if they don't exist
    Path('../model').mkdir(exist_ok=True)

    # Load data
    X, y = load_data(DATA_PATH)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
    )

    # Train model
    model = train_model(X_train, y_train, RANDOM_STATE)

    # Evaluate model
    print("\nModel Evaluation:")
    test_metrics = evaluate_model(model, X_test, y_test)
    cv_metrics = cross_validate(model, X_train, y_train, CV_FOLDS)

    # Combine metrics
    metrics = {
        'test_metrics': test_metrics,
        'cross_validation_metrics': cv_metrics
    }

    # Save artifacts
    save_artifacts(model, metrics, MODEL_PATH, METRICS_PATH)
    print(f"\nModel and metrics saved to {MODEL_PATH} and {METRICS_PATH}")


if __name__ == '__main__':
    main()