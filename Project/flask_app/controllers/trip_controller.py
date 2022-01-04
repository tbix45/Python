from flask.templating import render_template_string
from flask_app import app
from flask import redirect, render_template, request, session, flash
from flask_app.models.user import User
from flask_app.models.trip import Trip

# ========================
# Show New Trip page
# ========================


@app.route("/new_trip")
def new_trip():
    if "user_id" not in session:
        flash("Please login or register!")
    data = {
        "user_id": session["user_id"]
    }
    user = User.get_by_id(data)
    return render_template("new_trip.html", user=user)

# ========================
# Process/save New Trip page
# ========================


@app.route("/save_trip", methods=["POST"])
def save_trip():
    if request.form["seat_num"] == "":
        seat_num = 0
    else:
        seat_num = request.form["seat_num"]
    if not Trip.validate_trip(request.form):
        return redirect("/new_trip")
    data = {
        "departure": request.form["departure"].upper(),
        "arrival": request.form["arrival"],
        "airline": request.form["airline"].title(),
        "date": request.form["date"],
        "description": request.form["description"],
        "seat_num": int(seat_num),
        "seat": request.form["seat"].title(),
        "user_id": request.form["user_id"],
    }
    Trip.save_trip(data)
    return redirect("/my_trips")

# ========================
# Show user_trip_dashboard page
# ========================


@app.route("/my_trips")
def user_trip_dashboard():
    if "user_id" not in session:
        flash("Please login or register!")
    data = {
        "user_id": session["user_id"]
    }
    user = User.get_by_id(data)
    all_trips = Trip.all_trips_with_travellers()
    trip_count = Trip.traveller_trip_count(data)
    return render_template("my_trips.html", user=user, all_trips=all_trips, trip_count=trip_count)


# ========================
# Show completed trip page (VIEW)
# ========================
@app.route("/view/<int:trip_id>")
def view_trip(trip_id):
    if "user_id" not in session:
        flash("Please login or register!")
        return redirect("/")
    data = {
        "trip_id": trip_id
    }
    user_data = {
        "user_id": session['user_id']
    }
    user = User.get_by_id(user_data)
    trip = Trip.get_trip_with_traveller(data)
    return render_template("view_trip.html", trip=trip, user=user)

# ========================
# Show edit trip page
# ========================


@app.route("/edit/<int:trip_id>")
def edit_trip(trip_id):
    if "user_id" not in session:
        flash("Please register or login!")
        return redirect("/")
    data = {
        "trip_id": trip_id,
    }
    trip = Trip.get_trip_with_traveller(data)
    return render_template("edit_trip.html", trip=trip)

# ========================
# Process edit trip page
# ========================


@app.route("/update_trip/<int:trip_id>", methods=["POST"])
def update_trip(trip_id):
    if "user_id" not in session:
        flash("Please register or login!")
        return redirect("/")
    if not Trip.validate_trip(request.form):
        return redirect(f"/edit/{trip_id}")
    data = {
        "departure": request.form["departure"],
        "arrival": request.form["arrival"],
        "airline": request.form["airline"],
        "description": request.form["description"],
        "date": request.form["date"],
        "seat_num": request.form["seat_num"],
        "seat": request.form["seat"],
        "trip_id": trip_id
    }
    Trip.update_trip(data)
    return redirect("/my_trips")


# ========================
# Show airport ID API info page
# ========================


@app.route("/view_airport_info/<string:trip_departure>")
def view_airport_api(trip_departure):
    data = {
        "trip_departure": trip_departure
    }

    return render_template("airport_api.html", data=data)

# ========================
# Show weather page
# ========================


@app.route("/weather")
def view_weather():
    return render_template("weather.html")
# ========================
# Delete trip
# ========================


@app.route("/delete/<int:trip_id>")
def delete_trip(trip_id):
    data = {
        "trip_id": trip_id
    }
    Trip.delete_trip(data)
    return redirect("/my_trips")
