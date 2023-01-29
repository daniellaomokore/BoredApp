"""
Then: Create a wireframe of you want the app to look/the layout
# make the code work so the user can't access the user page unless logged in-flask login?
# make favourites add to the end of the list as it's currently adding in the middle
# Classes & different py files
# see if using flask login is better?
# ux design for signup and log in- no tedious, allow signup with Google etc
# add exception handling for each time a user has an input, if the activity is already in the favourites


Room for improvement
Given that this is still a very basic “skeleton” version of User Authentication/Login there are many opportunities for improvements. Some of them are as follows:

SSL Certificate — it is important to ensure that the private information of users is transmitted over a secure connection.
Feedback to users — to ensure users are aware if they have incorrectly submitted information flashes and general error messages should be incorporated into templates. These can be shown to users after their first failed attempt.
Email communication — to allow users to confirm their registration and reset their passwords, automatic email generation should be incorporated.
Styling and interactivity— the pages are very plain at the moment. Further styling should be added using CSS, JavaScript and front end frameworks.

"""

from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_wtf import FlaskForm  # Flask_WTF on install

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, and_
from wtforms import StringField, SubmitField, DateField, PasswordField, EmailField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash
from second import second
from config import SECRET_KEY, DATABASEPASSWORD, DATABASENAME
import json
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY  # secret key for the WTForm forms you create
app.register_blueprint(second, url_prefix="/admin")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:{PASSWORD}@localhost/{DatabaseName}'.format(
    PASSWORD=DATABASEPASSWORD, DatabaseName=DATABASENAME)
app.permanent_session_lifetime = timedelta(
    days=1)  # this lets us store out permanent session data for x days/minutes etc so the user doesn't have to re-login everytime they close the tab

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(app)

APIurl = "http://www.boredapi.com/api/activity"


def connect_to_api(url):
    response = requests.get(url)
    dataResponse = response.text
    connection = json.loads(
        dataResponse)  # deserializing - turns json string into python dictionary that can be now accessed

    return connection


@app.route("/randomActivity", methods=["GET", "POST"])
def randomActivity():
    if request.method == 'POST':
        clicked = True
        url = "{}/".format(APIurl)
        activity = connect_to_api(url)

        activityID = activity['key']

        activityInfo, link_str = display_the_activity(activityID)

        return render_template('user.html', activityInfo=activityInfo,
                               clicked=clicked)


@app.route("/participantNumber", methods=["GET", "POST"])
def participantNumber():
    if request.method == 'POST':
        form = request.form  # get the html form
        clicked = True
        number_of_participants = form["participants"]
        url = "{}?participants={}".format(APIurl, number_of_participants)
        activity = connect_to_api(url)

        activityID = activity['key']

        activityInfo, link_str = display_the_activity(activityID)

        return render_template('user.html', activityInfo=activityInfo,
                               clicked=clicked, number_of_participants=number_of_participants)


@app.route("/budgetRange", methods=["GET", "POST"])
def budgetRange():
    if request.method == 'POST':
        form = request.form  # get the html form
        clicked = True
        minimumBudget = form["minimumBudget"]
        maximumBudget = form["maximumBudget"]

        url = "{}?minprice={}&maxprice={}".format(APIurl, minimumBudget, maximumBudget)
        activity = connect_to_api(url)

        activityID = activity['key']

        activityInfo, link_str = display_the_activity(activityID)

        return render_template('user.html', activityInfo=activityInfo,
                               clicked=clicked, minimumBudget=minimumBudget, maximumBudget=maximumBudget)


@app.route("/activityType", methods=["GET", "POST"])
def activityType():
    if request.method == 'POST':
        form = request.form  # get the html form
        clicked = True
        activityType = form["activityType"]
        url = "{}?type={}".format(APIurl, activityType)
        activity = connect_to_api(url)

        activityID = activity['key']

        activityInfo, link_str = display_the_activity(activityID)

        return render_template('user.html', activityInfo=activityInfo,
                               clicked=clicked, activityType=activityType)


@app.route("/activityLinked", methods=["GET", "POST"])
def activityLinked():
    if request.method == 'POST':

        activity_with_link_found = False

        while not activity_with_link_found:
            url = "{}/".format(APIurl)
            activity = connect_to_api(url)

            if activity['link']:
                activityID = activity['key']
                activityInfo, link_str = display_the_activity(activityID)

                return render_template('user.html', activityInfo=activityInfo, clicked=True, link_str=link_str )


# display activity info, we can use if else statements to formate the string in certain ways depending on what the activity selection was based on
def display_the_activity(activityID):
    url = "{}?key={}".format(APIurl, activityID)
    activity = connect_to_api(url)

    session[
        "activityID"] = activityID  # saving the activity id into the session for the activity generated - for later use

    activity_name = activity['activity']
    participant_number = activity['participants']
    price = activity['price']
    activity_type = activity['type']
    activity_link = activity['link']

    # this formats the link to the string if a link exists, otherwise and empty string is formatted
    # this also makes the link hyperlinked
    link_str = f"{activity_link}" if activity_link else ""

    return "{}, costs £{}, it is a {} activity and can be done by {} participant{}".format(
        activity_name, price, activity_type, participant_number, "" if participant_number == 1 else "s"), link_str


@app.route("/saveActivity", methods=["GET", "POST"])
def saveActivity():
    activityID = session['activityID']
    UserID = session['UserID']
    activityInfo = display_the_activity(activityID)

    if check_if_activity_is_in_favourites(activityID, UserID) is True:
        flash("Activity already exists in favourites", "error")
    else:
        # Connect to API to get activity info
        url = "{}?key={}".format(APIurl, activityID)
        activity = connect_to_api(url)

        activity_name = activity['activity']
        participant_number = activity['participants']
        price = activity['price']
        activity_type = activity['type']

        # Run query to save activity info
        add_activity = favourites(activityID=activityID, UserID=UserID, activity=activity_name,
                                  participants=participant_number, price=price,
                                  type=activity_type)
        database.session.add(add_activity)
        database.session.commit()



        flash("Activity saved to favourites!", "success")

    return render_template('user.html', clicked=True, activityInfo=activityInfo)


def check_if_activity_is_in_favourites(activityID, UserID):
    favouritesExists = favourites.query.filter(and_(favourites.activityID == activityID, favourites.UserID == UserID)).first()

    if favouritesExists:  # if True
        return True
    else:  # if False
        return False




# SQL-ALCHEMY DATABASE CONNECTIONS : 'the_users' & 'favourites'

# DEFINES THE TABLE SCHEMA IN OUR DATABASE
# database connection for 'the_users' table
class the_users(database.Model):
    UserID = database.Column(database.Integer, primary_key=True, autoincrement=True, nullable=False)
    FirstName = database.Column(database.String(65), nullable=False)
    LastName = database.Column(database.String(65), nullable=False)
    Email = database.Column(database.String(65), nullable=False, unique=True)
    DOB = database.Column(database.DateTime, nullable=False)
    City = database.Column(database.String(200), nullable=False)
    Username = database.Column(database.String(200), nullable=False)
    Password = database.Column(database.String(200), nullable=False)

    def __init__(self, FirstName, LastName, Email, DOB, City, Username, Password):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.DOB = DOB
        self.City = City
        self.Username = Username
        self.Password = Password


# database connection for 'favourites' table
class favourites(database.Model):
    activityID = database.Column(database.Integer, primary_key=True, nullable=False)
    UserID = database.Column(database.Integer, database.ForeignKey('the_users.UserID'), nullable=False)
    activity = database.Column(database.String(200), nullable=False)
    participants = database.Column(database.Integer, nullable=False)
    price = database.Column(database.Float, nullable=False)
    type = database.Column(database.String(200), nullable=False)

    def __init__(self, activityID, UserID, activity, participants, price, type):
        self.activityID = activityID
        self.UserID = UserID
        self.activity = activity
        self.participants = participants
        self.price = price
        self.type = type


# WTFORMS - FLASK FORMS FOR LOGINS,SIGNUPS ETC

# Form for sign up
class signUpForm(FlaskForm):
    firstname = StringField("Firstname:", validators=[DataRequired()])
    lastname = StringField("Lastname", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    dateofbirth = DateField("Date Of Birth", validators=[DataRequired()])
    city = StringField("City", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign Up")


# Form for log in
class logInForm(FlaskForm):
    emailOrUsername = StringField("emailOrUsername:", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log in")


# Form for forgot password
class forgotPassword(FlaskForm):
    emailOrUsername = StringField("emailOrUsername:", validators=[DataRequired()])
    submit = SubmitField("Reset Password")


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


# this must be called after a user has logged in, so we can save the user's UserID into the session for later use
def get_user_id():
    # query user id where email/username is
    if 'Email' in session:
        # query the user by their email
        current_user = database.session.query(the_users).filter_by(Email="{}".format(session['Email'])).first()

    elif 'Username' in session:
        # query the user by their username
        current_user = database.session.query(the_users).filter_by(Username="{}".format(session['Username'])).first()

    UserID = current_user.UserID  # select their UserID column

    return UserID


def get_user_firstname():
    # query user firstname where email/username is
    if 'Email' in session:
        # query the user by their email
        current_user = database.session.query(the_users).filter_by(Email="{}".format(session['Email'])).first()

    elif 'Username' in session:
        # query the user by their username
        current_user = database.session.query(the_users).filter_by(Username="{}".format(session['Username'])).first()

    FirstName = current_user.FirstName  # select their FirstName column

    return FirstName.capitalize()


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


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/favourites")
def view_favourites():
    users_favourites = (
        database.session.query(favourites.activity, favourites.participants, favourites.type, favourites.price)
        .filter(favourites.UserID == session["UserID"])
        .all())

    return render_template("favourites.html", users_favourites=users_favourites)


@app.route("/activity")  # < > lets you pass value through to function as a parameter
def activity():
    return render_template("activityPage.html")


@app.route("/user", methods=["POST", "GET"])
def user():
    if "Username" or "Email" in session:  # if the user has logged in
        return render_template("user.html")
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    if "Username" or "Email" in session:  # if the user has logged in
        flash("Logged out successfully", "success")

    session.pop("Username", None)  # removing the data from our session dict
    session.pop("Email", None)  # removing the data from our session dict
    session.pop("password", None)  # removing the data from our session dict
    return redirect(url_for("home"))  # when we log out ,redirect to the home page


if __name__ == "__main__":
    app.run(debug=True)  # 'debug=True' to live Auto updates changes to website
