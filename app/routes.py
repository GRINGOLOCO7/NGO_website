from flask import Blueprint, render_template

# Define a Blueprint for the routes
main = Blueprint('main', __name__)

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/delivery")
def delivery():
    return render_template("delivery.html")

@main.route("/government")
def government():
    return render_template("government.html")

@main.route("/chat")
def chat():
    return render_template("chat.html")
