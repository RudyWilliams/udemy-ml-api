from flask import Flask

from api.config import get_logger

_logger = get_logger(logger_name=__name__)


def create_app(*, config_obj) -> Flask:
    """Create a flask app instance"""
    flask_app = Flask(
        "api"
    )  # api is the import name (but it doesn't seem to need to be based on the package)
    flask_app.config.from_object(config_obj)

    # from our codebase
    from api.controller import prediction_app

    flask_app.register_blueprint(prediction_app)
    _logger.debug("Application instance created")

    return flask_app
