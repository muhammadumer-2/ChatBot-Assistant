# ChatBot Assistant

This is a simple ChatBot assistant web application built using **Flask** and **Groq** API. It allows users to interact with an AI assistant, and the responses are generated based on the user’s prompts. The chat history is saved in a JSON file on the backend but is not displayed in the frontend chat interface.

## Features

- **Real-Time Chat:** Communicate with the AI assistant in real time.
- **Markdown Rendering:** The bot's responses are processed from Markdown to HTML for better formatting.
- **Session-Based Chat History:** The chat history is stored for the current session and saved in a JSON file on the server.
- **Chat History Persistence:** Chat history is saved in a `chat_history.json` file but is not visible in the frontend interface.

## Requirements

Before running the project, ensure you have the following installed:
- **Python 3.8+**
- **pip** (Python package manager)

All project dependencies are listed in the `requirements.txt` file. You can install them using the instructions below.

## Installation

Follow these steps to set up and run the project locally:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/chatbot-assistant.git
    ```

2. Navigate to the project directory:
    ```bash
    cd chatbot-assistant
    ```

3. (Optional) Set up a virtual environment:
    - For Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    - For Mac/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Set up the `config.json` file with your **GROQ API Key**:
    ```json
    {
        "GROQ_API_KEY": "YOUR_OWN_API_KEY"
    }
    ```

6. Run the Flask application:
    ```bash
    python app.py
    ```

7. Open your browser and go to `http://127.0.0.1:5000/` to interact with the ChatBot assistant.

## Usage

Once the server is up and running, you can start chatting with the AI assistant through the web interface:

1. Enter your question or prompt into the input field.
2. Click the **Send** button or press **Enter** to submit your prompt.
3. The AI will generate a response, which will be displayed in the chat window.

### Example Conversation:
- **User Prompt:** "What is Python?"
- **Assistant Response:** "Python is a high-level, general-purpose programming language."

## How it Works

- **Backend:** The Flask web framework handles routing and server-side logic. The `app.py` file manages the interaction between the frontend and the **Groq** API, which provides the AI's responses.
- **Frontend:** The chat interface is built using HTML, CSS, and JavaScript. User input is sent as a POST request to the `/chat` route, which processes it and returns the AI's response.
- **Markdown to HTML Conversion:** The AI's responses may include Markdown, which is converted to HTML for better display in the chat log.
- **Chat History:** Each conversation is saved in a JSON file (`chat_history.json`) on the server, but the history isn't shown in the chat window during the session.

## Chat History Management

The chat history is managed using two utility functions in the `utils.py` file:

- **`load_chat_history()`**: Loads the chat history from `chat_history.json`. If the file doesn't exist, it returns an empty list.
- **`save_chat_history(chat_history)`**: Saves the current chat history to the `chat_history.json` file.

Here’s a brief explanation of these functions:
- **load_chat_history():**
  - Checks if the `chat_history.json` file exists in the current working directory.
  - If it exists, it loads and returns the chat history (as a list).
  - If not, it returns an empty list.

- **save_chat_history(chat_history):**
  - Saves the chat history (a list of messages) to the `chat_history.json` file with proper indentation for readability.

## Project Structure

Here's an overview of the key files and directories:

```plaintext
├── app.py                # Main Flask application
├── config.json           # Configuration file for API key
├── templates/
│   └── index.html        # Frontend HTML for the chat interface
├── static/
│   ├── style.css         # CSS styles for the chat interface
│   └── script.js         # JavaScript for handling user input and chat
├── utils.py              # Utility functions for managing chat history
├── requirements.txt      # Python dependencies
├── chat_history.json     # JSON file where chat history is stored
└── README.md             # Project documentation
