from wtforms import Form, PasswordField, validators, SubmitField, StringField

# using wtforms to create registration and login forms


class Registration(Form):
    name = StringField("Name:")
    username = StringField("Username:", [validators.DataRequired()])
    email = StringField('Email Address:', [
                        validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField('New Password:', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password:')
    role = SelectField('Role:', [validators.DataRequired()], choices=[
                       ('admin', 'Admin'), ('astronaut', 'Astronaut')], validate_choice=True)
    submit = SubmitField("Submit")


class Login(Form):
    username = StringField("Username:", [validators.DataRequired()])
    password = PasswordField('Your Password', [validators.DataRequired()])
