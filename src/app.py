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

if __name__ == "__main__":
    # command line app execution ONLY
    # must set host ip address to make accessible outside of container
    # run in debug mode for live editting
    app.run(host='0.0.0.0', debug=True)
