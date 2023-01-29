#Blueprint example
from flask import Blueprint,render_template

second = Blueprint("second", __name__, static_folder="static", template_folder="template")


# to access /admin/home or /admin/
@second.route("/home")
@second.route("/")
def home():
    return "<h1>Admin home page</h1>"

# to access /admin/test
@second.route("/test")
def test():
    return "<h1>Admin test page</h1>"