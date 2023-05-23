from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo


# Form for sign up
class SignUpForm(FlaskForm):
    """
        This class creates a submission form for the user sign up
    """
    firstname = StringField("Firstname:", validators=[DataRequired()])
    lastname = StringField("Lastname", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign Up")


# Form for log in
class LogInForm(FlaskForm):
    """
        This class creates a submission form for the user log in
    """
    email_or_username = StringField("email_or_username:", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log in")


# Form for forgot password
class ForgotPassword(FlaskForm):
    """
        This class creates a submission form for the user forgot password form
    """
    email = EmailField("Email", validators=[DataRequired()])
    submit = SubmitField("Reset Password")


class ResetPassword(FlaskForm):
    password = PasswordField('New Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Submit')


class VerifyLogin(FlaskForm):
    user_verification_code = PasswordField('Enter Code', validators=[DataRequired()])
    submit = SubmitField('Submit')
