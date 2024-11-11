from flask import Blueprint, render_template, request, flash


#user-management api
authentication = Blueprint('authentication', __name__)
#blueprint to class urls

#decorator(url) followed by function which produces json or html etc
#our init file runs the apis
@authentication.route('/login', methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)


@authentication.route('/logout', methods=['GET','POST'])
def logout():
    print(request.form)
    return render_template("base.html", boolean=True)

@authentication.route('/sign-up', methods=['GET','POST'])
def sign_up():
    print(request.form)
    return render_template("sign_up.html", boolean=True)
