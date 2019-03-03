
from flask import Blueprint, render_template


static_files = Blueprint("static_files", __name__, template_folder="templates", static_folder="static")


# including static files to a page
# it's important that a template file placed into a subdirectory

@static_files.route("/")
def default_route():

    return render_template("static_files/template.html", title=static_files.name)
