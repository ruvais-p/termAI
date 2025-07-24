# ai_terminal_assistant/cli.py

import click
import sys
import subprocess
from .core import prompt_to_command, suggest_fix, update_api_key
from .config import get_api_key

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

@click.group(invoke_without_command=True)
@click.argument('prompt', required=False)
@click.option('--no-exec', '-n', is_flag=True, help='Do not execute the command, just show it')
@click.pass_context
def cli(ctx, prompt, no_exec):
    """🧠 AI Terminal Assistant - Convert natural language to commands"""
    if ctx.invoked_subcommand is None:
        if prompt:
            click.echo("🧠 Generating shell command...")
            result = prompt_to_command(prompt)
            click.echo(f"💻 AI Command:\n{result}")
            
            if not no_exec:
                click.echo("\n🚀 Executing command...")
                output = execute_command(result)
                click.echo(f"📝 Command output:\n{output}")
        else:
            click.echo(ctx.get_help())

@cli.command()
@click.argument('command')
@click.argument('error')
@click.option('--no-exec', '-n', is_flag=True, help='Do not execute the fixed command, just show it')
def fix(command, error, no_exec):
    """Fix a broken shell command using error output"""
    click.echo("🛠️  Suggesting fix for command...")
    result = suggest_fix(command, error)
    click.echo(f"💻 Fixed Command:\n{result}")
    
    if not no_exec:
        click.echo("\n🚀 Executing fixed command...")
        output = execute_command(result)
        click.echo(f"📝 Command output:\n{output}")

@cli.command()
@click.argument('new_key', required=False)
def key(new_key):
    """Set or show your Gemini API key"""
    if new_key:
        result = update_api_key(new_key)
        click.echo(f"🔑 {result}")
    else:
        current_key = get_api_key()
        if current_key:
            click.echo(f"🔑 Current key: {current_key[:4]}...{current_key[-4:]}")
        else:
            click.echo("❌ No API key set. Please set one with: ata key YOUR_API_KEY")