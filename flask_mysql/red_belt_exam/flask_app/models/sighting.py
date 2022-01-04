import re
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user


class Sighting:
    def __init__(self, data):
        self.id = data["id"]
        self.location = data["location"]
        self.what_happened = data["what_happened"]
        self.date_of_sighting = data["date_of_sighting"]
        self.numb_of_squatch = data["numb_of_squatch"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.reporter = []

    @staticmethod
    def validate_sighting(form_data):
        is_valid = True
        if len(form_data['location']) < 2:
            flash("Location must be at least 2 characters long!")
            is_valid = False
        if len(form_data['what_happened']) < 2:
            flash("What happened must be at least 2 characters long!")
            is_valid = False
        if form_data['date_of_sighting'] == "":
            flash("Please enter a date!")
            is_valid = False
        if (form_data['numb_of_squatch']) == "":
            flash("Must have seen at least one sasquatch!")
            is_valid = False
        elif int(form_data['numb_of_squatch']) < 1:
            flash("Must have seen at least one sasquatch!")
            is_valid = False
        return is_valid

    @classmethod
    def save_sighting(cls, data):
        query = "Insert into sightings (location, what_happened, date_of_sighting, numb_of_squatch, user_id, created_at, updated_at) VALUES (%(location)s, %(what_happened)s, %(date_of_sighting)s, %(numb_of_squatch)s, %(user_id)s, NOW(), NOW());"
        result = connectToMySQL("sightings_schema").query_db(query, data)
        return result

    @classmethod
    def all_sightings_with_reporters(cls):
        query = "SELECT * from sightings LEFT JOIN users on sightings.user_id = users.id;"
        results = connectToMySQL("sightings_schema").query_db(query)

        all_sightings = []

        for row in results:
            one_sighting = cls(row)
            user_data = {
                "id": row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"],
            }
            one_sighting.reporter = user.User(user_data)
            all_sightings.append(one_sighting)
        return all_sightings

    @classmethod
    def get_sighting_with_reporter(cls, data):
        query = "SELECT * from sightings left join users on sightings.user_id = users.id where sightings.id = %(sighting_id)s;"
        results = connectToMySQL("sightings_schema").query_db(query, data)

        sighting = cls(results[0])
        user_data = {
            "id": results[0]["users.id"],
            "first_name": results[0]["first_name"],
            "last_name": results[0]["last_name"],
            "email": results[0]["email"],
            "password": results[0]["password"],
            "created_at": results[0]["users.created_at"],
            "updated_at": results[0]["users.updated_at"],
        }
        sighting.reporter = user.User(user_data)
        return sighting

    @classmethod
    def update_sighting(cls, data):
        query = "UPDATE sightings set location = %(location)s, what_happened = %(what_happened)s, date_of_sighting = %(date_of_sighting)s, numb_of_squatch = %(numb_of_squatch)s, updated_at = NOW() where id = %(sighting_id)s;"
        results = connectToMySQL("sightings_schema").query_db(query, data)
        return

    @classmethod
    def delete_sighting(cls, data):
        query = "DELETE from sightings where id = %(sighting_id)s;"
        results = connectToMySQL("sightings_schema").query_db(query, data)
        return
