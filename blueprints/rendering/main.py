
from flask import Blueprint, Markup, render_template, render_template_string, jsonify


rendering = Blueprint("rendering", __name__, template_folder="templates")


# rendering a plain text
@rendering.route("/string/")
def string():

    return "<h1>Hello, world!</h1>"


# rendering a template string
@rendering.route("/template/string/")
def template_string():

    return render_template_string("{{ text }}", text="<h1>Hello, world!</h1>")


# rendering a template with unsafe data
@rendering.route("/template/escaped/")
def template_escaped():

    return render_template("rendering/template.html", text="<h1>Hello, world!</h1>")


# rendering a template with safe data
@rendering.route("/template/unescaped/")
def template_unescaped():

    return render_template("rendering/template.html", text=Markup("<h1>Hello, world!</h1>"))


# rendering json
@rendering.route("/json/")
def json():

    return jsonify({
        "text": "<h1>Hello, world!</h1>"
    })
