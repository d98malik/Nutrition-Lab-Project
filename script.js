// script.js

async function sendMessage() {
    const inputBox = document.getElementById('input-box');
    const outputBox = document.getElementById('output-box');
    const message = inputBox.value.trim();
    
    if (message) {
        // Display the user message
        const userMessage = document.createElement('div');
        userMessage.textContent = `You: ${message}`;
        outputBox.appendChild(userMessage);
        
        // Clear input box
        inputBox.value = '';

        // Send message to the Flask API
        try {
            const response = await fetch('http://127.0.0.1:5000/message', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message }),
            });
            const data = await response.json();

            if (response.ok) {
                // Display the response message
                const responseMessage = document.createElement('div');
                responseMessage.textContent = `Chatbot: ${data.response}`;
                outputBox.appendChild(responseMessage);
            } else {
                // Handle errors
                const errorMessage = document.createElement('div');
                errorMessage.textContent = `Chatbot: ${data.response}`;
                outputBox.appendChild(errorMessage);
            }
        } catch (error) {
            console.error('Error:', error);
        }
        outputBox.scrollTop = outputBox.scrollHeight; // Scroll to the bottom
    }
}