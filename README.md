## Breast Cancer Prediction Web Application

![ML](https://img.shields.io/badge/Machine-Learning-blueviolet)
![Model](https://img.shields.io/badge/Model-Logistic_Regression-yellowgreen)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange)
![Accuracy](https://img.shields.io/badge/Accuracy-96.5%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

An end-to-end machine learning solution that leverages the Wisconsin Diagnostic Breast Cancer dataset to predict tumor malignancy based on 30 numeric features. The project features advanced data processing, model training with logistic regression, and performance evaluation, with a Flask interface for real-time predictions

![Project Screenshot](/screenshots/UI.png)
## Features


- User-friendly web interface with form input
- Machine learning model (Logistic Regression) for predictions
- Modal-based result display
- Responsive design that works on all devices
- Clean, medical-themed UI


## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Machine Learning**: scikit-learn, Logistic Regression
- **Other**: joblib (model serialization)

## Dataset

- 569 instances
- 30 features 
- Binary classification (malignant/benign)
- Source: https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic

  
## Installation

1. Clone the repository:
   bash
   git clone https://github.com/NinaadSawant23/breast-cancer-prediction.git

2. cd breast-cancer-prediction
   
3. Create a virtual environment:
   bash
   python -m venv venv
   source venv/bin/activate   On Windows use venv\Scripts\activate
   
4. Install dependencies:
   bash
   pip install -r requirements.txt
   
5. Run the application:
   bash
   python app.py
   
6. Open your browser to:
   http://127.0.0.1:5000/ 

## Usage

1. Enter the following cell characteristics: (For Test: Click on "Load Sample Values")

   **Mean Features**
   - Radius Mean
   - Texture Mean
   - Perimeter Mean
   - Area Mean
   - Smoothness Mean
   - Compactness Mean
   - Concavity Mean
   - Concave Point Mean
   - Symmetry Mean
   - Fractal Dimension Mean
     
   **Standard Error (SE) Features**
   - Radius SE
   - Texture SE
   - Perimeter SE
   - Area SE
   - Smoothness SE
   - Compactness SE
   - Concavity SE
   - Concave Point SE
   - Symmetry SE
   - Fractal Dimension SE
  
   **Worst Features**
   - Radius Worst
   - Texture Worst
   - Perimeter Worst
   - Area Worst
   - Smoothness Worst
   - Compactness Worst
   - Concavity Worst
   - Concave Point Worst
   - Symmetry Worst
   - Fractal Dimension Worst

3. Click "Predict" to see the result

   
## Model Performance

- Accuracy: 96.5%
- Confusion Matrix:
  ```
  [[71, 1]
   [3, 39]]
  ```
- For more info: Navigate to `breast-cancer-prediction/ml_model/model_metrics.json`

## Screenshots
![Project Screenshot](/screenshots/UI.png)


![Project Screenshot](/screenshots/UI_2.png)


![Project Screenshot](/screenshots/Prediction.png)

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License

[MIT License](LICENSE)
