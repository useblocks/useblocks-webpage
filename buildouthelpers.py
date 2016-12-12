WSGISCRIPT_TEMPLATE = """\
# -*- coding: utf-8 -*-
import sys
import os

join = os.path.join
base = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
base = os.path.dirname(base)

sys.path[0:0] = [
{0}
]

from {1} import {2}


def application(environ, start_response):
    app = create_app()
    return app.web.flask(environ, start_response)
"""


def make_wsgi_script(recipe, buildout):
    """Build the script for Apache/mod_wsgi
    """
    # Late import: zc.recipe.egg may not be installed when executing 1st
    # function
    from zc.recipe.egg.egg import Eggs
    app_egg = recipe['egg']
    wsgi_filepath = recipe['script']
    app_mod, app_obj = recipe['app'].rsplit('.', 1)  # 'a.b.c.d' -> 'a.b.c', 'd'
    working_dir = recipe['working_dir']
    relative_paths = recipe["relative-paths"]

    reqs, ws = Eggs(buildout, app_egg, recipe).working_set()
    egg_paths = [pkg.location for pkg in ws]

    if relative_paths == "false":
        src_egg_paths = ',\n'.join(["    '{0}'".format(path) for path in egg_paths])
    else:
        src_egg_paths = ',\n'.join(["join(base, '{0}')".format("/".join(path.split("/")[-2:])) for path in egg_paths])
        src_egg_paths = "base, \n%s" % src_egg_paths

    with open(wsgi_filepath, 'w') as fh:
        fh.write(WSGISCRIPT_TEMPLATE.format(src_egg_paths, app_mod, app_obj, working_dir))
    return
