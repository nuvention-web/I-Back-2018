import os, sys
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
basedir = os.path.abspath(os.path.dirname(__file__))
from app import app
from db import db
import json
from datetime import datetime, timedelta
from freezegun import freeze_time

from helper_tests import helper
 
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
                

    ###############
    #### tests ####
    ###############

    def test_response(self):
        # create scent_profile
        scent_profile_create = helper.make_scent_profile(self, 0, 1, 'Fresh', '', 'Light', 'aha', '', 0, "hah")
        self.assertEqual(scent_profile_create.status_code, 201)
        scent_profile_get = helper.get_scent_profile(self, '0', '1')
        scent_profile_data = json.loads(scent_profile_get.data.decode())
        self.assertEqual(scent_profile_data['id'], 1)
        _id = scent_profile_data['id']

        # make perfume
        valid_post = helper.make_perfume(self, '3', 'b', 'c', 'd', str(_id))
        self.assertEqual(valid_post.status_code, 201)

        # get perfume
        valid_get = helper.get_perfume(self, '3')
        self.assertEqual(valid_get.status_code, 200)
        valid_get_data = json.loads(valid_get.data.decode())
        self.assertEqual(valid_get_data['name'], '3')
        perfume_id = valid_get_data['id']

        # submit a quiz for that perfume
        quiz = helper.quiz_req(self, '0', '1')
        self.assertEqual(quiz.status_code, 200)
        quiz_data = json.loads(quiz.data.decode())
        self.assertEqual(quiz_data['perfumes'][0]['name'], '3')

        # see if the response got logged
        response = helper.get_response(self, '4')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['responses'][0]['perfume_id'], perfume_id)


        
    

if __name__ == "__main__":
    unittest.main()
