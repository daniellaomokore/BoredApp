import sqlalchemy
from boredapp import database

if __name__ == '__main__':
    from config import DATABASEPASSWORD, DATABASENAME, HOST, USER
else:
    from boredapp.config import DATABASEPASSWORD, DATABASENAME, USER, HOST
from sqlalchemy import create_engine, orm

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

Base.metadata.create_all(engine)





