
from flask import Blueprint, request, jsonify, current_app


url = Blueprint("url", __name__)


# getting different url data for the root path
@url.route("/")
def default_route():

    return jsonify({
        "request.url": request.url,
        "request.base_url": request.base_url,
        "request.host_url": request.host_url,
        "request.url_root": request.url_root,
        "request.url_rule.rule": request.url_rule.rule,
        "request.url_rule.endpoint": request.url_rule.endpoint,
        "request.path": request.path,
        "request.blueprint": request.blueprint,
        "url.name": url.name,
        "url.url_prefix": url.url_prefix,
        "current_app.blueprints[request.blueprint].url_prefix": current_app.blueprints[request.blueprint].url_prefix,
    })


# the same for the other path
@url.route("/sub/route/")
def sub_route():

    return jsonify({
        "request.url": request.url,
        "request.base_url": request.base_url,
        "request.host_url": request.host_url,
        "request.url_root": request.url_root,
        "request.url_rule.rule": request.url_rule.rule,
        "request.url_rule.endpoint": request.url_rule.endpoint,
        "request.path": request.path,
        "request.blueprint": request.blueprint,
        "url.name": url.name,
        "url.url_prefix": url.url_prefix,
        "current_app.blueprints[request.blueprint].url_prefix": current_app.blueprints[request.blueprint].url_prefix,
    })
