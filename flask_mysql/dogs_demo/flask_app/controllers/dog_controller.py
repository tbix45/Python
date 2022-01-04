from flask_app import app
from flask import render_template, redirect, request, session, flash
import flask_app
from flask_app.models.dog import Dog
from flask_app.models.user import User

# ====================================
# Create Dog Routes
# ======================================


@app.route("/new_dog")
def new_dog():
    if "user_id" not in session:
        flash("Please register or login!")
        return redirect("/")
    data = {
        "user_id": session["user_id"]
    }
    user = User.get_by_id(data)
    return render_template("new_dog.html", user=user)


@app.route("/create_dog", methods=["POST"])
def create_dog():
    if not Dog.validate_dog(request.form):
        return redirect("/new_dog")

    data = {
        "name": request.form["name"],
        "breed": request.form["breed"],
        "age": request.form["age"],
        "user_id": request.form["user_id"]
    }
    Dog.save_dog(data)
    return redirect("/dashboard")


# =====================================
# show dog route
@app.route("/show/<int:dog_id>")
def show_dog(dog_id):
    if "user_id" not in session:
        flash("Please login or register!")
        return redirect("/")
    data = {
        "dog_id": dog_id
    }
    dog = Dog.get_dog_with_owner(data)
    return render_template("show_dog.html", dog=dog)


# == == == == == == == == == == == == == == == == ==
# Edit dog route
@app.route("/edit/<int:dog_id>")
def edit_dog(dog_id):
    if "user_id" not in session:
        flash("Please register or login!")
        return redirect("/")
    data = {
        "dog_id": dog_id
    }
    dog = Dog.get_dog_with_owner(data)
    return render_template("/edit_dog.html", dog=dog)


@app.route("/update/<int:dog_id>", methods=["POST"])
def update_dog(dog_id):
    if not Dog.validate_dog(request.form):
        return redirect(f"/edit/{dog_id}")

    data = {
        "name": request.form['name'],
        "age": request.form['age'],
        "breed": request.form['breed'],
        "dog_id": dog_id
    }
    Dog.update_dog(data)
    return redirect("/dashboard")


# ===============================
# DELETE
@app.route("/delete/<int:dog_id>")
def delete_dog(dog_id):

    data = {
        "dog_id": dog_id
    }
    Dog.delete_dog(data)
    return redirect("/dashboard")
