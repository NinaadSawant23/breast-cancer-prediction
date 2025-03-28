## Breast Cancer Prediction Web Application

![ML](https://img.shields.io/badge/Machine-Learning-blueviolet)
![Model](https://img.shields.io/badge/Model-Logistic_Regression-yellowgreen)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange)
![Accuracy](https://img.shields.io/badge/Accuracy-96.2%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

A Flask-based web application that predicts breast cancer (malignant/benign) based on cell characteristics using machine learning.

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

## Installation

1. Clone the repository:
   bash
   git clone https://github.com/your-username/breast-cancer-prediction.git
   cd breast-cancer-prediction
   
2. Create a virtual environment:
   bash
   python -m venv venv
   source venv/bin/activate   On Windows use venv\Scripts\activate
   
3. Install dependencies:
   bash
   pip install -r requirements.txt
   
4. Run the application:
   bash
   python app.py
   
5. Open your browser to:
   http://localhost:5000

## Usage

1. Enter the following cell characteristics (values 1-10):
   - Clump Thickness
   - Uniformity of Cell Size
   - Uniformity of Cell Shape
   - Marginal Adhesion
   - Single Epithelial Cell Size
   - Bare Nuclei
   - Bland Chromatin
   - Normal Nucleoli
   - Mitoses


2. Click "Predict" to see the result
## Model Performance

- Accuracy: 96.7%
- Confusion Matrix:
  ```
  [[84, 3]
   [3, 47]]
  ```

  

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License

[MIT License](LICENSE)
