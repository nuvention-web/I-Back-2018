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
# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/special/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/special/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))


api.add_resource(Quiz, '/quiz')


if __name__ == '__main__':
    from db import db
    db.init_app(application)
    @application.before_first_request
    def create_tables():
        db.create_all()
    application.debug = True
    application.run()

