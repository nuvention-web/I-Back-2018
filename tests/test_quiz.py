import os, sys
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
basedir = os.path.abspath(os.path.dirname(__file__))
from app import app
from db import db
import json
from datetime import datetime, timedelta
from freezegun import freeze_time
 
TEST_DB = 'test.db'
 
class BasicTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.init_app(app)
        db.drop_all(app=app)
        db.create_all(app=app)
 
 
    # executed after each test
    def tearDown(self):
        pass

    ########################
    #### helper methods ####
    ########################
    
    def go_quiz(self, Q6, Q7):
        return self.app.post(
                '/quiz',
                data=dict(Q6=Q6, Q7=Q7),
                )
    
    # make request to new endline
    def make_profile(self, Q6, Q7, card, sillage, name, designer, card_image_link, perfume_image_link, buy_link, sound_link):
        return self.app.post(
                '/'
            )
 
    ###############
    #### tests ####
    ###############

    def test_valid_generate_profile(self):
        valid_response = self.make_profile()
        self.assertEqual(valid_response.status_code, 201)

    def test_valid_quiz(self):
        valid_response = self.go_quiz(0, 0)
        self.assertEqual(valid_response.status_code, 200)
        
        

    

if __name__ == "__main__":
    unittest.main()

