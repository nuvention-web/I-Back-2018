from flask import Flask
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


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    @app.before_first_request
    def create_tables():
        db.create_all()
    app.run(port=5000, debug=True)

