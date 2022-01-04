from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user


class Dog:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.breed = data["breed"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.owner = []

    @staticmethod
    def validate_dog(form_data):
        is_valid = True

        if len(form_data["name"]) < 3:
            flash("Name must be at least 3 characters long!")
            is_valid = False
        if len(form_data["breed"]) < 2:
            flash("Breed must be at least 2 characters long!")
            is_valid = False
        if form_data["age"] == "":
            flash("Please enter a valid age!")
            is_valid = False
        elif int(form_data["age"]) < 2:
            flash("Dog must be at least 2 years old!")
            is_valid = False
        return is_valid

    @classmethod
    def save_dog(cls, data):
        query = "INSERT into dogs (name, age, breed, user_id, created_at, updated_at) VALUE (%(name)s, %(age)s, %(breed)s, %(user_id)s, NOW(), NOW());"
        results = connectToMySQL("dogs_show_schema").query_db(query, data)
        return results

    @classmethod
    def all_dogs_with_owners(cls):
        query = "Select * from dogs left join users on dogs.user_id = users.id;"
        results = connectToMySQL("dogs_show_schema").query_db(query)

        all_dogs = []

        for row in results:
            one_dog = cls(row)
            user_data = {
                "id": row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"],
            }
            one_dog.owner = user.User(user_data)
            all_dogs.append(one_dog)
        return all_dogs

    @classmethod
    def get_dog_with_owner(cls, data):
        query = "Select * from dogs left join users on dogs.user_id = users.id where dogs.id =%(dog_id)s;"
        results = connectToMySQL("dogs_show_schema").query_db(query, data)

        dog = cls(results[0])
        user_data = {
            "id": results[0]["users.id"],
            "first_name": results[0]["first_name"],
            "last_name": results[0]["last_name"],
            "email": results[0]["email"],
            "password": results[0]["password"],
            "created_at": results[0]["users.created_at"],
            "updated_at": results[0]["users.updated_at"],
        }
        dog.owner = user.User(user_data)
        return dog

    @classmethod
    def update_dog(cls, data):
        query = "Update dogs SET name = %(name)s, age = %(age)s, breed = %(breed)s, updated_at = NOW() where id = %(dog_id)s;"
        results = connectToMySQL("dogs_show_schema").query_db(query, data)
        return

    @classmethod
    def delete_dog(cls, data):
        query = "delete from dogs where id = %(dog_id)s;"
        results = connectToMySQL("dogs_show_schema").query_db(query, data)
        return
