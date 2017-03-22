#!/usr/bin/env python

import os

from flask.cli import FlaskGroup
from {{ project_name }} import create_app as create_app_base

# Por algum motivo o Flask está ignorando a flag DEBUG quando vem do config,
# e se você está aqui você está no ambiente local logo podemos setar debug
# como True sempre.
os.environ.setdefault('FLASK_DEBUG', '1')


def create_app(info):
    return create_app_base()


cli = FlaskGroup(create_app=create_app)


@cli.command('test', short_help='Discover and run tests for current project.')
def test_command():
    import pytest

    pytest.main([])


if __name__ == '__main__':
    cli()
