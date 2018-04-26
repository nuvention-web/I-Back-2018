import os

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from resources.card import Card
from resources.notbought import NotBought

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=2592000)
api = Api(app)
CORS(app, resources={r"/*": {"origins": "http://perffronttwo.s3-website-us-east-1.amazonaws.com"}})
#CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

api.add_resource(Card, '/card/<string:mode>')
api.add_resource(NotBought, '/notbought')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    @app.before_first_request
    def create_tables():
        db.create_all()
    app.run()


