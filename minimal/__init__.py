import site

from flask import Flask

site.addsitedir("vendor")


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "hello world"

    return app
