from flask import Flask, render_template, redirect
# from werkzeug.utils import redirect
app = Flask(__name__)


@app.route("/")
def redirect_index():
    return redirect('/play')


@app.route("/play")
def index():
    return render_template('index.html', number=3, color="blue")


@app.route("/play/<int:x>")
def num_boxes(x):
    return render_template('index.html', number=x, color="blue")


@app.route("/play/<int:x>/<string:color>")
def num_boxes_color(x, color):
    return render_template("index.html", number=x, color=color)


if __name__ == "__main__":
    app.run(debug=True)
