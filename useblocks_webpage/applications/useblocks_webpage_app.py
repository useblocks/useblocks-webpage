import os
from groundwork import App


def create_app():
    app = App([os.path.abspath(os.path.join(os.path.dirname(__file__), "configuration.py"))])
    app.plugins.activate(["GwWeb", "UbWebpageIntroduction", "GwWebManager", "GwPluginsInfo"])
    return app


def start_app():
    app = create_app()
    app.commands.start_cli()


if "main" in __name__:
    start_app()
