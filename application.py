from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from resources.quiz import Quiz

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=2592000)
#app.secret_key = ''
api = Api(application)
#CORS(app)

api.add_resource(Quiz, '/quiz')


if __name__ == '__main__':
    from db import db
    db.init_app(application)
    @application.before_first_request
    def create_tables():
        db.create_all()
    application.run(port=5000, debug=True)

