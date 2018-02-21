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
    
    def go_quiz(self, ans1, ans2, ans3, ans4):
        return self.app.post(
                '/quiz',
                data=dict(ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4),
                )
 
    ###############
    #### tests ####
    ###############

    def test_valid_quiz(self):
        valid_response = self.go_quiz(0, 0, 0, 0)
        self.assertEqual(valid_response.status_code, 200)
        valid_response = self.go_quiz(0, 0, 0, 1)
        self.assertEqual(valid_response.status_code, 200)
        valid_response = self.go_quiz(0, 0, 1, 0)
        self.assertEqual(valid_response.status_code, 200)
        valid_response = self.go_quiz(0, 0, 1, 1)
        self.assertEqual(valid_response.status_code, 200)
        valid_response = self.go_quiz(0, 1, 0, 0)
        self.assertEqual(valid_response.status_code, 200)
        valid_response = self.go_quiz(0, 1, 0, 1)
        self.assertEqual(valid_response.status_code, 200)
        valid_response = self.go_quiz(0, 1, 1, 0)
        self.assertEqual(valid_response.status_code, 200)
        valid_response = self.go_quiz(0, 1, 1, 1)
        self.assertEqual(valid_response.status_code, 200)
        valid_response = self.go_quiz(1, 0, 0, 0)
        self.assertEqual(valid_response.status_code, 200)
        valid_response = self.go_quiz(1, 0, 0, 1)
        self.assertEqual(valid_response.status_code, 200)
        valid_response = self.go_quiz(1, 0, 1, 0)
        self.assertEqual(valid_response.status_code, 200)
        valid_response = self.go_quiz(1, 0, 1, 1)
        self.assertEqual(valid_response.status_code, 200)
        valid_response = self.go_quiz(1, 1, 0, 0)
        self.assertEqual(valid_response.status_code, 200)
        valid_response = self.go_quiz(1, 1, 0, 1)
        self.assertEqual(valid_response.status_code, 200)
        valid_response = self.go_quiz(1, 1, 1, 0)
        self.assertEqual(valid_response.status_code, 200)
        valid_response = self.go_quiz(1, 1, 1, 1)
        self.assertEqual(valid_response.status_code, 200)

if __name__ == "__main__":
    unittest.main()

