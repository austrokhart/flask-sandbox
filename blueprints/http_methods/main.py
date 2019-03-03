
from flask import Blueprint, request, jsonify


http_methods = Blueprint("http_methods", __name__)


# getting data from different type requests

@http_methods.route("/", methods=["GET"])
def get_method(**request_variables):

    return jsonify({
        "request_method":    request.method,
        "request_variables": request_variables,
        "request_args":      request.args.to_dict(),
        "request_data":      request.form.to_dict()
    })


@http_methods.route("/", methods=["POST"])
def post_method(**request_variables):

    return jsonify({
        "request_method":    request.method,
        "request_variables": request_variables,
        "request_args":      request.args.to_dict(),
        "request_data":      request.form.to_dict()
    })