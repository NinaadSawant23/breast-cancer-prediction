import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score
from sklearn.preprocessing import StandardScaler
import json

def load_data(data_path):
    """Load and prepare the Wisconsin Diagnostic dataset"""
    # Define column names as specified in the dataset documentation
    column_names = ['id', 'diagnosis'] + [f'{stat}_{feature}'
                                          for feature in ['radius', 'texture', 'perimeter', 'area',
                                                          'smoothness', 'compactness', 'concavity',
                                                          'concave_points', 'symmetry', 'fractal_dimension']
                                          for stat in ['mean', 'se', 'worst']]

    # Read data with explicit column names
    df = pd.read_csv(data_path, header=None, names=column_names)

    # Convert diagnosis to binary (Malignant = 1, Benign = 0)
    df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})

    X = df.drop(['id', 'diagnosis'], axis=1).values
    y = df['diagnosis'].values

    # Feature scaling
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    return X, y, scaler

def train_model(X_train, y_train, random_state=42):
    """Train and return a logistic regression model"""
    classifier = LogisticRegression(random_state=random_state, max_iter=1000)
    classifier.fit(X_train, y_train)
    return classifier


def evaluate_model(model, X_test, y_test):
    """Enhanced model evaluation"""
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    # Metrics
    cm = confusion_matrix(y_test, y_pred)
    cr = classification_report(y_test, y_pred, output_dict=True)
    roc_auc = roc_auc_score(y_test, y_proba)

    print("Confusion Matrix:")
    print(cm)
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    print(f"\nROC AUC Score: {roc_auc:.4f}")

    return {
        'confusion_matrix': cm.tolist(),
        'classification_report': cr,
        'roc_auc': roc_auc
    }


def save_artifacts(model, scaler, metrics, model_path, scaler_path, metrics_path):
    """Save all artifacts needed for production"""
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)
    with open(metrics_path, 'w') as f:
        json.dump(metrics, f, indent=4)

def cross_validate(model, X, y, cv=5):
    """Perform cross validation and return AUC scores"""
    cv_scores = cross_val_score(
        estimator=model,
        X=X,
        y=y,
        cv=cv,
        scoring='roc_auc'
    )
    print(f"\nCross Validation AUC: {cv_scores.mean():.4f} (±{cv_scores.std():.4f})")
    return cv_scores


def main():
    # Configuration
    DATA_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data"
    COLUMN_NAMES = ['id', 'diagnosis'] + [f'{stat}_{feature}'
                                          for feature in ['radius', 'texture', 'perimeter', 'area',
                                                          'smoothness', 'compactness', 'concavity',
                                                          'concave_points', 'symmetry', 'fractal_dimension']
                                          for stat in ['mean', 'se', 'worst']]

    MODEL_PATH = '../model.pkl'
    SCALER_PATH = '../scaler.pkl'
    METRICS_PATH = 'model_metrics.json'
    TEST_SIZE = 0.2
    RANDOM_STATE = 42
    CV_FOLDS = 5  # Reduced for better variance estimation

    # Load data
    X, y, scaler = load_data(DATA_URL)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )

    # Train model
    model = train_model(X_train, y_train, RANDOM_STATE)

    # Evaluate
    print("\nModel Evaluation:")
    test_metrics = evaluate_model(model, X_test, y_test)

    cv_scores = cross_validate(model, X_train, y_train, cv=CV_FOLDS)

    metrics = {
        'test_metrics': test_metrics,
        'cross_val_auc_scores': cv_scores.tolist(),  # Convert numpy array to list
        'cross_val_auc_mean': cv_scores.mean(),
        'cross_val_auc_std': cv_scores.std()
    }

    # Save artifacts
    save_artifacts(model, scaler, metrics, MODEL_PATH, SCALER_PATH, METRICS_PATH)
    print(f"\nArtifacts saved:")
    print(f"- Model: {MODEL_PATH}")
    print(f"- Scaler: {SCALER_PATH}")
    print(f"- Metrics: {METRICS_PATH}")

if __name__ == '__main__':
    main()