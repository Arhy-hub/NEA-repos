from flask import Blueprint, render_template, request, flash

#user-management api
authentication = Blueprint('authentication', __name__)
#blueprint to class urls

#decorator(url) followed by function which produces json or html etc
#our init file runs the apis
@authentication.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html", boolean=True)


@authentication.route('/logout')
def logout():
    return "<h1></h1>"

@authentication.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == "POST":
        UserName = request.form.get('UserNameInp')
        Password1 = request.form.get('PasswordInp')
        Password2 = request.form.get('RepPasswordInp')

        if len(UserName) <= 2:
            flash('Username is too short. It must be greater than 2 characters', category='error')
        elif len(Password1) < 8 or len(Password2) < 8:
            flash('Password length is too short. It must at least be 8 characters', category='error')
        elif Password1 != Password2:
            flash('Passwords do not match', category='error')
        else:
            #add user to db
            pass
    return render_template("sign_up.html", boolean=True)
