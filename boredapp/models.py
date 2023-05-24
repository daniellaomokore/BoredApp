import psycopg2
from sqlalchemy import Column, Integer, String, ForeignKey, Index
from sqlalchemy.orm import relationship, declarative_base

if __name__ == '__main__':
    from config import DATABASEPASSWORD, DATABASENAME, HOST, PORT, DATABASEUSERNAME
else:
    from boredapp.config import DATABASEPASSWORD, DATABASENAME, HOST, PORT, DATABASEUSERNAME

from sqlalchemy import create_engine

Base = declarative_base()


# TO CREATE THE DATABASE
# Note: I put this in a function to prevent cnx from running when I run the app even when I haven't run the models file.
def create_database():
    """
    This function creates a new PostgreSQL database.
    """

    # Establish a connection to the PostgreSQL server
    cnx = psycopg2.connect(user=DATABASEUSERNAME, password=DATABASEPASSWORD, host=HOST, port=PORT)

    cnx.autocommit = True

    # Create a cursor object to execute SQL commands
    cursor = cnx.cursor()

    # Execute the SQL command to create the new database
    cursor.execute(f"CREATE DATABASE {DATABASENAME}")

    # Commit the transaction to make the database creation permanent
    #cnx.commit()

    # Close the cursor and the connection
    cursor.close()
    cnx.close()


class TheUsers(Base):
    __tablename__ = 'the_users'

    UserID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    FirstName = Column(String(65), nullable=False)
    LastName = Column(String(65), nullable=False)
    Email = Column(String(65), nullable=False, unique=True, index=True)
    Username = Column(String(200), index=True)
    Password = Column(String(200))

    def __init__(self, FirstName, LastName, Email, Username=None, Password=None):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.Username = Username
        self.Password = Password

    # Add the relationship attributes
    favourites = relationship('Favourites')


class Favourites(Base):
    __tablename__ = 'favourites'

    activityID = Column(Integer, primary_key=True, nullable=False)
    UserID = Column(Integer, ForeignKey('the_users.UserID'), nullable=False)
    activity = Column(String(200), nullable=False)
    participants = Column(Integer, nullable=False)
    type = Column(String(200), nullable=False)
    link = Column(String(200), nullable=False)

    __table_args__ = (
        Index('ix_favourites_activityID_UserID', 'activityID', 'UserID'),
    )

    def __init__(self, activityID, UserID, activity, participants, type, link):
        self.activityID = activityID
        self.UserID = UserID
        self.activity = activity
        self.participants = participants
        self.type = type
        self.link = link

    # Add the relationship attributes
    user = relationship('TheUsers')


engine = create_engine("postgresql+psycopg2://{user}:{password}@{host}:{port}/{databasename}".format(
    user=DATABASEUSERNAME,
    password=DATABASEPASSWORD,
    host=HOST,
    port=PORT,
    databasename=DATABASENAME,
))


def create_database_table():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_database()
    create_database_table()
