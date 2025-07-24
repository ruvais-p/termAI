# ai_terminal_assistant/cli.py

import click
import subprocess
import shlex
from .core import prompt_to_command, suggest_fix, update_api_key
from .config import get_api_key
import sys

def execute_command(command):
    """Execute the command and return its output"""
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

def handle_direct_prompt(args, no_exec=False):
    """Handle direct prompt execution"""
    full_prompt = ' '.join(args)
    click.echo("🧠 Generating shell command...")
    result = prompt_to_command(full_prompt)
    click.echo(f"💻 AI Command:\n{result}")
    
    if not no_exec:
        click.echo("\n🚀 Executing command...")
        output = execute_command(result)
        click.echo(f"📝 Command output:\n{output}")

def show_help():
    """Show help message"""
    help_text = """🧠 AI Terminal Assistant - Convert natural language to commands
    

Usage:
  python3 main.py "list all files"                    # Direct prompt (recommended)
  python3 main.py list all files                      # Direct prompt without quotes
  python3 main.py --no-exec "create directory test"   # Show command without executing
  python3 main.py cmd "list all files"                # Using cmd subcommand
  python3 main.py fix "ls -la" "permission denied"    # Fix a broken command
  python3 main.py key YOUR_API_KEY                    # Set API key
  python3 main.py key                                 # Show current API key

Options:
  --no-exec, -n    Do not execute the command, just show it
  --help           Show this message and exit
"""
    click.echo(help_text)

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        show_help()
        return
    
    args = sys.argv[1:]
    
    # Handle help
    if args[0] in ['--help', '-h', 'help']:
        show_help()
        return
    
    # Check for flags
    no_exec = False
    if '--no-exec' in args:
        args.remove('--no-exec')
        no_exec = True
    if '-n' in args:
        args.remove('-n')
        no_exec = True
    
    if not args:
        show_help()
        return
    
    first_arg = args[0]
    
    # Handle subcommands
    if first_arg == 'cmd':
        if len(args) < 2:
            click.echo("❌ Error: cmd requires a prompt")
            click.echo("Usage: python3 main.py cmd \"your prompt here\"")
            return
        prompt_args = args[1:]
        handle_direct_prompt(prompt_args, no_exec)
        
    elif first_arg == 'fix':
        if len(args) < 3:
            click.echo("❌ Error: fix requires a command and error message")
            click.echo("Usage: python3 main.py fix \"command\" \"error message\"")
            return
        command = args[1]
        error = args[2]
        click.echo("🛠️  Suggesting fix for command...")
        result = suggest_fix(command, error)
        click.echo(f"💻 Fixed Command:\n{result}")
        
        if not no_exec:
            click.echo("\n🚀 Executing fixed command...")
            output = execute_command(result)
            click.echo(f"📝 Command output:\n{output}")
            
    elif first_arg == 'key':
        if len(args) > 1:
            # Set new key
            new_key = args[1]
            result = update_api_key(new_key)
            click.echo(f"🔑 {result}")
        else:
            # Show current key
            current_key = get_api_key()
            if current_key:
                click.echo(f"🔑 Current key: {current_key[:4]}...{current_key[-4:]}")
            else:
                click.echo("❌ No API key set. Please set one with: python3 main.py key YOUR_API_KEY")
    
    else:
        # This is a direct prompt
        handle_direct_prompt(args, no_exec)

if __name__ == '__main__':
    main()