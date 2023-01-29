# don't need this
import mysql.connector
from config import USER, HOST, PASSWORD

my_database = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    auth_plugin='mysql_native_password',
    database="BoredApp_users"
)

my_cursor = my_database.cursor(buffered=True)  # the cursor communicated with your mySQL server

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)
