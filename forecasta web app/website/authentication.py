from flask import Blueprint, render_template, request, flash, redirect, url_for
import re
import pg8000

#user-management api
authentication = Blueprint('authentication', __name__)
#blueprint to class urls

#decorator(url) followed by function which produces json or html etc
#our init file runs the apis
@authentication.route('/login', methods=['GET','POST'])
def login():
    print(request.form)
    return render_template("login.html", boolean=True)


@authentication.route('/logout', methods=['GET','POST'])
def logout():
    print(request.form)
    return render_template("base.html", boolean=True)

@authentication.route('/sign-up', methods=['GET','POST'])
def sign_up():
    print(request.form)

    if request.method == "POST":
        UserName = request.form.get('UseNameInp')
        Password = request.form.get('PasswordInp')
        RepPassword = request.form.get('RepPasswordInp')

        if Password != RepPassword:
            pass
        elif len(Password) < 8 or len(RepPassword) < 8:
            pass
        elif not re.search("[a-z]" , Password) or not re.search("[a-z]" , RepPassword):
            pass
        elif not re.search("[A-Z]" , Password) or not re.search("[A-Z]" , RepPassword):
            pass
        elif not re.search("[0-9]" , Password) or not re.search("[0-9]" , RepPassword):
            pass
        elif not re.search(r"[!@#$%^&*()\-_+=\\|~`\"'<>.,?{}\[\]:;]" , Password) or not re.search(r"[!@#$%^&*()\-_+=\\|~`\"'<>.,?{}\[\]:;]", RepPassword):
            pass
        else:
            #connect to db
            connection = pg8000.connect(database="ForecastaDB", user="postgres", password="Password123!", host="localhost", port="5432")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users(user_name,password) VALUES(%s,%s);",(UserName,Password))
            connection.commit() 
            cursor.close() 
            connection.close() 
    return render_template("sign_up.html", boolean=True)
