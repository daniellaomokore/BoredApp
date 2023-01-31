import os

# Mysqlworkbench

DATABASENAME = os.environ.get('DATABASENAME')
USER = os.environ.get('USER')
DATABASEPASSWORD = os.environ.get('DATABASEPASSWORD') # THIS IS YOUR MYSQLWORKBENCH PASSWORD
HOST = os.environ.get('HOST')

# secret key

SECRET_KEY = os.environ.get('SECRET_KEY')

