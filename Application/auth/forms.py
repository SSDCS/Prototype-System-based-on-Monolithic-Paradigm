""" Authentication Blueprint Forms

The following forms are used exclusively within the authentication blueprint.
Two forms are defined below, registration and login.

Registration:
    The registration form is used exclusively by administrators to create new users in the system.
    Email and password validation is performed using the following methods within wtforms:
     - validators.DataRequired(),validators.Length(min=8)
     - validators.Regexp("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{8,}$",
       message="All passwords should contain a lowercase, an uppercase and a number")
     - validators.EqualTo('confirm', message='Passwords must match')

Login:
    The login form is used by all users who wish to access the system

"""
from wtforms import Form, PasswordField, validators, SubmitField, StringField, SelectField


class Registration(Form): # pylint: disable=too-few-public-methods
    """ Define the structure of the registration form

    Args:
        Form: Inherits the wtform libary

    Returns:
        None

    Validators:
        All fields except for name make use of validators to ensure that the entered
        data meets a specific requirement if provided.

        username - Prompt user to enter a username if none provided
        email - If email entered in incorrect format prompt user for correct email
        password - Password must meet unique contraints
        role - role must be selected

    """
    name = StringField("Name:")
    username = StringField("Username:", [validators.DataRequired()])
    email = StringField('Email Address:', [
                        validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField('New Password:', [
        validators.DataRequired(), validators.Length(min=8),
        validators.Regexp(
            "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{8,}$", 
            message="All passwords should contain a lowercase, an uppercase and a number"),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password:')
    role = SelectField('Role:', [validators.DataRequired()], choices=[
                       ('admin', 'Admin'), ('astronaut', 'Astronaut')], validate_choice=True)
    submit = SubmitField("Submit")


class Login(Form): # pylint: disable=too-few-public-methods
    """ Defines the form used for user login

    Args:
        Form: Inherits the form functions from the wtforms library

    Returns:
        None
    """
    username = StringField("Username:", [validators.DataRequired()])
    password = PasswordField('Your Password', [validators.DataRequired()])
