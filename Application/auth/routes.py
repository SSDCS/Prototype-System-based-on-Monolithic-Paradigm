"""Authentication Blueprint

 The following Flask Blueprint defines URL's/routes for all authentication requests.

login:
    The login route begins by establishing whether a user is logged in to the system.
    If the user is not logged in, they are presented with a login form.
    When completing the form, we evaluate whether the username entered is
    an administrator or astronaut, followed by verifying whether the password
    entered matches the stored hash in the database.


register:
    The register route is only accessible by administrators, and this is determined
    within the dashboard template.
    The administrator is presented with a registration form '/Application/auth/forms.py'.
    The administrator has the choice of creating additional administrator and astronaut accounts.

logout:
    The logout route is used to log users out of the system by clearing the session cookie stored
    on the system accessing the application.

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
    """ Function is reposible for login requests
    Args:
        None

    Returns:
        ON GET:
            If: user is not logged in return login.html
            Else: return dashboard.index
    """
    if "username" in session:  # If username in session redirect to dashboard
        return redirect(url_for('dashboard.index'))
    form = Login(request.form)  # create an instace of the login form
    if request.method == 'POST' and form.validate():
        # Query whether admin exists
        admin = Admin.query.filter_by(username=form.username.data).first()
        # Query whether astronaut exists
        astronaut = Astronaut.query.filter_by(
            username=form.username.data).first()
        # If user is astronaut verify username and password then redirect to dashboard
        if astronaut:
            try:
                ph.verify(astronaut.password, form.password.data)
                # Add astronaut user type to session cookie
                session['myuser'] = "astronaut"
                session['username'] = form.username.data
                return redirect(request.args.get('next') or url_for('dashboard.index'))
            except:
                flash('Incorrect Password.', 'danger')
        # If user is admin verify username and password then redirect to dashboard
        elif admin:
            try:
                ph.verify(admin.password, form.password.data)
                # Add admin user type to session cookie
                session['myuser'] = "admin"
                session['username'] = form.username.data
                return redirect(request.args.get('next') or url_for('dashboard.index'))
            except:
                flash('Incorrect Password.', 'danger')
        else:
            flash('Incorrect Username or Password.', 'danger')
    return render_template("login.html", form=form, title="Login page")


@bp.route("/register", methods=["POST", "GET"])
@login_required
def register():
    """ Function provides registration form used by administators

    Args:
        None.

    Returns:
        register.html
    """
    # Create an instace of the Registration form
    form = Registration(request.form)
    if request.method == 'POST' and form.validate():
        hashedpass = ph.hash(
            form.password.data)  # Hash password
        if form.role.data == 'admin':
            admin = Admin(name=form.name.data, username=form.username.data,
                          email=form.email.data, password=hashedpass)
            existing_user = Admin.query.filter_by(
                username=form.username.data).first()
            if existing_user:
                flash('User Already Exists', 'danger')
            else:
                db.session.add(admin)  # Add admin to session
                db.session.commit()  # Persist session to database
                flash(f'Admin {form.username.data} registered!', 'success')
                return redirect(url_for("auth.login"))
        else:
            hashedpass = ph.hash(
                form.password.data)  # Hash password
            astronaut = Astronaut(name=form.name.data, username=form.username.data,
                                  email=form.email.data, password=hashedpass,
                                  admin_id=session['username'])
            existing_user = Astronaut.query.filter_by(
                username=form.username.data).first()
            if existing_user:
                flash('User Already Exists', 'danger')
            else:
                db.session.add(astronaut)  # Add astronaut to session
                db.session.commit()  # Persist session to database
                flash(f'Astronuat {form.username.data} registered!', 'success')
                return redirect(url_for("auth.login"))
    return render_template("register.html", form=form)


@bp.route("/logout")
@login_required  # applying the login decorator.
def logout():
    """ Function clears session cookie and redirects to login page

    Args:
        None

    Returns:
        auth.login route which propts user to login
    """
    session.clear()  # clear the session cookie
    flash("You have successfully logged out.")
    return redirect(url_for("auth.login"))  # Redirect to login page
