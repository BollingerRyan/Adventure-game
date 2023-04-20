from flask import render_template,redirect,request,session,flash,send_from_directory
from flask_app.controllers import map_controller
from flask_app import app


@app.route('/')
def show_home_page():
    map_filename = map_controller.generate_map()
    return render_template('game.html', map_filename=map_filename)