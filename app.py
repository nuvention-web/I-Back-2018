import os

from db import db
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from resources.card import Card
from resources.notbought import NotBought
from resources.bought import Bought

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=2592000)
api = Api(app)
migrate = Migrate(app, db)
#CORS(app, resources={r"/*": {"origins": "http://survey.tryperf.com.s3-website-us-east-1.amazonaws.com"}})
CORS(app, resources={r"/*": {"origins": "http://survey.tryperf.com"}})
#CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

api.add_resource(Card, '/card/<string:mode>')
api.add_resource(NotBought, '/notbought/<string:mode>')
api.add_resource(Bought, '/bought/<string:mode>')

if __name__ == '__main__':
    db.init_app(app)
    @app.before_first_request
    def create_tables():
        db.create_all()
    app.run()


