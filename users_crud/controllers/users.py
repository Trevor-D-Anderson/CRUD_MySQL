from users_crud import app
from flask import render_template, redirect, session, request, flash

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