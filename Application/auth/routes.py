from flask import Flask, render_template, url_for, session, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from functools import wraps
from Application import db
from Application import bcrypt
from Application.auth.forms import Login, Registration
from Application.models import Admin, Astronaut
from Application.auth import bp
from ..decorators import login_required

# decorator function to check if user baccessing certain paths are authenticated, if not they are taken back to login


# def login_required(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         if "username" in session:
#             return f(*args, **kwargs)
#         else:
#             flash("You need to login first!")
#             return redirect(url_for("auth.login"))
#     return wrap


user = ""
# astromaut login page


@bp.route("/", methods=["POST", "GET"])
def login():
    global user
    if "username" in session:
        # for persistence purposes
        return redirect(url_for('dashboard.index'))
    form = Login(request.form)  # create an instace of the login form
    if request.method == 'POST' and form.validate():  # if the method is post and the form validates
        admin = Admin.query.filter_by(username=form.username.data).first()
        # find the astronaut in the database
        astronaut = Astronaut.query.filter_by(
            username=form.username.data).first()
        # if the astronaut exists and the password hash matches the hash fro entered password
        if astronaut and bcrypt.check_password_hash(astronaut.password, form.password.data):
            user = "astronaut"
            session['username'] = form.username.data  # add the user to session
            return redirect(request.args.get('next') or url_for('dashboard.index'))
        elif admin and admin and bcrypt.check_password_hash(admin.password, form.password.data):
            user = "admin"
            session['username'] = form.username.data  # add the user to session
            return redirect(request.args.get('next') or url_for('dashboard.index'))
        else:
            flash(f'Wrong password/email. Please try again.', 'danger')
    return render_template("login.html", form=form, title="Login page")

# this route also should only be accessible to logged in astronaut


# @bp.route('/dashboard')
# @login_required  # applying the login decorator.
# def dashboard():
#     return render_template("dashboard.html", user=user)


@bp.route("/register", methods=["POST", "GET"])
@login_required
def register():
    # create an instace of the Registration form
    form = Registration(request.form)
    if request.method == 'POST' and form.validate():  # if the request method is post
        hashedpass = bcrypt.generate_password_hash(
            form.password.data)  # encrypt the password
        if form.role.data == 'admin':
            admin = Admin(name=form.name.data, username=form.username.data,
                          email=form.email.data, password=hashedpass)
            db.session.add(admin)  # add to db
            db.session.commit()  # commit the process for the actual save.
            flash(f'Admin {form.username.data} registered!', 'success')
            return redirect(url_for("auth.login"))
        else:
            hashedpass = bcrypt.generate_password_hash(
                form.password.data)  # encrypt the password
            astronaut = Astronaut(name=form.name.data, username=form.username.data,
                                  email=form.email.data, password=hashedpass, admin_id=session['username'])
            db.session.add(astronaut)  # add to db
            db.session.commit()  # commit the process for the actual save.
            flash(f'Astronuat {form.username.data} registered!', 'success')
            return redirect(url_for("auth.login"))
    return render_template("register.html", form=form)

# astronaut logout route


@bp.route("/logout")
@login_required  # applying the login decorator.
def logout():
    session.clear()  # clear the session values
    flash("You have successfully logged out.")
    return redirect(url_for("auth.login"))  # then redirecting to login
