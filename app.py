from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the form
    features = [
        float(request.form['clump_thickness']),
        float(request.form['cell_size']),
        float(request.form['cell_shape']),
        float(request.form['marginal_adhesion']),
        float(request.form['epithelial_size']),
        float(request.form['bare_nuclei']),
        float(request.form['bland_chromatin']),
        float(request.form['normal_nucleoli']),
        float(request.form['mitoses'])
    ]

    # Prediction
    prediction = model.predict([features])[0]

    # Return JSON response using jsonify
    return jsonify({
        'result': "Malignant (Cancerous)" if prediction == 4 else "Benign (Non-Cancerous)"
    })

if __name__ == '__main__':
    app.run(debug=True)