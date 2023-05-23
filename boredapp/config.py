import os
import pathlib

from dotenv import load_dotenv

"""
    The code below sets up the necessary environmental variables for connecting to a MySQL database and sets a secret key.
"""

# load environmental variables
load_dotenv()

# Mysqlworkbench
# environmental variables stored

DATABASENAME = "boredapp_users"
USER = os.environ.get("USER")
DATABASEPASSWORD = os.environ.get("DATABASEPASSWORD")  # THIS IS YOUR MYSQLWORKBENCH PASSWORD
HOST = os.environ.get("HOST")
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")

OAUTHLIB_INSECURE_TRANSPORT = os.environ.get("OAUTHLIB_INSECURE_TRANSPORT")


# secret key
SECRET_KEY = os.environ.get("SECRET_KEY")

client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")


MYEMAIL=os.environ.get("MYEMAIL")
MYEMAILPASSWORD=os.environ.get("MYEMAILPASSWORD")
DUMMYEMAIL='boredapp@noreply.com'