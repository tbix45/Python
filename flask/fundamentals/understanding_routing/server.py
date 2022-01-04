from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World!"


@app.route("/dojo")
def dojo():
    return "Dojo!"


@app.route("/say/<string:name>")
def say_name(name):
    return f"Hi, {name}!"


@app.route("/repeat/<int:num>/<string:word>")
def repeat_word(num, word):
    return f"{num * word }"


if __name__ == "__main__":
    app.run(debug=True)
