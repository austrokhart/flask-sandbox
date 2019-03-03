
from flask import Blueprint, request, jsonify


rest_methods = Blueprint("rest_methods", __name__)


# this routes returns same data
# but a real project can use this model to build a restful crud api

@rest_methods.route("/<id>/", methods=["GET"])
def get_method(**request_variables):

    return jsonify({
        "request_method":    request.method,
        "request_variables": request_variables,
        "request_args":      request.args.to_dict(),
        "request_data":      request.form.to_dict()
    })


@rest_methods.route("/<id>/", methods=["POST"])
def post_method(**request_variables):

    return jsonify({
        "request_method":    request.method,
        "request_variables": request_variables,
        "request_args":      request.args.to_dict(),
        "request_data":      request.form.to_dict()
    })


@rest_methods.route("/<id>/", methods=["PUT"])
def put_method(**request_variables):

    return jsonify({
        "request_method":    request.method,
        "request_variables": request_variables,
        "request_args":      request.args.to_dict(),
        "request_data":      request.form.to_dict()
    })


@rest_methods.route("/<id>/", methods=["DELETE"])
def delete_method(**request_variables):

    return jsonify({
        "request_method":    request.method,
        "request_variables": request_variables,
        "request_args":      request.args.to_dict(),
        "request_data":      request.form.to_dict()
    })
