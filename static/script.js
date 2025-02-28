document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('studentForm');
    const messageDiv = document.getElementById('message');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission (page reload)

        const formData = new FormData(form); // Get form data
        
        // Convert FormData to JSON if needed
        const jsonData = {};
        formData.forEach((value, key) => {
            jsonData[key] = value;
        });

        fetch('/submit-form', { // Send POST request to the backend endpoint
            method: 'POST',
            body: formData
            // If sending JSON data:
            // headers: {
            //     'Content-Type': 'application/json'
            // },
            // body: JSON.stringify(jsonData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json(); // Parse response as JSON
        })
        .then(data => {
            messageDiv.textContent = data.message; // Display message from backend
            messageDiv.className = 'success'; // Add success class for styling
            form.reset(); // Clear the form
        })
        .catch(error => {
            console.error('Error:', error);
            messageDiv.textContent = 'Error submitting data. Please try again.';
            messageDiv.className = 'error'; // Add error class for styling
        });
    });
});
