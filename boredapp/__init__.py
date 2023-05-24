import json
from flask_bcrypt import Bcrypt
import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from flask_mail import Mail

from boredapp.config import (
    DATABASENAME,
    DATABASEPASSWORD,
    GOOGLE_CLIENT_ID,
    SECRET_KEY,
    MYEMAILPASSWORD,
    DATABASEUSERNAME,
    MYEMAIL,
    PORT,
)

"""
Code Structure reference: 
https://youtu.be/44PvX0Yv368
"""

"""
This code block sets up a Flask web application with a secret key for encryption and a MySQL database for storage. It also initializes a database connection using the SQLAlchemy library and the flask mail connection, and imports the URL routes and view functions defined in the routes module.
"""


app = Flask(__name__)  # Initialise the flask app

bcrypt = Bcrypt(app)   # Initialize the Bcrypt extension with the Flask app

# Set the app's configs
app.config["SECRET_KEY"] = f"{SECRET_KEY}"  # secret key for the WTForm forms you create
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://{DATABASEUSERNAME}:{PASSWORD}@localhost/{DATABASENAME}".format(
    PASSWORD=DATABASEPASSWORD, DATABASENAME=DATABASENAME,DATABASEUSERNAME=DATABASEUSERNAME)



# Set the app's session lifetime to 30 minutes
app.permanent_session_lifetime = timedelta(minutes=30)


# Configure Flask-Mail
app.config["MAIL_SERVER"] = 'smtp.gmail.com'  # Replace with your email server
app.config["MAIL_PORT"] = 587  # Replace with the appropriate port
app.config["MAIL_USE_TLS"] = True  # Enable TLS encryption
app.config["MAIL_USERNAME"] = MYEMAIL   # Replace with your email address
app.config["MAIL_PASSWORD"] = MYEMAILPASSWORD  # Replace with your email password


database = SQLAlchemy(app)  # Initialise the database connection
mail = Mail(app)            # Initialise the flask mail connection


GOOGLE_CLIENT_ID = GOOGLE_CLIENT_ID


def connect_to_api(url):
    response = requests.get(url)
    dataResponse = response.text
    connection = json.loads(
        dataResponse)  # deserializing - turns json string into python dictionary that can be now accessed

    return connection


from boredapp import routes
