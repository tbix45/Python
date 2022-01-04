from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
from flask_app.models.airport_codes import airports


class Trip:
    def __init__(self, data):
        self.id = data["id"]
        self.departure = data["departure"]
        self.arrival = data["arrival"]
        self.airline = data["airline"]
        self.date = data["date"]
        self.description = data["description"]
        self.seat_num = data["seat_num"]
        self.seat = data["seat"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.traveller = []

    @staticmethod
    def validate_trip(form_data):
        is_valid = True
        if form_data["departure"].upper() not in airports:
            flash("Departure must be a valid 3 letter airport code!")
            is_valid = False
        if form_data["arrival"].upper() not in airports:
            flash("Arrival must be a valid 3 letter airport code!")
            is_valid = False
        # if len(form_data["departure"]) != 3:
        #     flash("Departure must be a valid 3 letter airport code!")
        #     is_valid = False
        # if len(form_data["arrival"]) != 3:
        #     flash("Arrival must be a valid 3 letter airport code!")
        #     is_valid = False
        if len(form_data["airline"]) < 3:
            flash("Airline must be at least 3 characters long!")
            is_valid = False
        if len(form_data["description"]) < 3:
            flash("Description must be at least 3 characters long!")
            is_valid = False
        if (form_data["date"]) == "":
            flash("Please enter a date!")
            is_valid = False
        # if (form_data['seat_num']) == "":
        #     flash("Must pick a seat number!")
        #     is_valid = False
        # elif int(form_data['seat_num']) < 1:
        #     flash("Must be a valid seat number!")
        #     is_valid = False
        return is_valid

    @classmethod
    def save_trip(cls, data):
        query = "Insert into trips (departure, arrival, airline, date, description, seat_num, seat, user_id, created_at, updated_at) VALUES (upper(%(departure)s), upper(%(arrival)s), %(airline)s, %(date)s, %(description)s, %(seat_num)s, %(seat)s, %(user_id)s, NOW(), NOW());"
        result = connectToMySQL("trips_tracker_schema").query_db(query, data)
        return result

    @classmethod
    def all_trips_with_travellers(cls):
        query = "SELECT * from trips left join users on trips.user_id = users.id;"
        results = connectToMySQL("trips_tracker_schema").query_db(query)

        all_trips = []

        for row in results:
            one_trip = cls(row)
            user_data = {
                "id": row["users.id"],
                "username": row["username"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"],
            }
            one_trip.traveller = user.User(user_data)
            all_trips.append(one_trip)
        return all_trips

    @classmethod
    def get_trip_with_traveller(cls, data):
        query = "Select * from trips left join users on trips.user_id = users.id where trips.id = %(trip_id)s;"
        results = connectToMySQL("trips_tracker_schema").query_db(query, data)

        trip = cls(results[0])
        user_data = {
            "id": results[0]["users.id"],
            "username": results[0]["username"],
            "first_name": results[0]["first_name"],
            "last_name": results[0]["last_name"],
            "email": results[0]["email"],
            "password": results[0]["password"],
            "created_at": results[0]["users.created_at"],
            "updated_at": results[0]["users.updated_at"],
        }
        trip.traveller = user.User(user_data)
        return trip

    @classmethod
    def update_trip(cls, data):
        query = "UPDATE trips set departure = upper(%(departure)s), arrival = upper(%(arrival)s), airline = %(airline)s, description = %(description)s,date = %(date)s,seat_num = %(seat_num)s, seat = %(seat)s, updated_at = NOW() where id = %(trip_id)s;"
        results = connectToMySQL("trips_tracker_schema").query_db(query, data)
        return

    @classmethod
    def total_trip_count(cls):
        query = "SELECT count(id) as 'total' FROM trips;"
        result = connectToMySQL("trips_tracker_schema").query_db(query)
        return result[0]

    @classmethod
    def traveller_trip_count(cls, data):
        query = "Select count(*) as 'total' from trips where trips.user_id = %(user_id)s;"
        results = connectToMySQL("trips_tracker_schema").query_db(query, data)
        return results[0]

    @ classmethod
    def delete_trip(cls, data):
        query = "Delete from trips where id = %(trip_id)s;"
        result = connectToMySQL("trips_tracker_schema").query_db(query, data)
        return
