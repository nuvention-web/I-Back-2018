import os

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from resources.quiz import Quiz

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=2592000)
#app.secret_key = ''
api = Api(app)
CORS(app)

api.add_resource(Quiz, '/quiz')
@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    @app.before_first_request
    def create_tables():
        db.create_all()
    app.run()


