from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def home():
    dojos = Dojo.get_dojos()
    return render_template('index.html', dojos=dojos)

@app.route('/')
def reroute():
    return redirect('/dojos')