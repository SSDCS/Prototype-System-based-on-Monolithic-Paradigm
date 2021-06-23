from flask import Flask,render_template, url_for, session, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from functools import wraps
from Application import db
from Application import bcrypt
from Application.auth.forms import Login, Registration
from Application.models import Admin, Astronaut
from Application.auth import bp
#decorator function to check if user baccessing certain paths are authenticated, if not they are taken back to login
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "username" in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first!")
            return redirect(url_for("astronautlogin"))
    return wrap

#decorator function to check if administrative user accessing certain paths are authenticated, if not they are taken back to login
def adminlogin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "adminusername" in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first!")
            return redirect(url_for("bp.adminlogin"))
    return wrap

@bp.route("/", methods=["POST", "GET"])
def adminlogin():
    if "adminusername" in session:
        return redirect(url_for('bp.admindashboard'))# this is for persistence purposes, if the user is logged in they should stay logged in.
    form=Login(request.form) # create an instace of the login form
    if request.method == 'POST' and form.validate(): #if the method is post and the form validates
        admin=Admin.query.filter_by(username=form.username.data).first()#find the astronaut in the database
        if admin and bcrypt.check_password_hash(admin.password, form.password.data): #if the astronaut exists and the password hash matches the hash fro entered password
            session['adminusername']=form.username.data #add the user to session
            flash(f'Welcome {form.username.data}. You are now logged in.', 'success')
            return redirect(request.args.get('next') or url_for('bp.admindashboard'))
        else:
            flash(f'Wrong password/email. Please try again.', 'danger')
    return render_template("admin/login.html", form=form, title="Login page")

#this path should only be acccessible to logged in administartors so we use the decorator.
@bp.route("/dashboard")
@adminlogin_required #applying the adminlogin decorator
def admindashboard():
    return "<h1>Welcome to admin dashboard</h1>"

#this is for admin registration
@bp.route("/register", methods=["POST", "GET"])
def register():
    form=Registration(request.form) #create an instace of the registration form
    if request.method == 'POST' and form.validate(): # if the reuest method is post 
        hashedpass=bcrypt.generate_password_hash(form.password.data)#encrypt the password
        admin = Admin(name=form.name.data, username=form.username.data, email=form.email.data, password=hashedpass)
        db.session.add(admin) #add data to the db
        db.session.commit() #commit the process for the actual save.
        flash(f'Welcome {form.username.data}. Thank you for registering.', 'success')
        return redirect(url_for("bp.adminlogin"))
    return render_template("admin/register.html", form=form)

#this is for admin logout
@bp.route("/logout")
@login_required #applying the login decorator.
def logout():
    session.clear()
    flash("You have successfully logged out.")
    return redirect(url_for("bp.adminlogin"))


#astromaut login page
@bp.route("/", methods=["POST", "GET"])
def astronautlogin():
    if "username" in session:
        return redirect(url_for('dashboard')) #for persistence purposes
    form=Login(request.form) # create an instace of the login form
    if request.method == 'POST' and form.validate(): #if the method is post and the form validates
        astronaut=Astronaut.query.filter_by(username=form.username.data).first()#find the astronaut in the database
        if astronaut and bcrypt.check_password_hash(astronaut.password, form.password.data): #if the astronaut exists and the password hash matches the hash fro entered password
            session['username']=form.username.data #add the user to session
            flash(f'Welcome {form.username.data}. You are now logged in.', 'success')
            return redirect(request.args.get('next') or url_for('dashboard'))
        else:
            flash(f'Wrong password/email. Please try again.', 'danger')
    return render_template("astronaut/login.html", form=form, title="Login page")

#this route also should only be accessible to logged in astronaut
@bp.route('/dashboard')
@login_required #applying the login decorator.
def dashboard():
    return "<h1>Welcome to dashboard</h1>"

@bp.route("/register", methods=["POST", "GET"])
def register():
    form=Registration(request.form) #create an instace of the Registration form
    if request.method == 'POST' and form.validate(): # if the request method is post 
        hashedpass=bcrypt.generate_password_hash(form.password.data)#encrypt the password
        astronaut = Astronaut(name=form.name.data, username=form.username.data, email=form.email.data, password=hashedpass)
        db.session.add(astronaut) #add to db
        db.session.commit() #commit the process for the actual save.
        flash(f'Welcome {form.username.data}. Thank you for registering.', 'success')
        return redirect(url_for("astronautlogin"))
    return render_template("astronaut/register.html", form=form)

#astronaut logout route
@bp.route("/logout")
@login_required #applying the login decorator.
def logout():
    session.clear() #clear the session values
    flash("You have successfully logged out.")
    return redirect(url_for("astronautlogin")) #then redirecting to login