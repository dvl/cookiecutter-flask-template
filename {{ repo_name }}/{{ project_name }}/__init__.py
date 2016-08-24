from flask import Flask

from .views import api


def create_app(config=None):
    if not config:
        config = '{{ project_name }}.config'

    app = Flask('{{ project_name }}')
    app.config.from_oject(config)

    app.register_blueprint(api)

    return app
