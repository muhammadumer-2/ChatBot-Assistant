import os
import json

def load_chat_history():
    working_dir = os.path.dirname(os.path.abspath(__file__))
    chat_history_path = f"{working_dir}/chat_history.json"
    if os.path.exists(chat_history_path):
        with open(chat_history_path, "r") as f:
            return json.load(f)
    else:
        # If file does not exist, return an empty list
        return []

def save_chat_history(chat_history):
    working_dir = os.path.dirname(os.path.abspath(__file__))
    chat_history_path = f"{working_dir}/chat_history.json"
    with open(chat_history_path, "w") as f:
        json.dump(chat_history, f, indent=4)
