from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/dojos')
def home():
    dojos = Dojo.get_dojos()
    return render_template('index.html', dojos=dojos)

@app.route("/create_dojo", methods=["POST"])
def create_users():
    data = {
        "name": request.form['name']
    }
    Dojo.create_dojo(data)
    return redirect("/dojos")

@app.route("/dojos/<id>")
def show_dojo(id):
    dojo_id = {'id': id}
    ninjas = Ninja.get_ninjas(dojo_id)
    return render_template("dojo.html", ninjas=ninjas)

@app.route("/add_ninja")
def add_ninja():
    dojos = Dojo.get_dojos()
    return render_template('ninja.html', dojos=dojos)

@app.route("/new_ninja", methods=['POST'])
def new_ninja():
    id = request.form['dojo']
    data = {
    "first_name": request.form['first_name'],
    "last_name": request.form['last_name'],
    "age": request.form['age'],
    "dojo_id": request.form['dojo']
    }
    Ninja.create_ninja(data)
    return redirect(f"/dojos/{id}")

@app.route('/')
def reroute():
    return redirect('/dojos')