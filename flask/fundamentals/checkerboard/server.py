from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", rows=8, columns=8, color_one="black", color_two="red")


@app.route("/<int:i>")
def user_rows(i):
    return render_template("index.html", rows=i, columns=8, color_one="black", color_two="red")


@app.route("/<int:i>/<int:x>")
def user_rows_cols(i, x):
    return render_template("index.html", rows=i, columns=x, color_one="black", color_two="red")


@app.route("/<int:i>/<int:x>/<string:color_one>/<string:color_two>")
def user_rows_cols_colors(i, x, color_one, color_two):
    return render_template("index.html", rows=i, columns=x, color_one=color_one, color_two=color_two)


if __name__ == "__main__":
    app.run(debug=True)
