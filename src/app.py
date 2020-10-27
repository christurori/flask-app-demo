"""
author: Chris Turori
"""
# import packages
from flask import Flask, request, render_template

# create flask app
app = Flask(__name__)
app.debug = True

# create route
@app.route("/")
def home():
    return render_template("index.html")
