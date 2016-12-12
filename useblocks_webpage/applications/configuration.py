import os
import sys

APP_NAME = "useblocks_webpage_app"
APP_DESCRIPTION = "groundwork application of package useblocks webpage"
APP_PATH = os.path.dirname(__file__)
PACKAGE_PATH = os.path.join(os.path.dirname(__file__), "..", "..")

PLUGINS = ["GwWeb", "UbWebpageIntroduction", "GwWebManager", "GwPluginsInfo"]

# The Server_NAME should contain ip/name + port. If port is 80 or 412, leave it away!
FLASK_SERVER_NAME = os.getenv("FLASK_SERVER_NAME", "127.0.0.1")

FLASK_HOST = os.getenv("FLASK_HOST", "0.0.0.0")
FLASK_PORT = os.getenv("FLASK_PORT", 5000)
FLASK_DEBUG = os.getenv("FLASK_DEBUG", False)


GROUNDWORK_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "%(asctime)s - %(levelname)-5s - %(message)s"
        },
        'debug': {
            'format': "%(asctime)s - %(levelname)-5s - %(name)-40s - %(message)-80s - %(module)s:%("
                      "funcName)s(%(lineno)s)"
        },
    },
    'handlers': {
        'console_stdout': {
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'level': 'DEBUG'
        },
        'file': {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "debug",
            "filename": "%s/logs/app.log" % PACKAGE_PATH,
            "maxBytes": 1024000,
            "backupCount": 3,
            'level': 'DEBUG'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console_stdout', 'file'],
            'level': 'DEBUG',
            'propagate': True
        },
        'groundwork': {
            'handlers': ['console_stdout', 'file'],
            'level': 'INFO',
            'propagate': False
        },
    }
}