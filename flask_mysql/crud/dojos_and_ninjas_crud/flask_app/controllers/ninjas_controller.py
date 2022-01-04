from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route("/ninjas")
def new_ninja_page():
    dojos = Dojo.get_all_dojos()
    return render_template("new_ninja.html", all_dojos=dojos)


@app.route("/save_ninja", methods=["POST"])
def save_ninja():
    data = {
        "dojo_id": request.form["dojo_id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
    }
    Ninja.save_ninja(data)
    return redirect("/")
