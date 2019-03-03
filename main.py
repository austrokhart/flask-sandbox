
from flask import Flask, current_app, render_template, Markup
from config import secret_key

from blueprints.routing.main import routing
from blueprints.variable_rules.main import variable_rules
from blueprints.http_methods.main import http_methods
from blueprints.rest_methods.main import rest_methods
from blueprints.rendering.main import rendering
from blueprints.static_files.main import static_files
from blueprints.files_uploading.main import files_uploading
from blueprints.cookies.main import cookies
from blueprints.redirects.main import redirects
from blueprints.errors.main import errors
from blueprints.sessions.main import sessions
from blueprints.logging.main import logging
from blueprints.url.main import url


# creating an app and registering blueprints
app = Flask(__name__, template_folder="templates")
app.secret_key = secret_key
app.register_blueprint(routing,         url_prefix="/routing/")
app.register_blueprint(variable_rules,  url_prefix="/variable_rules/")
app.register_blueprint(http_methods,    url_prefix="/http_methods/")
app.register_blueprint(rest_methods,    url_prefix="/rest_methods/")
app.register_blueprint(rendering,       url_prefix="/render/")
app.register_blueprint(static_files,    url_prefix="/static_files/")
app.register_blueprint(files_uploading, url_prefix="/files_uploading/")
app.register_blueprint(cookies,         url_prefix="/cookies/")
app.register_blueprint(redirects,       url_prefix="/redirects/")
app.register_blueprint(errors,          url_prefix="/errors/")
app.register_blueprint(sessions,        url_prefix="/sessions/")
app.register_blueprint(logging,         url_prefix="/logging/")
app.register_blueprint(url,             url_prefix="/url/")


# showing all registered routes
@app.route("/")
def routes_list():

    routes = [str(rule) for rule in current_app.url_map.iter_rules()]
    routes.sort()

    return render_template("routes_list.html", title=routes_list.__name__, routes=routes)


if __name__ == '__main__':
    app.run(debug=True)
