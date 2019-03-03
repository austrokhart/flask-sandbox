
from flask import Blueprint


variable_rules = Blueprint("variable_rules", __name__)


# getting an untyped value (by default the type is a str)
@variable_rules.route("/<value>/")
def default_type(value):

    return str(value)


# getting an int type value
@variable_rules.route("/integer/<int:value>/")
def integer_type(value):

    return str(value)


# getting an float value
@variable_rules.route("/float/<float:value>/")
def float_type(value):

    return str(value)


# getting an path value
@variable_rules.route("/path/<path:value>/")
def path_type(value):

    return str(value)
