from flask import Flask

@app.route('/')
def index():
    return ("Hola mundo")


app = Flask(__name__)