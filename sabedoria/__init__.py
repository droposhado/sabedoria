import os

import sentry_sdk
from flask import Flask
from flask.logging import create_logger
from sentry_sdk.integrations.flask import FlaskIntegration

from . import cli
from .models.db import db
from .views import apiv2

__version__ = "2.0.1"


def create_app(config_string="sabedoria.config.ProductionConfig"):
    """Simple function to create application to use with wsgi and flask run"""

    sentry_sdk.init(
        dsn=os.getenv("SENTRY_DSN"),
        integrations=[
            FlaskIntegration(),
        ],

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0
    )

    app = Flask(__name__, static_folder="static", static_url_path="")
    app.config.from_object(config_string)

    app.logger = create_logger(app)
    app.logger.setLevel(app.config["LOG_LEVEL"])

    db.init_app(app)

    app.cli.add_command(cli.create_tables_command)
    app.cli.add_command(cli.drop_tables_command)

    app.register_blueprint(apiv2.bp)


    @app.errorhandler(404)
    def route_not_found(err):
        """Custom 404 pages returning json"""
        return {
            "status": "error",
            "message": err.name
        }, 404


    @app.errorhandler(500)
    def route_internal_error(err):
        """Custom 500 pages returning json"""
        return {
            "status": "error",
            "message": err.name
        }, 500

    return app
