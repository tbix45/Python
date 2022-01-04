from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

# =========================================
# ShOW New Recipe Page
# =========================================


@app.route("/recipes/new")
def new_recipe():
    if "user_id" not in session:
        flash("Please login or register!")
        return redirect("/")
    data = {
        "user_id": session["user_id"]
    }
    user = User.get_by_id(data)
    return render_template("new_recipe.html", user=user)
    # =========================================
# Show completed recipe page
# =========================================


@app.route("/recipes/<int:recipe_id>")
def show_recipe(recipe_id):
    if "user_id" not in session:
        flash("Please login or register!")
        return redirect("/")
    data = {
        "recipe_id": recipe_id
    }
    user_data = {
        "user_id": session['user_id']
    }
    user = User.get_by_id(user_data)
    recipe = Recipe.get_recipe_with_maker(data)
    return render_template("show_recipe.html", recipe=recipe, user=user)
    # =========================================
    # Process Recipe Form
    # =========================================


@app.route("/save_recipe", methods=["POST"])
def save_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect("/recipes/new")
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "date_made_on": request.form["date_made_on"],
        "under_30_min": request.form["under_30_min"],
        "user_id": request.form["user_id"]
    }
    Recipe.save_recipe(data)
    return redirect("/dashboard")
# =========================================
# Display Edit recipe page
# =========================================


@app.route("/edit/<int:recipe_id>")
def edit_recipe(recipe_id):
    if "user_id" not in session:
        flash("Please register or login!")
        return redirect("/")

    data = {
        "recipe_id": recipe_id
    }
    # user_data = {
    #     "id": session["user_id"]
    # }
    recipe = Recipe.get_recipe_with_maker(data)
    # user = User.get_by_id(user_data)
    return render_template("edit_recipe.html", recipe=recipe)

# =========================================
# Process Edit recipe page/form
# =========================================


@app.route("/update_recipe/<int:recipe_id>", methods=["POST"])
def update_recipe(recipe_id):
    if "user_id" not in session:
        flash("Please register or login!")
        return redirect("/")
    if not Recipe.validate_recipe(request.form):
        return redirect(f"/edit/{recipe_id}")
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "date_made_on": request.form["date_made_on"],
        "under_30_min": request.form["under_30_min"],
        "recipe_id": recipe_id
    }
    Recipe.update_recipe(data)
    return redirect("/dashboard")


# =========================================
# Delete recipe
# =========================================


@app.route("/delete/<int:recipe_id>")
def delete_recipe(recipe_id):
    data = {
        "recipe_id": recipe_id
    }
    Recipe.delete_recipe(data)
    return redirect("/dashboard")
