
from flask import Blueprint, url_for


routing = Blueprint("routing", __name__)


# processing a default route
@routing.route("/")
def default_route():

    return "the default route"


# processing a some route
@routing.route("/sub/route/")
def sub_route():

    return "the sub route"


# an example of obtaining a route path from other route
# works with apps and blueprints
@routing.route("/from/one/route/to/other/route/")
def from_one_route_to_other_route():

    return url_for("routing.sub_route")
