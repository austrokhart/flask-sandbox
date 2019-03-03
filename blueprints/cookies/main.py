
from flask import Blueprint, request, make_response, abort


cookies = Blueprint("cookies", __name__)


# there i got an important lesson
# the initiator of the setting cookies by the server side must be the server


# getting cookie data
@cookies.route("/name/", methods=["GET"])
def get_name():

    if "name" in request.cookies:

        return request.cookies.get("name", "")

    else:

        return abort(404)


# setting cookie data
@cookies.route("/name/", methods=["POST"])
def set_name():

    if "name" in request.form:

        response = make_response()
        response.set_cookie("name", request.form["name"])

        return response

    else:

        return abort(404)
