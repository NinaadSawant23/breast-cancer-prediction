// DOM Elements
const predictionForm = document.getElementById('predictionForm');
const loadingSpinner = document.getElementById('loadingSpinner');
const resultModal = document.getElementById('resultModal');
const resultDisplay = document.getElementById('resultDisplay');
const closeModalBtn = document.getElementById('closeModalBtn');
const sampleValuesBtn = document.getElementById('sampleValues');
const probabilityBar = document.getElementById('probabilityBar');
const confidenceText = document.getElementById('confidenceText');

// Sample Values Loader
sampleValuesBtn.addEventListener('click', () => {
    // Define an array of sample cases
    const sampleValuesArray = [
        {
            radius_mean: 17.99,
            texture_mean: 10.38,
            perimeter_mean: 122.8,
            area_mean: 1001.0,
            smoothness_mean: 0.1184,
            compactness_mean: 0.2776,
            concavity_mean: 0.3001,
            concave_points_mean: 0.1471,
            symmetry_mean: 0.2419,
            fractal_dimension_mean: 0.07871,
            radius_se: 1.095,
            texture_se: 0.905,
            perimeter_se: 8.589,
            area_se: 153.4,
            smoothness_se: 0.006399,
            compactness_se: 0.04904,
            concavity_se: 0.05373,
            concave_points_se: 0.01587,
            symmetry_se: 0.03003,
            fractal_dimension_se: 0.006193,
            radius_worst: 25.38,
            texture_worst: 17.33,
            perimeter_worst: 184.6,
            area_worst: 2019.0,
            smoothness_worst: 0.1622,
            compactness_worst: 0.6656,
            concavity_worst: 0.7119,
            concave_points_worst: 0.2654,
            symmetry_worst: 0.4601,
            fractal_dimension_worst: 0.1189
        },
        {
            radius_mean: 12.34,
            texture_mean: 15.67,
            perimeter_mean: 80.12,
            area_mean: 500.0,
            smoothness_mean: 0.1,
            compactness_mean: 0.15,
            concavity_mean: 0.12,
            concave_points_mean: 0.08,
            symmetry_mean: 0.2,
            fractal_dimension_mean: 0.06,
            radius_se: 0.8,
            texture_se: 1.0,
            perimeter_se: 4.5,
            area_se: 40.0,
            smoothness_se: 0.005,
            compactness_se: 0.02,
            concavity_se: 0.03,
            concave_points_se: 0.01,
            symmetry_se: 0.02,
            fractal_dimension_se: 0.003,
            radius_worst: 15.0,
            texture_worst: 20.0,
            perimeter_worst: 100.0,
            area_worst: 800.0,
            smoothness_worst: 0.15,
            compactness_worst: 0.5,
            concavity_worst: 0.6,
            concave_points_worst: 0.2,
            symmetry_worst: 0.3,
            fractal_dimension_worst: 0.09
        },
        {
            radius_mean: 11.0,
            texture_mean: 13.5,
            perimeter_mean: 70.0,
            area_mean: 300.0,
            smoothness_mean: 0.1,
            compactness_mean: 0.1,
            concavity_mean: 0.05,
            concave_points_mean: 0.05,
            symmetry_mean: 0.2,
            fractal_dimension_mean: 0.06,
            // Standard Error (SE) Features
            radius_se: 0.5,
            texture_se: 1.0,
            perimeter_se: 2.0,
            area_se: 30.0,
            smoothness_se: 0.005,
            compactness_se: 0.02,
            concavity_se: 0.02,
            concave_points_se: 0.01,
            symmetry_se: 0.02,
            fractal_dimension_se: 0.003,
            // Worst Features (still on the lower side)
            radius_worst: 12.0,
            texture_worst: 15.0,
            perimeter_worst: 80.0,
            area_worst: 350.0,
            smoothness_worst: 0.12,
            compactness_worst: 0.15,
            concavity_worst: 0.1,
            concave_points_worst: 0.07,
            symmetry_worst: 0.25,
            fractal_dimension_worst: 0.07}
        // Add more sample objects as needed
    ];

    // Randomly select one sample
    const randomSample = sampleValuesArray[Math.floor(Math.random() * sampleValuesArray.length)];

    // Set all sample values in the form
    for (const [id, value] of Object.entries(randomSample)) {
        const input = document.getElementById(id);
        if (input) {
            input.value = value;
            // Trigger validation if needed
            input.dispatchEvent(new Event('input'));
        }
    }
});


// Form Submission Handler
predictionForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Validate before submission
    if (!validateAllInputs()) {
        showError('Please fill in all fields with valid positive numbers');
        return;
    }

    // Show loading spinner
    loadingSpinner.style.display = 'block';

    try {
        // Validate all inputs first
        if (!validateInputs()) {
            throw new Error('Please fill in all fields with valid numbers');
        }

        // Prepare form data
        const formData = new FormData(predictionForm);
        const data = {};

        // Convert to numbers and build data object
        formData.forEach((value, key) => {
            data[key] = parseFloat(value);
        });

        // Send prediction request
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams(data)
        });

        // Handle response
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Prediction request failed');
        }

        const result = await response.json();

        // Display results
        displayResult(result);
    } catch (error) {
        console.error('Prediction error:', error);
        showError(error.message);
    } finally {
        // Hide loading spinner
        loadingSpinner.style.display = 'none';
    }
});

// Input Validation
function validateInputs() {
    const inputs = document.querySelectorAll('input[type="number"]');
    let isValid = true;

    inputs.forEach(input => {
        const value = parseFloat(input.value);
        if (isNaN(value) || value < 0) {
            input.classList.add('invalid');
            isValid = false;
        } else {
            input.classList.remove('invalid');
        }
    });

    return isValid;
}

function validateAllInputs() {
    const requiredFields = [
        'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
        'smoothness_mean', 'compactness_mean', 'concavity_mean',
        'concave_points_mean', 'symmetry_mean', 'fractal_dimension_mean',
        'radius_se', 'texture_se', 'perimeter_se', 'area_se',
        'smoothness_se', 'compactness_se', 'concavity_se',
        'concave_points_se', 'symmetry_se', 'fractal_dimension_se',
        'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst',
        'smoothness_worst', 'compactness_worst', 'concavity_worst',
        'concave_points_worst', 'symmetry_worst', 'fractal_dimension_worst'
    ];

    let isValid = true;

    requiredFields.forEach(field => {
        const input = document.querySelector(`[name="${field}"]`);
        if (!input || input.value === '') {
            isValid = false;
            if (input) {
                input.classList.add('invalid');
                // Scroll to the first invalid field
                if (isValid) {
                    input.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
            }
        } else {
            const value = parseFloat(input.value);
            if (isNaN(value) || value < 0) {
                input.classList.add('invalid');
                isValid = false;
            } else {
                input.classList.remove('invalid');
            }
        }
    });

    if (!isValid) {
        showError('Please fill in all fields with valid positive numbers');
    }

    return isValid;
}

// Display Results
function displayResult(result) {
    const percentage = (result.probability * 100).toFixed(2);

    // Set result text
    resultDisplay.innerHTML = `
        <h3>Diagnosis: ${result.result}</h3>
        <p>Malignancy Probability: ${percentage}%</p>
    `;

    // Set result class for styling
    resultDisplay.className = `result-text ${result.result === 'Malignant' ? 'malignant' : 'benign'}`;

    // Update probability meter
    probabilityBar.style.width = `${percentage}%`;
    probabilityBar.style.backgroundColor = result.result === 'Malignant'
        ? `hsl(${120 - (result.probability * 120)}, 70%, 45%)`
        : `hsl(${result.probability * 120}, 70%, 45%)`;

    // Set confidence text
    confidenceText.textContent = `Confidence: ${result.confidence}`;
    confidenceText.style.color = result.confidence === 'high' ? '#2ecc71' : '#f39c12';

    // Show modal
    resultModal.style.display = 'block';
}

// Error Display
function showError(message) {
    resultDisplay.innerHTML = `<h3>Error</h3><p>${message}</p>`;
    resultDisplay.className = 'result-text error';
    probabilityBar.style.width = '0%';
    confidenceText.textContent = '';
    resultModal.style.display = 'block';
}

// Close Modal
closeModalBtn.addEventListener('click', () => {
    resultModal.style.display = 'none';
});

// Close modal when clicking outside
window.addEventListener('click', (event) => {
    if (event.target === resultModal) {
        resultModal.style.display = 'none';
    }
});

// Real-time input validation
document.querySelectorAll('input[type="number"]').forEach(input => {
    input.addEventListener('input', function() {
        const value = parseFloat(this.value);
        if (isNaN(value) || value < 0) {
            this.classList.add('invalid');
        } else {
            this.classList.remove('invalid');
        }
    });
});