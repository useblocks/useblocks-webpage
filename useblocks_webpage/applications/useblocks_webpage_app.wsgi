"""
WSGI script for useblocks_webpage_app

This file may be used by the Apache mod_wsgi plugin, so that this application get
delivered and managed by Apache

"""
activate_this = '/home/useblocks/py35_venv_ub_webpage/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys
import os
sys.path.insert(0, os.path.basename(os.path.realpath(__file__)))

from useblocks_webpage.applications.useblocks_webpage_app import create_app


def application(environ, start_response):
    app = create_app()
    return app.web.flask(environ, start_response)

