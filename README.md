# BoredApp
 

## 🚀<b>Usage</b>:

<i>The BoredApp assists users in generating a chosen activity to take part in based on number of participants, free & paid activities, paid activities with associated links, a specific type of activity or choose an activity at random.
            
Video Demo Link: https://clipchamp.com/watch/ZVdVr6OEF1Z
 
This version uses the MySQL database, there is an alternate 'postgress' branch compatible with Postgres.

## ✨<b>My Favourite Features:</b>

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



## <b>Things to add:</b>

- Dynamic front end design & more styling
- Darkmode/lightmode


## ✨<b>Installation</b>
1. Clone the repository:

``` git clone https://github.com/daniellaomokore/BoredApp.git ```

2. Change into the project directory:

``` cd BoredApp ```

3. Create a virtual environment:

```python3 -m venv venv```

4. Activate the virtual environment:
- For Mac/Linux:
  ```source venv/bin/activate```
- For Windows:
  ```venv\Scripts\activate```
5. Install the required dependencies:

```pip install -r requirements.txt```
 

6. Create a `.env` file in the project root directory.

7. Add the following configuration variables:
  ``` USER = "[your MYSQL user]"
  DATABASEPASSWORD = "[your MYSQL password]"  
  HOST = "[your MYSQL host]" 
  SECRET_KEY = "[your secret key]"
  MYEMAIL="[your email]"
  MYEMAILPASSWORD="[your email password]"
 
  ```
8. Run the models.py at path `boredapp/models.py` file <b>directly</b> to create the database.
  
9. Run the Flask development server in the root directory:
 
 ```python run.py```
 
10. Open your browser and navigate to `http://localhost:5000` to access the app.
 
## ✨<b>How to Test:</b>

1. Run the test file in the root directory.
 ```python test.py```

 Code Structure reference: https://youtu.be/44PvX0Yv368
