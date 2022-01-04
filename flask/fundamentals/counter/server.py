from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = "yoyo"


@app.route("/")
def index():

    if "count" not in session:
        session["count"] = 1
    else:
        session['count'] += 1
    count = session['count']

    return render_template("index.html", count=count)


@app.route("/2")
def count_2():

    if "count" not in session:
        session["count"] = 1
    else:
        session['count'] += 2
    count = session['count']

    return render_template("index.html", count=count)


@app.route("/destroy_session")
def destroy_session():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
