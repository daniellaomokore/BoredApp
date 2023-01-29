# authentication of app

from flask import Blueprint, render_template,request,flash,redirect, session, url_for
from .models import the_users, signUpForm,logInForm,forgotPassword
from . import database, create_app
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import or_
from FlaskBoredApp import get_user_id,get_user_firstname


auth = Blueprint("auth", __name__, static_folder="static", template_folder="template")


# FLASK APP SERVER FUNCTIONS
@app.route("/signup", methods=["GET", "POST"])
def signup():
    firstname = lastname = email = dateofbirth = city = username = password = None
    form = signUpForm()

    # if a POST request was made from the signup page
    if request.method == "POST":

        # if the inputted form data is all valid.
        if form.validate_on_submit():
            firstname = form.firstname.data
            form.firstname.data = ''
            lastname = form.lastname.data
            form.lastname.data = ''
            email = form.email.data
            form.email.data = ''
            dateofbirth = form.dateofbirth.data
            form.dateofbirth.data = ''
            city = form.city.data
            form.city.data = ''
            username = form.username.data
            form.username.data = ''
            password = form.password.data
            form.password.data = ''

            password = generate_password_hash(password)

            # Check if there's a user in the database with this username/email already
            # this returns the user row with this email/username or None if it doesn't exist
            user_exists = the_users.query.filter(or_(the_users.Email == email, the_users.Username == username)).first()

            if user_exists:
                flash("A User already exists with this email/username.", "error")
            else:
                # save user into database
                new_user = the_users(FirstName=firstname, LastName=lastname, Email=email, DOB=dateofbirth, City=city,
                                     Username=username, Password=password)  # hash password
                database.session.add(new_user)
                database.session.commit()

                flash("Sign Up Successful!!", "success")
        else:
            flash("Signup details are invalid", "error")

    return render_template("signup.html", firstname=firstname, lastname=lastname, email=email, dateofbirth=dateofbirth,
                           city=city, username=username, password=password, form=form)


@app.route("/login", methods=["POST", "GET"])
def login():
    emailOrUsername = password = None
    form = logInForm()

    # if a POST request was made from the signup page
    if request.method == "POST":
        # if the inputted form data is all valid.
        if form.validate_on_submit():
            emailOrUsername = form.emailOrUsername.data
            form.emailOrUsername.data = ''
            password = form.password.data
            form.password.data = ''

            # Check if user used their email or username to login
            # returns a value or none if a user doesn't exist with these matching credentials

            # check if a username or email was entered
            if "@" in emailOrUsername:
                session['Email'] = emailOrUsername  # saves the users email into the session
                user = database.session.query(the_users).filter_by(Email=emailOrUsername).first()
            else:
                session['Username'] = emailOrUsername  # saves the users email into the session
                user = database.session.query(the_users).filter_by(Username=emailOrUsername).first()

            # if a user exists in the database with this username/email
            if user:
                # compare the hashed password from the database to the password the user logged in
                if check_password_hash(user.Password, password):
                    session['UserID'] = get_user_id()  # save the users ID to a session for later use
                    session['FirstName'] = get_user_firstname()

                    flash("Log in Successful!", "success")
                    return redirect(url_for("user"))

            else:
                flash("Log in Unsuccessful, Please try again!", "error")

    return render_template("login.html", emailOrUsername=emailOrUsername, password=password, form=form)

@app.route("/logout")
def logout():
    if "Username" or "Email" in session:  # if the user has logged in
        flash("Logged out successfully", "success")

    session.pop("Username", None)  # removing the data from our session dict
    session.pop("Email", None)  # removing the data from our session dict
    session.pop("password", None)  # removing the data from our session dict
    return redirect(url_for("home"))  # when we log out ,redirect to the home page


@app.route("/forgotpassword", methods=["POST", "GET"])
def forgotpassword():
    emailOrUsername = None
    form = forgotPassword()

    # if a POST request was made from the signup page
    if request.method == "POST":
        # if the inputted form data is all valid.
        if form.validate_on_submit():
            emailOrUsername = form.emailOrUsername.data
            form.emailOrUsername.data = ''

        # insert something that send a password changer to their email

        flash("Password reset link sent", "info")

    return render_template("forgotpassword.html", emailOrUsername=emailOrUsername, form=form)
