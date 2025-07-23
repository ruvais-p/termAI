# ai_terminal_assistant/config.py

import os

KEY_FILE = os.path.expanduser('geminikey.txt')

def get_api_key():
    """Get API key from file or return None"""
    try:
        with open(KEY_FILE, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def set_api_key(key):
    """Store API key in file"""
    with open(KEY_FILE, 'w') as f:
        f.write(key.strip())

# Try to get key from file, otherwise use placeholder
GEMINI_API_KEY = get_api_key() or "your-api-key-here"