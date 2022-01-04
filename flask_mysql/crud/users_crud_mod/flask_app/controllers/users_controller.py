from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user import User


@app.route("/")
def index():
    return redirect("/users")


@app.route("/users")
def read_all():
    users = User.get_all()
    return render_template("index.html", all_users=users)


@app.route("/users/new")
def new_user():
    return render_template("new_user.html")


@app.route("/users/<int:id>/edit")
def edit_user(id):
    data = {
        "id": id
    }
    return render_template("edit_user.html", user=User.get_one(data))


@app.route("/users/<int:id>")
def show_user(id):
    data = {
        "id": id
    }
    user = User.get_one(data)
    return render_template("show_1_user.html", user=user)


@app.route("/update_submit_user", methods=["POST"])
def update():
    User.update(request.form)
    return redirect("/users")
# ===========creating/save user to DB=============================


@ app.route("/save_user", methods=["POST"])
def save_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    User.save(data)
    return redirect("/users")


@app.route("/users/<int:id>/destroy")
def delete_user(id):
    data = {
        "id": id
    }
    User.delete_user(data)
    return redirect("/users")
