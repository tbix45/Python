import re
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user


class Recipe:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.date_made_on = data["date_made_on"]
        self.under_30_min = data["under_30_min"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.maker = []

    @staticmethod
    def validate_recipe(form_data):
        is_valid = True
        if len(form_data['name']) < 3:
            flash("Name must be at least 3 characters long!")
            is_valid = False
        if len(form_data['description']) < 3:
            flash("Description must be at least 3 characters long!")
            is_valid = False
        if len(form_data['instructions']) < 3:
            flash("Instructions must be at least 3 characters long!")
            is_valid = False
        if form_data['date_made_on'] == "":
            is_valid = False
            flash("Please enter a date")

        return is_valid

    @classmethod
    def save_recipe(cls, data):
        query = "Insert into recipes (name, description, instructions, date_made_on, under_30_min, user_id, created_at, updated_at) VALUES (%(name)s,%(description)s, %(instructions)s,%(date_made_on)s,%(under_30_min)s,%(user_id)s, NOW(), NOW());"
        result = connectToMySQL("recipes_schema").query_db(query, data)
        return result

    @classmethod
    def all_recipes_with_makers(cls):
        query = "SELECT * from recipes LEFT JOIN users on recipes.user_id = users.id;"
        results = connectToMySQL("recipes_schema").query_db(query)

        all_recipes = []

        for row in results:
            one_recipe = cls(row)
            user_data = {
                "id": row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"],
            }
            one_recipe.maker = user.User(user_data)
            all_recipes.append(one_recipe)
        return all_recipes

    @classmethod
    def get_recipe_with_maker(cls, data):
        query = "SELECT * from recipes left join users on recipes.user_id = users.id where recipes.id = %(recipe_id)s;"
        results = connectToMySQL("recipes_schema").query_db(query, data)

        recipe = cls(results[0])
        user_data = {
            "id": results[0]["users.id"],
            "first_name": results[0]["first_name"],
            "last_name": results[0]["last_name"],
            "email": results[0]["email"],
            "password": results[0]["password"],
            "created_at": results[0]["users.created_at"],
            "updated_at": results[0]["users.updated_at"],
        }
        recipe.maker = user.User(user_data)
        return recipe

    @classmethod
    def update_recipe(cls, data):
        query = "Update recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made_on = %(date_made_on)s,under_30_min = %(under_30_min)s, updated_at = NOW() where id = %(recipe_id)s;"
        results = connectToMySQL("recipes_schema").query_db(query, data)
        return

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE from recipes where id = %(recipe_id)s;"
        results = connectToMySQL("recipes_schema").query_db(query, data)
        return
