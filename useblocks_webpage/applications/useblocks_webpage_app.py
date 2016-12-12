import os
from groundwork import App
from flask import redirect, url_for


def create_app():
    app = App([os.path.abspath(os.path.join(os.path.dirname(__file__), "configuration.py"))])
    app.plugins.activate(["GwWeb", "UbWebpageIntroduction", "GwWebManager", "GwPluginsInfo"])
    return app


def start_app():

    def open_page():
        with app.web.flask.app_context():
            return redirect(url_for("ub.__introduction_view"))

    app = create_app()

    app.web.routes.register("/", ["GET"], open_page, plugin=None, context="web", name="start_redirect")

    app.commands.start_cli()


if "main" in __name__:
    start_app()
