# ai_terminal_assistant/core.py

import re
import os
import google.generativeai as genai
from .config import GEMINI_API_KEY, set_api_key

# Initialize model variable
model = None

def initialize_model():
    """Initialize the Gemini model with current API key"""
    global model
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash-002")

# Initialize on import
initialize_model()

def update_api_key(new_key):
    """Update the API key and reinitialize the model"""
    global GEMINI_API_KEY, model
    set_api_key(new_key)
    GEMINI_API_KEY = new_key
    initialize_model()
    return "API key updated successfully"

def get_directory_info():
    """Get current directory structure info"""
    cwd = os.getcwd()
    dir_structure = []
    for root, dirs, files in os.walk(cwd, topdown=True):
        level = root.replace(cwd, '').count(os.sep)
        indent = ' ' * 4 * level
        dir_structure.append(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            dir_structure.append(f"{subindent}{f}")
        # Limit depth for brevity
        if level > 2:
            del dirs[:]
    return "\n".join(dir_structure[:20])  # Limit output length

def prompt_to_command(user_prompt: str) -> str:
    try:
        dir_info = get_directory_info()
        prompt = (
            "You are a Linux terminal command expert. "
            "Current directory structure:\n"
            f"{dir_info}\n\n"
            "Convert this to a single Linux shell command ONLY with these rules:\n"
            "1. NO additional text\n"
            "2. NO explanations\n"
            "3. NO markdown\n"
            "4. NO quotes/backticks\n"
            "5. ONLY the raw command\n\n"
            "User request: {user_prompt}\n"
            "Command:"
        ).format(user_prompt=user_prompt)
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"echo '❌ Error: {e}'"

def suggest_fix(command: str, error_output: str) -> str:
    try:
        dir_info = get_directory_info()
        prompt = (
            "Current directory structure:\n"
            f"{dir_info}\n\n"
            "The command failed:\n{command}\n\n"
            "Error:\n{error_output}\n\n"
            "Provide ONLY the corrected command with:\n"
            "1. NO additional text\n"
            "2. NO explanations\n"
            "3. NO markdown\n"
            "4. NO quotes/backticks\n"
            "Command:"
        )
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"echo '⚠️ Error: {e}'"