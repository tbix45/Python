from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect("/show")


# adding this method
@app.route("/show")
def show_user():
    return render_template('show.html', name=session['username'], email=session['useremail'])


if __name__ == "__main__":
    app.run(debug=True)
