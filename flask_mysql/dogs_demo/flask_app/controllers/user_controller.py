from types import MethodDescriptorType
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.dog import Dog
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():

    if not User.validate_register(request.form):
        return redirect("/")

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    user_id = User.save_user(data)

    session["user_id"] = user_id

    return redirect("/dashboard")


@app.route("/login", methods=["POST"])
def login():

    if not User.validate_login(request.form):
        return redirect("/")

    user_from_db = User.get_by_email(request.form)
    session["user_id"] = user_from_db.id

    return redirect("/dashboard")

# =====================================
# Dashboard


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("Please register or login!")
        return redirect("/")

    data = {
        "user_id": session["user_id"]
    }
    user = User.get_by_id(data)
    all_dogs = Dog.all_dogs_with_owners()
    return render_template("dashboard.html", user=user, all_dogs=all_dogs)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
