# models defines the table schemas

from . import database
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, PasswordField, EmailField
from wtforms.validators import DataRequired


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
