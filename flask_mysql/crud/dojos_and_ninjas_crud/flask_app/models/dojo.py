from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja


class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.ninjas = []

    @classmethod
    def save(cls, data):
        query = "Insert into Dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * from dojos"
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query)

    @classmethod
    def delete_dojo(cls, data):
        query = "Delete from dojos where id = %(id)s;"
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "Select * from dojos left join ninjas on dojos.id=ninjas.dojo_id where dojos.id = %(dojo_id)s;"
        results = connectToMySQL(
            "dojos_and_ninjas_schema").query_db(query, data)

        print(results)
        dojo = cls(results[0])

        for data in results:
            ninja_data = {
                "id": data['ninjas.id'],
                "first_name": data['first_name'],
                "last_name": data['last_name'],
                "age": data['age'],
                "created_at": data['ninjas.created_at'],
                "updated_at": data['ninjas.updated_at'],
                "dojo_id": data['dojo_id'],
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))

        return dojo
