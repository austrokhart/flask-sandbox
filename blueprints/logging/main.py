
from flask import Blueprint, current_app


logging = Blueprint("logging", __name__)


@logging.route("/debug/")
def debug():

    current_app.logger.debug("some debug message")
    return ""


@logging.route("/warning/")
def warning():

    current_app.logger.warning("some warning message")
    return ""


@logging.route("/error/")
def error():

    current_app.logger.error("some error message")
    return ""
