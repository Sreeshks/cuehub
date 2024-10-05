import click
from cuehub.commands import django, flask, generic

@click.group()
def cue():
    """CueHub CLI - Setup frameworks like Django, Flask, etc."""
    pass

@cue.command()
def setup_django():
    """Sets up a Django project."""
    django.setup_django()

@cue.command()
def setup_flask():
    """Sets up a Flask project."""
    flask.setup_flask()
