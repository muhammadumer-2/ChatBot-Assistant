const chatInput = document.getElementById('chat-input');
const sendButton = document.getElementById('send-button');
const chatLog = document.getElementById('chat-log');

// Function to send the user prompt
const sendPrompt = () => {
    const userPrompt = chatInput.value;
    if (userPrompt.trim() === "") {
        return; // Do nothing if the input is empty
    }
    chatInput.value = '';
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            user_prompt: userPrompt
        })
    })
    .then(response => response.json())
    .then(data => {
        const assistantResponse = data['assistant_response'];
        const chatUpdateHTML = `
            <li class="user">${userPrompt}</li>
            <li class="assistant">${assistantResponse}</li>
        `;
        chatLog.insertAdjacentHTML('beforeend', chatUpdateHTML);
    })
    .catch(error => console.error(error));
};

// Add event listener for Send button
sendButton.addEventListener('click', sendPrompt);

// Add event listener for Enter key press
chatInput.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        event.preventDefault(); // Prevent the default form submit action
        sendPrompt();
    }
});
