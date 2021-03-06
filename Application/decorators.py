from functools import wraps
from flask import url_for, redirect, flash, session

def login_required(f):
    #decorator wrap make function wrap to look like f funcion  
    @wraps(f)
    def wrap(*args, **kwargs):
        #checking if username is logged already in
        if "username" in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first!")
            return redirect(url_for("auth.login"))
    return wrap