import os
import json
from flask import Flask, render_template, request, jsonify, session
from groq import Groq
from utils import load_chat_history, save_chat_history
import markdown

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Load config
working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))

GROQ_API_KEY = config_data["GROQ_API_KEY"]
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

client = Groq()

# Route for the home page
@app.route('/')
def index():
    if 'chat_history' not in session:
        session['chat_history'] = []
    return render_template('index.html', chat_history=session['chat_history'])


@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_prompt = request.json["user_prompt"]
        chat_history = load_chat_history()
        chat_history.append({"role": "user", "content": user_prompt})
        messages = [
            {"role": "system", "content": "You are a helpful assistant"},
            *chat_history
        ]
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages
        )
        assistant_response = response.choices[0].message.content

        # Convert Markdown to HTML
        html_response = markdown.markdown(assistant_response)
        
        chat_history.append({"role": "assistant", "content": html_response})
        save_chat_history(chat_history)
        return jsonify({"assistant_response": html_response})
    return jsonify({"message": "Invalid request"})


if __name__ == "__main__":
    app.run(debug=True)
