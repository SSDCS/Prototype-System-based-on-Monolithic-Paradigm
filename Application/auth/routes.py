"""
Authentication routes 
"""
from flask import render_template, url_for, session, request, redirect, flash
from Application import db
from Application import ph
from Application.auth.forms import Login, Registration
from Application.models import Admin, Astronaut
from Application.auth import bp
from ..decorators import login_required


@bp.route("/", methods=["POST", "GET"])
def login():
    """ This function is reposible for all login requests
    Args:
        None

    Returns:
        ON GET:
            If: user is not logged in return login.html
            Else: return dashboard.index
    """
    if "username" in session:
        # for persistence purposes
        return redirect(url_for('dashboard.index'))
    form = Login(request.form) # create an instace of the login form
    if request.method == 'POST' and form.validate():  # if the method is post and the form validates
        admin = Admin.query.filter_by(username=form.username.data).first()
        # find the astronaut in the database
        astronaut = Astronaut.query.filter_by(
            username=form.username.data).first()
        # if the astronaut exists and the password hash matches the hash fro entered password
        if astronaut and ph.verify(astronaut.password, form.password.data):
            session['myuser'] = "astronaut"
            session['username'] = form.username.data  # add the user to session
            return redirect(request.args.get('next') or url_for('dashboard.index'))
        elif admin and ph.verify(admin.password, form.password.data):
            session['myuser'] = "admin"
            session['username'] = form.username.data  # add the user to session
            return redirect(request.args.get('next') or url_for('dashboard.index'))
        else:
            flash('Wrong password/email. Please try again.', 'danger')
    return render_template("login.html", form=form, title="Login page")


@bp.route("/register", methods=["POST", "GET"])
@login_required
def register():
    """ This function is used to register new users

    Args:
        None.

    Returns:
        register.html
    """
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
            hashedpass = ph.hash(
                form.password.data)  # encrypt the password
            astronaut = Astronaut(name=form.name.data, username=form.username.data,
                                  email=form.email.data, password=hashedpass,
                                  admin_id=session['username'])
            db.session.add(astronaut)  # add to db
            db.session.commit()  # commit the process for the actual save.
            flash(f'Astronuat {form.username.data} registered!', 'success')
            return redirect(url_for("auth.login"))
    return render_template("register.html", form=form)

# astronaut logout route


@bp.route("/logout")
@login_required  # applying the login decorator.
def logout():
    """ This function is used to terminate the session cookie

    Args:
        None

    Returns:
        auth.login route which propts user to login
    """
    session.clear()  # clear the session values
    flash("You have successfully logged out.")
    return redirect(url_for("auth.login"))  # then redirecting to login
