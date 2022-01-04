from flask_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

# ==========ADDS TO DB ==================
    @classmethod
    def save(cls, data):
        query = "Insert into users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"

        return connectToMySQL("users_schema").query_db(query, data)

# =============DISPLAY USERS ON PAGE =============
    @classmethod
    def get_all(cls):
        query = "Select * from users;"
        results = connectToMySQL("users_schema").query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_one(cls, data):
        query = "Select * from users where id = %(id)s;"
        result = connectToMySQL("users_schema").query_db(query, data)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query, data)

    @classmethod
    def delete_user(cls, data):
        query = "Delete from users where id = %(id)s;"
        return connectToMySQL("users_schema").query_db(query, data)
