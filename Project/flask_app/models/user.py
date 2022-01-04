import re
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.username = data["username"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validate_register(form_data):
        is_valid = True
        if len(form_data["username"]) < 4:
            flash("Username must be at least 4 characters long!")
            is_valid = False
        if len(form_data["first_name"]) < 2:
            flash("Username must be at least 2 characters long!")
            is_valid = False
        if len(form_data["last_name"]) < 2:
            flash("Username must be at least 2 characters long!")
            is_valid = False
        if not EMAIL_REGEX.match(form_data["email"]):
            flash("Must be a valid email format!")
            is_valid = False
        # elif User.get_by_email(form_data):
        #     flash("Email already in use")
        #     is_valid = False
        if len(form_data['password']) < 6:
            flash("Password must be at least 6 characters long!")
            is_valid = False
        if (form_data['password']) != (form_data["confirm_password"]):
            flash("Passwords must match!")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(validation_data):
        is_valid = True
        if not validation_data["user_in_db"]:
            flash("Invalid Email/Password")
            is_valid = False
        elif not bcrypt.check_password_hash(validation_data["user_in_db"].password, validation_data["password"]):
            flash("Invalid Email/Pasword")
            is_valid = False
        return is_valid

    @classmethod
    def save_user(cls, data):
        query = "INSERT into users (username, first_name, last_name, email, password, created_at, updated_at) VALUES (%(username)s,%(first_name)s,%(last_name)s,%(email)s,%(password)s, NOW(), NOW());"
        result = connectToMySQL("trips_tracker_schema").query_db(query, data)
        return result

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * from users where email = %(email)s;"
        result = connectToMySQL("trips_tracker_schema").query_db(query, data)
        # didnt find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * from users where id = %(user_id)s;"
        result = connectToMySQL("trips_tracker_schema").query_db(query, data)
        return cls(result[0])
