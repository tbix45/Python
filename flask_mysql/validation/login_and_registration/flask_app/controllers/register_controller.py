from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
# ===========SHOW================


@app.route("/")
def login_and_register():
    return render_template("login_reg.html")


@app.route("/user_dashboard")
def user_dashboard():
    data = {
        'user_id': session["user_id"],
        # "email": ["email"] ==============Cant figure out how to display on html
    }
    user = User.get_user_info(data)
    return render_template("user_dashboard.html", user=user)
# =================================
# ===========PROCESS================


@app.route("/user_register", methods=["POST"])
def user_register():
    if not User.validate_user(request.form):
        # we redirect to the template with the form.
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash
    }

    session["user_id"] = User.save_user(data)
    return redirect("/user_dashboard")


@app.route("/user_login", methods=["POST"])
def user_login():
    data = {
        'email': request.form["email"]
    }
    user_in_db = User.get_by_email(data)
    validation_data = {
        'user_in_db': user_in_db,
        "password": request.form["password"]
    }
    if not User.validate_login(validation_data):
        return redirect("/")
    session["user_id"] = user_in_db.id
    return redirect("/user_dashboard")
# =================================
# LOGOUT


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
