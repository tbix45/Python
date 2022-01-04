from user import User
from flask import Flask, render_template, redirect, session
from flask.globals import request
app = Flask(__name__)


@app.route("/")
def index():
    return redirect("/users")


@app.route("/users")
def read_all():
    users = User.get_all()
    return render_template("index.html", all_users=users)


@app.route("/users/new")
def new_user_index():
    return render_template("create.html")


@app.route("/create_user", methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.save(data)

    return redirect("/users")


if __name__ == "__main__":
    app.run(debug=True)
