from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return redirect("/all_users")

@app.route("/create_user", methods=["POST"])
def create_users():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    User.create_user(data)
    return redirect("/all_users")

@app.route("/new_user")
def new_user():
    return render_template("new_user.html")

@app.route("/delete/<id>")
def delete_user(id):
    id = {"id": id}
    User.delete_user(id)
    return redirect("/all_users")

@app.route("/users/<id>")
def show_user(id):
    id = {"id": id}
    users = User.show_user(id)
    return render_template("show_user.html", users=users)

@app.route("/users/<id>/edit")
def edit_users(id):
    id_num = {"id": id}
    users = User.show_user(id_num)
    return render_template("edit_user.html",users=users)

@app.route("/users/<id>/editing", methods=["POST"])
def editing_users(id):
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "id": id
    }
    User.edit_user(data)
    return redirect(f"/users/{id}")

@app.route("/all_users")
def all_users():
    users = User.get_all()
    return render_template("/all_users.html", users=users)
