from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

SECRET_KEY = "my_secret_key"



def create_app():

    from .views import views

    from .auth import auth

    app = Flask(__name__)
    SECRET_KEY = "my_secret_key"

    app.config['SECRET_KEY'] = '{}'.format(SECRET_KEY)  # secret key for the WTForm forms you create
    app.register_blueprint(auth, url_prefix="/")
    #app.register_blueprint(views, url_prefix="/")


    app.permanent_session_lifetime = timedelta(days=1)  # this lets us store out permanent session data for x days/minutes etc so the user doesn't have to re-login everytime they close the tab

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Softqueen123!@localhost/BoredApp_users'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    database = SQLAlchemy(app)

    return app
