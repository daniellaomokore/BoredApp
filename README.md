# BoredApp
 

## 🚀<b>Usage</b>:

<i>The BoredApp assists users in generating a chosen activity to take part in based on number of participants, free & paid activities, paid activities with associated links, a specific type of activity or choose an activity at random.
            
Video Demo Link: https://clipchamp.com/watch/ZVdVr6OEF1Z
 
This version uses the MySQL database, there is an alternate 'postgress' branch compatible with Postgres.

 
<img width="552" alt="image" src="https://github.com/daniellaomokore/BoredApp/assets/79287671/3ce688bb-629f-4950-b5c0-c7fb53df7676">
<img width="415" alt="image" src="https://github.com/daniellaomokore/BoredApp/assets/79287671/7f51ea32-2b73-4c73-aae7-18f4e7854869"><img width="395" alt="image" src="https://github.com/daniellaomokore/BoredApp/assets/79287671/381ec885-544c-4b94-890a-db91255ec475">
<img width="380" alt="image" src="https://github.com/daniellaomokore/BoredApp/assets/79287671/bbb39569-3fc3-4a17-b5b0-40ec2d6a92fa">
<img width="917" alt="image" src="https://github.com/daniellaomokore/BoredApp/assets/79287671/dddd9af3-87e2-4dbd-a515-a272ebbabeb5">
<img width="920" alt="image" src="https://github.com/daniellaomokore/BoredApp/assets/79287671/eaad3bc8-a2d3-45fa-b591-cb6c288b7c25">


## ✨<b>My Favourite Features:</b>

- 3rd Party Google log in and sign up for users.

- Forgot password feature to generate a link sent to a user's email to reset password.

- 6-digit login verification code sent to users emails.

- Use of SQL Indexes in my relational MYSQL database to speed up database queries and make data retrieval more efficient.

- Use of the SQLAlchemy ORM instead of using raw SQL queries -> to prevent sql injection attacks.

- Password Hashing and salting for data security with bcyrpt.

- Clean & modular code, easy to understand & well commented code.

- Use of API and http requests.

- Use of Relational Database -> MySQL.

- Unit testing & good test coverage.



## <b>Things to add:</b>

- Dynamic front end design & more styling.
- Darkmode/lightmode.


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
8. Run the `models.py` at path `boredapp/models.py` file <b>directly</b> to create the database.
  
9. Run the `run.py` file in the root directory <b>directly</b> to run the App.
  
10. Open your browser and navigate to `http://localhost:5000` to access the App.
 


## ✨<b>How to Test:</b>

1. Run the `test.py` file in the root directory <b>directly</b>.

 Code Structure reference: https://youtu.be/44PvX0Yv368

