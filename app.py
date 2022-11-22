import json
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)


class UserModel (db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    """Return the index."""
    return "Hello world. Remember to change this"


@app.route('/about')
def about():
    """Return the about page."""
    return "This is the about page"


@app.route('/contact')
def contact():
    """Return the contact page ."""
    return "This is the contact page"


@app.route('/user/<name>', methods=['GET', 'POST'])
def user(name):
    """Return or Add an user to the database"""
    if request.method == 'GET':
        user_sql = UserModel.query.filter_by(name=name).first()
        return json.dumps(user_sql.email)
    elif request.method == 'POST':
        email = request.form['email']
        user_model = UserModel(name=name, email=email)
        db.session.add(user_model)
        db.session.commit()
        return json.dumps('Hello {}! Your email is {}'.format(name, email))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
