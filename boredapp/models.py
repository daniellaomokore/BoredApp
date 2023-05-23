import sqlalchemy
import mysql.connector
from boredapp import database

if __name__ == '__main__':
    from config import DATABASEPASSWORD, DATABASENAME, HOST, USER
else:
    from boredapp.config import DATABASEPASSWORD, DATABASENAME, USER, HOST
from sqlalchemy import create_engine, orm, Index

Base = sqlalchemy.orm.declarative_base()

# TO CREATE THE DATABASE
# Note: I put this in a function to prevent cnx from running when i run the app even when i haven't ran the models file.
def create_database():
    """
    This function creates a new MYSQL database.
    """
    # Establish a connection to the MySQL server
    cnx = mysql.connector.connect(user=USER, password=DATABASEPASSWORD, host=HOST)

    # Create a cursor object to execute SQL commands
    cursor = cnx.cursor()

    # Execute the SQL command to create the new database
    cursor.execute(f"CREATE DATABASE {DATABASENAME}")

    # Commit the transaction to make the database creation permanent
    cnx.commit()

    # Close the cursor and the connection
    cursor.close()
    cnx.close()


# DATABASE TABLE SCHEMA

Base = sqlalchemy.orm.declarative_base()


class TheUsers(Base):
    """
        This function creates a new MYSQL database table.
    """
    __tablename__ = 'the_users'

    UserID = database.Column(database.Integer, primary_key=True, autoincrement=True, nullable=False)
    FirstName = database.Column(database.String(65), nullable=False)
    LastName = database.Column(database.String(65), nullable=False)
    Email = database.Column(database.String(65), nullable=False, unique=True, index=True)  # create index for Email column
    Username = database.Column(database.String(200), index=True)  # create index for Username column
    Password = database.Column(database.String(200))

    def __init__(self, FirstName, LastName, Email, Username=None, Password=None): # Set Username & Password to Default None becuase if a user signs up with google account then those arguments aren't needed
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.Username = Username
        self.Password = Password


class Favourites(Base):
    """
        This function creates a new MYSQL database table.
    """
    __tablename__ = 'favourites'

    activityID = database.Column(database.Integer, primary_key=True, nullable=False)
    UserID = database.Column(database.Integer, database.ForeignKey('the_users.UserID'), nullable=False)
    activity = database.Column(database.String(200), nullable=False)
    participants = database.Column(database.Integer, nullable=False)
    type = database.Column(database.String(200), nullable=False)
    link = database.Column(database.String(200), nullable=False)

    def __init__(self, activityID, UserID, activity, participants, type, link):
        self.activityID = activityID
        self.UserID = UserID
        self.activity = activity
        self.participants = participants
        self.type = type
        self.link = link

        # create 2 column index for activity id and user id.
        __table_args__ = (
            Index('ix_favourites_activityID_UserID', 'activityID', 'UserID'),
        )


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
