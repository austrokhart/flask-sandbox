
from flask import Blueprint, request, make_response, abort, session


sessions = Blueprint("sessions", __name__)


# getting a name in a session
@sessions.route("/name/", methods=["GET"])
def get_name():

    if "name" in session:

        return session["name"]

    else:

        return abort(404)


# setting a name in a session
@sessions.route("/name/", methods=["POST"])
def set_name():

    if "name" in request.form:

        session["name"] = request.form["name"]

        return make_response()

    else:

        return abort(404)

