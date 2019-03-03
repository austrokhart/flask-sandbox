
from flask import Blueprint, redirect, url_for


redirects = Blueprint("redirects", __name__)


@redirects.route("/")
def default_route():

    return "the default route"


@redirects.route("/redirect/")
def redirecting():

    return redirect(url_for("redirects.default_route"))
