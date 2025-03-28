document.getElementById('predictionForm').addEventListener('submit', function(e) {
        e.preventDefault();

        // Show loading spinner
        document.getElementById('loadingSpinner').style.display = 'block';

        // Collect form data
        const formData = new FormData(this);
        const data = {};
        formData.forEach((value, key) => data[key] = value);

        // Send to server
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams(data).toString()
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Display result in modal
            const resultDisplay = document.getElementById('resultDisplay');
            resultDisplay.textContent = data.result;

            // Set appropriate class based on result
            resultDisplay.className = data.result.includes('Benign') ?
                'result-text benign' : 'result-text malignant';

            // Show modal
            document.getElementById('resultModal').style.display = 'block';
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        })
        .finally(() => {
            // Hide loading spinner
            document.getElementById('loadingSpinner').style.display = 'none';
        });
    });

    // Improved close button handling
    document.addEventListener('DOMContentLoaded', function() {
        const closeButton = document.getElementById('closeModal');
        const modal = document.getElementById('resultModal');

        if (closeButton) {
            closeButton.addEventListener('click', function() {
                modal.style.display = 'none';
            });
        }

        window.addEventListener('click', function(event) {
            if (event.target === modal) {
                modal.style.display = 'none';
            }
        });
    });