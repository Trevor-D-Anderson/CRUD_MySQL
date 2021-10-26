from flask import Flask, render_template, redirect, request
from user import User

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_user", methods=["POST"])
def create_users():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    User.create_user(data)
    return redirect("/all_users")

@app.route("/all_users")
def all_users():
    users = User.get_all()
    return render_template("/all_users.html", users=users)

@app.route("/home")
def home():
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)