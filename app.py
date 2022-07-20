from flask import Flask, render_template

# Instance of Flask
app = Flask(__name__)

# create a route decorator 
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user/<name>')
def user(name):
    return "Hello {}".format(name)
