from flask import Flask, render_template, redirect, session, flash
from flask.globals import request
app = Flask(__name__)
app.secret_key = "yoyoy"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create", methods=["POST"])
def create():
    session["name"] = request.form["name"]
    session["gender"] = request.form["gender"]
    session["dojo_location"] = request.form["dojo_location"]
    session["favorite_language"] = request.form["favorite_language"]
    session["comments"] = request.form["comments"]
    return redirect("/results")


@app.route("/results")
def results():

    return render_template("results.html", name=session["name"], dojo_location=session["dojo_location"], favorite_lang=session["favorite_language"], comments=session["comments"], gender=session["gender"])


if __name__ == "__main__":
    app.run(debug=True)
