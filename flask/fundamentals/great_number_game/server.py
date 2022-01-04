import random
from flask import Flask, render_template, redirect, session
from flask.globals import request
app = Flask(__name__)
app.secret_key = "yoyo"


@app.route("/")
def index():
    if "num" not in session:
        session["num"] = random.randint(1, 5)
    return render_template("index.html")


@app.route("/guess", methods=["POST"])
def guess():
    session["num"] = int(request.form["num"])
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
