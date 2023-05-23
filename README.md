# BoredApp
 

🚀<b>Usage</b>:

<i>The BoredApp assists users in generating a chosen activity to take part in based on number of participants, free & paid activities, paid activities with associated links, a specific type of activity or choose an activity at random.
            
Video Demo Link: https://clipchamp.com/watch/ZVdVr6OEF1Z
 
<b>My Favourite Features:</b>

- 3rd Party Google log in and sign up for users.

- Forgot password feature to generate a link sent to a user's email to reset password.

- 6-digit login verification code sent to users emails.

- Use of SQL Indexes in my relational MYSQL database to speed up database queries and make data retrieval more efficient.

- Use of the SQLAlchemy ORM instead of using raw SQL queries -> to prevent sql injection attacks.

- Password Hashing and salting for data security with bcyrpt.

- Clean & modular code, easy to understand & well commented code.

- Use of API and http requests

- Use of Relational Database -> MySQL

- Unit testing & good test coverage.



<b>Things to add:</b>

- Dynamic front end design & more styling
- Darkmode/lightmode


✨<b>How to Run:</b>

* Install the dependencies by running `pip install -r requirements.txt` in the terminal or command prompt on your system.

* Run the 'models.py' file once to create your database and it's tables.

* set up your environmental variables in a '.env' file in the root. With variables for :
  * USER = "[your MYSQL user]"
  * DATABASEPASSWORD = "[your MYSQL password]"  
  * HOST = "[your MYSQL host]" 
  * SECRET_KEY = "[your secret key]"
  * MYEMAIL="[your email]"
  * MYEMAILPASSWORD="[your email password]"

* Run `python run.py` in the terminal of the root directory of the project or run the 'run.py' file directly and then click the link: http://127.0.0.1:5000.




✨<b>How to Test:</b>

* Run `python test.py` in the terminal of the root directory of the project or run the 'test.py' file directly.

 Code Structure reference: https://youtu.be/44PvX0Yv368
