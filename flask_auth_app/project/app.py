from flask import Flask
from models import db, login

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///<my_flask>.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


login.init_app(app)
login.login_view = 'login'

app.run(host='localhost', port=5000)
