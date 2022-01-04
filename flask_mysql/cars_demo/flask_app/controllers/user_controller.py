from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
# =======SHOW================


@app.route("/")
def reg_login():
    return render_template("reg_login.html")


@app.route("/dashboard")
def dashboard():

    data = {
        "user_id": session["user_id"]
    }
    user = User.get_user_info(data)
    return render_template("dashboard.html", user=user)
# ===========================
# Process


@app.route("/register", methods=["POST"])
def register():
    # validate user first. before adding to database
    if not User.validate_register(request.form):
        return redirect("/")

    # hash password before passing it into data object and into database
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash
    }
    # check if email already in use

    # call the save @classmethod on User
    user_id = User.save_user(data)

    # store user id into session

    session["user_id"] = user_id
    return redirect("/dashboard")


@app.route("/login", methods=["POST"])
def login():
    data = {
        "email": request.form["email"]
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")

    validation_data = {
        "user_in_db": user_in_db,
        "password": request.form["password"]
    }
    if not User.validate_login(validation_data):
        return redirect("/")
    # if passwords matched, we set the user_id into session
    session["user_id"] = user_in_db.id

    return redirect("/dashboard")


# ==============LOGOUT=================
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
