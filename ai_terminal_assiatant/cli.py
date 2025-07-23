# ai_terminal_assistant/cli.py

import click
import sys
from .core import prompt_to_command, suggest_fix, update_api_key
from .config import get_api_key

@click.group(invoke_without_command=True)
@click.argument('prompt', required=False)
@click.pass_context
def cli(ctx, prompt):
    """🧠 AI Terminal Assistant - Convert natural language to commands"""
    if ctx.invoked_subcommand is None:
        if prompt:
            # Handle direct natural language prompt
            click.echo("🧠 Generating shell command...")
            result = prompt_to_command(prompt)
            click.echo(f"💻 AI Command:\n{result}")
        else:
            # Show help if no command or prompt provided
            click.echo(ctx.get_help())

@cli.command()
@click.argument('command')
@click.argument('error')
def fix(command, error):
    """Fix a broken shell command using error output"""
    click.echo("🛠️  Suggesting fix for command...")
    result = suggest_fix(command, error)
    click.echo(f"💻 Fixed Command:\n{result}")

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