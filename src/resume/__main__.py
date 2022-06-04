"""CLI Entry Point for Luke Garzia's Resume - Making Resumes fun since 2022"""

import typer


def main() -> None:
    """Dispatch to typer"""
    typer.run(get_luke_cli)

def get_luke_cli()->None:
    """Entry point for CLI"""
    resume_text = '''RESUME DETAILS HERE'''
    typer.echo(resume_text)
