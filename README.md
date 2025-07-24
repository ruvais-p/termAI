![Flow Expense Tracker Banner](https://github.com/ruvais-p/flow/blob/main/ChatGPT%20Image%20Jun%2024%2C%202025%2C%2010_40_58%20AM.png)
# termAI

**termAI** is an AI-powered terminal assistant that converts natural language prompts into shell commands using Google's Gemini API. It can also fix broken shell commands and manage API keys.

## Features

- 🚀 Convert natural language to Linux shell commands
- ⚡ Execute or preview commands before running
- 🔧 Fix broken commands using error messages
- 🔑 Manage your Google Gemini API key (set/show/clear)
- 📦 Easy-to-use CLI with `ata` command

## Installation

### Prerequisites
- Python 3.8+
- Git (optional)

### 1. Clone the Repository
```bash
git clone https://github.com/ruvais-p/termAI.git
cd termAI
```

### 2. Create and Activate Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows
```

### 3. Install the Package
```bash
pip install -e .
```

## Setup API Key

Set your Gemini API key (get one from [Google AI Studio](https://aistudio.google.com)):
```bash
ata key YOUR_API_KEY
```

Verify your key:
```bash
ata key
```

## Usage

### Basic Command Generation
```bash
ata "list all PDF files in current directory"
```

### Preview Without Execution
```bash
ata --no-exec "find all files modified today"
```

### Fix Broken Commands
```bash
ata fix "rm non-existent-file" "rm: cannot remove 'non-existent-file': No such file or directory"
```

## Advanced Usage

| Command | Description |
|---------|-------------|
| `ata "your prompt"` | Generate and execute command |
| `ata "prompt" -n` | Generate command without executing |
| `ata fix "cmd" "error"` | Fix a failed command |
| `ata key` | Show current API key |
| `ata key NEW_KEY` | Update API key |

## Project Structure

```
termAI/
├── ai_terminal_assistant/
│   ├── __init__.py
│   ├── cli.py        # Command line interface
│   ├── core.py       # AI command generation logic
│   ├── config.py     # API key management
├── main.py           # Entry point
├── geminikey.txt     # API key storage
├── setup.py          # Package configuration
├── pyproject.toml    # Build system config
└── README.md
```

## Troubleshooting

### Command Not Found
```bash
# Ensure virtual environment is active
source .venv/bin/activate
# Reinstall package
pip install -e .
```

### API Errors
- Check your internet connection
- Verify API key is valid
- Check Google AI Studio for quota limits

## Development

1. Make code changes
2. Reinstall package:
```bash
pip install -e .
```
3. Test changes:
```bash
ata "test command"
```

## Uninstallation
```bash
pip uninstall termAI
rm -rf ~/geminikey.txt  # Remove API key file
```

> ✨ **Pro Tip**: Add `alias ata='ata --no-exec'` to your `.bashrc`/`.zshrc` to default to safe mode!
```

This README includes:
1. Clear installation instructions
2. Usage examples with code blocks
3. Command reference table
4. Project structure visualization
5. Troubleshooting section
6. Development notes
7. Proper formatting for GitHub rendering

Would you like me to make any adjustments to this README or package it with your project files?
