import sqlalchemy
import mysql.connector
from boredapp import database
from flask_sqlalchemy import SQLAlchemy

if __name__ == '__main__':
    from config import DATABASEPASSWORD, DATABASENAME, HOST, USER
else:
    from boredapp.config import DATABASEPASSWORD, DATABASENAME, USER, HOST
from sqlalchemy import create_engine, orm

Base = sqlalchemy.orm.declarative_base()

# TO CREATE THE DATABASE
# Note: I put this in a function to prevent cnx from running when i run the app even when i haven't ran the models file.
def create_database():
    # Establish a connection to the MySQL server
    cnx = mysql.connector.connect(user=USER, password=DATABASEPASSWORD, host=HOST)

    # Create a cursor object to execute SQL commands
    cursor = cnx.cursor()

    # Execute the SQL command to create the new database
    cursor.execute("CREATE DATABASE {}".format(DATABASENAME))

    # Commit the transaction to make the database creation permanent
    cnx.commit()

    # Close the cursor and the connection
    cursor.close()
    cnx.close()


# DATABASE TABLE SCHEMA

Base = sqlalchemy.orm.declarative_base()


class TheUsers(Base):
    __tablename__ = 'the_users'

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


class Favourites(Base):
    __tablename__ = 'favourites'

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


engine = create_engine("mysql+mysqlconnector://{user}:{password}@{host}/{DatabaseName}".format(
    user=USER,
    password=DATABASEPASSWORD,
    host=HOST,
    DatabaseName=DATABASENAME
))


def create_database_table():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_database()
    create_database_table()



