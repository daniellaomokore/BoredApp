
from flask import Blueprint, redirect,render_template, session, url_for
#from flask_login import login_required, current_user

views = Blueprint("views", __name__, static_folder="static", template_folder="template")



@views.route("/")
#@login_required
def home():
    return render_template("home.html")


@views.route("/favourites")
#@login_required
def favourites():
    """ users_favourites = favourites.select().with_only_columns(
        [favourites.activity, favourites.participants, favourites.type, favourites.price]).where(
        favourites.UserID == "{}".format(session["UserID"])).execute()


    activity=users_favourites.activity
    participants=users_favourites.participants
    price=users_favourites.price
    type=users_favourites.type"""






    return render_template("favourites.html")


@views.route("/activity")  # < > lets you pass value through to function as a parameter
def activity():
    return render_template("activityPage.html")


@views.route("/user", methods=["POST", "GET"])
def user():
    if "Username" or "Email" in session:  # if the user has logged in
        return render_template("user.html")
    else:
        return redirect(url_for("login"))

