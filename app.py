from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__, static_folder='static', template_folder='templates')

# Load the trained model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

FEATURE_NAMES = [
    'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
    'smoothness_mean', 'compactness_mean', 'concavity_mean',
    'concave_points_mean', 'symmetry_mean', 'fractal_dimension_mean',
    'radius_se', 'texture_se', 'perimeter_se', 'area_se',
    'smoothness_se', 'compactness_se', 'concavity_se',
    'concave_points_se', 'symmetry_se', 'fractal_dimension_se',
    'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst',
    'smoothness_worst', 'compactness_worst', 'concavity_worst',
    'concave_points_worst', 'symmetry_worst', 'fractal_dimension_worst'
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get all features from form data with validation
        missing_fields = [field for field in FEATURE_NAMES if field not in request.form]
        if missing_fields:
            return jsonify({
                'error': f'Missing fields: {", ".join(missing_fields)}',
                'missing_fields': missing_fields
            }), 400

        features = []
        for feature in FEATURE_NAMES:
            value = request.form.get(feature)
            try:
                features.append(float(value))
            except ValueError:
                return jsonify({
                    'error': f'Invalid number for {feature}',
                    'invalid_field': feature
                }), 400
            if value is None or value == '':
                return jsonify({'error': f'Missing value for {feature}'}), 400

        features_array = np.array(features).reshape(1, -1)

        scaled_features = scaler.transform(features_array)

        prediction = model.predict(scaled_features)[0]
        probability = model.predict_proba(scaled_features)[0][1]

        return jsonify({
            'result': "Malignant" if prediction == 1 else "Benign",
            'probability': float(probability),
            'confidence': "high" if probability > 0.9 or probability < 0.1 else "medium"
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)