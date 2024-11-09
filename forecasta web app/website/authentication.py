from flask import Blueprint, render_template, request

#user-management api
authentication = Blueprint('authentication', __name__)
#blueprint to class urls

#decorator(url) followed by function which produces json or html etc
#our init file runs the apis
@authentication.route('/login')
def login():
    return render_template("login.html", boolean=True)


@authentication.route('/logout')
def logout():
    return "<h1></h1>"

@authentication.route('/sign-up')
def sign_up():
    return render_template("sign_up.html", boolean=True)
