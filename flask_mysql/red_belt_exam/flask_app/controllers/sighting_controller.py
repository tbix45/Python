from re import S
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.sighting import Sighting


# =========================================
# ShOW New Sighting Page
# =========================================


@app.route("/sighting/new")
def new_sighting():
    if "user_id" not in session:
        flash("Please login or register!")
        return redirect("/")
    data = {
        "user_id": session["user_id"]
    }
    user = User.get_by_id(data)
    return render_template("new_sighting.html", user=user)

# =========================================
# Process New Sighting Form
# =========================================


@app.route("/save_sighting", methods=["POST"])
def save_sighting():
    if not Sighting.validate_sighting(request.form):
        return redirect("/sighting/new")
    data = {
        "location": request.form["location"],
        "what_happened": request.form["what_happened"],
        "date_of_sighting": request.form["date_of_sighting"],
        "numb_of_squatch": request.form["numb_of_squatch"],
        "user_id": request.form["user_id"]
    }
    Sighting.save_sighting(data)
    return redirect("/dashboard")

    # =========================================
# Show completed sighting page
# =========================================


@app.route("/sightings/<int:sighting_id>")
def show_sighting(sighting_id):
    if "user_id" not in session:
        flash("Please login or register!")
        return redirect("/")
    data = {
        "sighting_id": sighting_id
    }
    user_data = {
        "user_id": session['user_id']
    }
    user = User.get_by_id(user_data)
    sighting = Sighting.get_sighting_with_reporter(data)
    return render_template("show_sighting.html", sighting=sighting, user=user)
# =========================================
# Display Edit sighting page
# =========================================


@app.route("/edit/<int:sighting_id>")
def edit_recipe(sighting_id):
    if "user_id" not in session:
        flash("Please register or login!")
        return redirect("/")
    data = {
        "sighting_id": sighting_id
    }
    # user_data = {
    #     "id": session["user_id"]
    # }
    sighting = Sighting.get_sighting_with_reporter(data)
    # user = User.get_by_id(user_data)
    return render_template("edit_sighting.html", sighting=sighting)


# =========================================
# Process Edit Page
# =========================================
@app.route("/update_sighting/<int:sighting_id>", methods=["POST"])
def update_sighting(sighting_id):
    if "user_id" not in session:
        flash("Please register or login!")
        return redirect("/")
    if not Sighting.validate_sighting(request.form):
        return redirect(f"/edit/{sighting_id}")
    data = {
        "location": request.form["location"],
        "what_happened": request.form["what_happened"],
        "date_of_sighting": request.form["date_of_sighting"],
        "numb_of_squatch": request.form["numb_of_squatch"],
        "sighting_id": sighting_id
    }

    Sighting.update_sighting(data)
    return redirect("/dashboard")
# =========================================
# Delete sighting
# =========================================


@app.route("/delete/<int:sighting_id>")
def delete_sighting(sighting_id):
    data = {
        "sighting_id": sighting_id
    }
    Sighting.delete_sighting(data)
    return redirect("/dashboard")
