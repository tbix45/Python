from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

# =========SHOW DOJOS==============


@app.route("/")
def dashboard_dojos():
    dojos = Dojo.get_all_dojos()
    return render_template("dashboard_dojos.html", all_dojos=dojos)


@app.route("/dojos/<int:dojo_id>")
def show_1_dojo(dojo_id):
    data = {
        "dojo_id": dojo_id
    }
    one_dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template("dojos_show_1.html", one_dojo=one_dojo)
# ==================================
# ==========PROCESS==============


@app.route("/save_dojo", methods=["POST"])
def save_dojo():

    data = {
        "name": request.form["name"],
    }
    Dojo.save(data)
    return redirect("/")


@app.route("/delete_dojo/<int:id>")
def delete_dojo(id):
    data = {
        "id": id
    }
    Dojo.delete_dojo(data)
    return redirect("/")

# ==================================
