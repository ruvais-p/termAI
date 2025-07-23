# main.py

import sys
from ai_terminal_assiatant.cli import cli

if __name__ == "__main__":
    # Handle cases where the prompt might contain spaces
    if len(sys.argv) > 1 and not sys.argv[1].startswith('-') and sys.argv[1] not in ['fix', 'key']:
        # If the first argument isn't a command, treat everything as a prompt
        prompt = ' '.join(sys.argv[1:])
        sys.argv = [sys.argv[0], prompt]
    cli()