# BoredApp
 

I'm Currently developing the 'BoredApp' using Python, RESTApi , MySQL, SQL Alchemy, Flask, HTML & CSS.

API: https://www.boredapi.com/

NEW LEARNS:

-sqlalchemy 
-flask forms instead of html forms for validation, inputting images, documents etc, csrf token
-werkzeug
-'permanent_session_lifetime' for flask app
-how to use python code in html {{% %}}, {{}}
-bootstrap & customizing flashes/alert messages based on message type and colour and fading them awayover time

THINGS I DID TO OPTIMIZE THE APP/MAKE IT LESS EXPENSIVE/ FASTER/ SAFER

- i was going to use the exists query for login and signup but its expensive as it queries the db twice so instead i use just a single filter query to see if a row is returned or if none is returned.
- using sessions to store user email/username and id when they log in instead of repeatedly querying the database as Trips to database are slower than accessing sessions
- Hashing passwords using werkzeug
- wtforms = easy inbuilt validation for login and signup forms e.g email validators so i'm not reinventing the wheel + csrf token
- sqlalchemy to query the database instead of using raw sql to prevent SQL injection attacks

Libraries Used:
pymysql
Flask_WTF
Flask
datetime
flask_sqlalchemy
wtforms
werkzeug
requests