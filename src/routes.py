from flask import render_template, request, jsonify

from src import app

@app.route("/")
def index():
    return render_template("index.html")
