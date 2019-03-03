
from flask import Blueprint, abort


errors = Blueprint("errors", __name__)


@errors.route("/404/")
def route_404():

    return abort(404)


@errors.route("/404/custom/")
def route_404_custom():

    return "<h1>the custom error template</h1>", 404


@errors.route("/500/")
def route_500():

    return abort(500)
