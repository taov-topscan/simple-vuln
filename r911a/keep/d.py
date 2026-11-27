from flask import Blueprint, request


def register(app):
    bp = Blueprint("xss", __name__)
    bp.add_url_rule("/hello", "hello", _hello_vulnerable)
    app.register_blueprint(bp)


def _hello_vulnerable():
    name = request.args.get("name", "world")
    return f"<!doctype html><html><body><h1>Hello {name}</h1><a href=\"/\">Home</a></body></html>"
