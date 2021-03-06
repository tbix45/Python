# from flask_bcrypt import Bcrypt
import re  # the regex module
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app import app
bcrypt = Bcrypt(app)
# create a regular expression object that we'll use later
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# bcrypt = Bcrypt(app)     # we are creating an object called bcrypt,
# which is made by invoking the function Bcrypt with our app as an argument


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validate_user(user):
        is_valid = True  # we assume this is true
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters!")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters!")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Must be a valid email format!")
            is_valid = False
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(
            "users_login_reg_schema").query_db(query, user)
        if len(results) >= 1:
            flash("Email already taken.")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters!")
            is_valid = False
        if user['confirm_password'] != user["password"]:
            flash("Passwords must match!")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(data):
        is_valid = True
        if not data['user_in_db']:
            flash('Invalid Email/Password')
            is_valid = False
        elif not bcrypt.check_password_hash(data['user_in_db'].password, data['password']):
            # if we get False after checking the password
            flash("Invalid Email/Password")
            is_valid = False
        return is_valid

    @classmethod
    def save_user(cls, data):
        query = "INSERT into users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s,NOW(), NOW());"
        return connectToMySQL("users_login_reg_schema").query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = "select * from users where email = %(email)s;"
        result = connectToMySQL("users_login_reg_schema").query_db(query, data)
        # didnt find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_user_info(cls, data):
        query = "SELECT * from users where id = %(user_id)s;"
        result = connectToMySQL("users_login_reg_schema").query_db(query, data)
        return cls(result[0])
