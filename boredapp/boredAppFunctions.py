from flask import session
from sqlalchemy import and_
from boredapp import database, connect_to_api
from boredapp.models import TheUsers, Favourites

APIurl = "http://www.boredapi.com/api/activity"


def display_the_activity(activityID):
    """
        Display activity info, we can use if else statements to format the string in certain ways depending on what the activity selection was based on

    """

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


def check_if_activity_is_in_favourites(activityID, UserID):
    favouritesExists = database.session.query(Favourites).filter_by(activityID=activityID, UserID=UserID).first()

    if favouritesExists:  # if True
        return True
    else:  # if False
        return False


# this must be called after a user has logged in, so we can save the user's UserID into the session for later use
def get_user_id():
    # query user id where email/username is
    if 'Email' in session:
        # query the user by their email
        current_user = database.session.query(TheUsers).filter_by(Email="{}".format(session['Email'])).first()

    elif 'Username' in session:
        # query the user by their username
        current_user = database.session.query(TheUsers).filter_by(Username="{}".format(session['Username'])).first()

    UserID = current_user.UserID  # select their UserID column

    return UserID


def get_user_firstname():
    # query user firstname where email/username is
    if 'Email' in session:
        # query the user by their email
        current_user = database.session.query(TheUsers).filter_by(Email="{}".format(session['Email'])).first()

    elif 'Username' in session:
        # query the user by their username
        current_user = database.session.query(TheUsers).filter_by(Username="{}".format(session['Username'])).first()

    FirstName = current_user.FirstName  # select their FirstName column

    return FirstName.capitalize()


def is_user_logged_in():
    if "UserID" in session:  # if the user has logged in
        return True
    else:
        return False
