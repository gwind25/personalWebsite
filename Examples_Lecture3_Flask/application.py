import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

# Example 1: Using a formatted string
# @app.route("/<string:name>")
# def hello(name):
#     return f"Hello, {name}!"

# Example 2: Render Template and include variables
# @app.route("/")
# def index():
#     headline = "Hello!"
#     return render_template("begin.html", headline=headline)
#
# @app.route("/bye")
# def bye():
#     headline = "Goodbye!"
#     return render_template("begin.html", headline=headline)

# Example 3: Ginja and if statements
# now.day returns the current date
#friday is equal to True if now.day equals 1.
# @app.route("/")
# def index():
#     now = datetime.datetime.now()
#     friday = now.day == 1
#     return render_template("index.html", friday=friday)

# Example 4: for loops, linking to another page/function
# Extending layout
# @app.route("/")
# def index():
#     names = ["Mark", "Simon", "Sam"]
#     return render_template("index.html", names=names)
#
# @app.route("/begin")
# def begin():
#     return render_template("begin.html")

# Example 5: forms
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/name", methods = ["POST"])
def name():
    name = request.form.get("name")
    return render_template("name.html", name=name)
