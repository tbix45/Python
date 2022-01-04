from flask_app import app
from flask import redirect, render_template, request, session, flash
from flask_app.models.user import User
from flask_app.models.trip import Trip
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# ========================
# Show login/reg page
# ========================


@app.route("/")
def show_login_reg():
    return render_template("login_reg.html")

# ========================
# Process registration page
# ========================


@app.route("/register", methods=["POST"])
def register_user():
    if not User.validate_register(request.form):
        return redirect("/")
    pw_hash = bcrypt.generate_password_hash(request.form["password"])

    data = {
        "username": request.form["username"].title(),
        "first_name": request.form["first_name"].title(),
        "last_name": request.form["last_name"].title(),
        "email": request.form["email"],
        "password": pw_hash
    }
    # call the save user method on user
    user_id = User.save_user(data)
    session["user_id"] = user_id
    return redirect("/dashboard")

# ========================
# Process login page
# ========================


@app.route("/login", methods=["POST"])
def login_user():
    data = {
        "email": request.form["email"]
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password!")
        return redirect("/")
    validation_data = {
        "user_in_db": user_in_db,
        "password": request.form["password"]
    }
    if not User.validate_login(validation_data):
        return redirect("/")
    session["user_id"] = user_in_db.id

    return redirect("/dashboard")


# ========================
# Show Dashboard Page
# ========================
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("Please register or login!")
        return redirect("/")
    data = {
        "user_id": session["user_id"]
    }
    user = User.get_by_id(data)
    all_trips = Trip.all_trips_with_travellers()
    trip_count = Trip.total_trip_count()
    return render_template("dashboard.html", user=user, all_trips=all_trips, trip_count=trip_count)

# ========================
# Logout Route
# ========================


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
