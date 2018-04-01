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

    def test_scent_profile_generation(self):

        # create scent_profile
        scent_profile_create = helper.make_scent_profile(self, 0, 1, 'Fresh', '', 'Light', 'aha', '', 0, "hah")
        self.assertEqual(scent_profile_create.status_code, 201)
        scent_profile_get = helper.get_scent_profile(self, '0', '1')
        scent_profile_data = json.loads(scent_profile_get.data.decode())
        self.assertEqual(scent_profile_get.status_code, 200)
        self.assertEqual(scent_profile_data['id'], 1)
        

    def test_scent_profile_update(self):
        # create scent_profile
        scent_profile_create = helper.make_scent_profile(self, 0, 1, 'Fresh', '', 'Light', 'aha', '', 0, "hah")
        self.assertEqual(scent_profile_create.status_code, 201)
        scent_profile_get = helper.get_scent_profile(self, '0', '1')
        scent_profile_data = json.loads(scent_profile_get.data.decode())
        self.assertEqual(scent_profile_get.status_code, 200)
        self.assertEqual(scent_profile_data['id'], 1)

        # update scent_profile
        scent_profile_update = helper.put_scent_profile(self, 0, 1, 'Fresh', '', 'Light', 'aha', '', 0, "abcd")
        self.assertEqual(scent_profile_update.status_code, 200)
        scent_profile_get = helper.get_scent_profile(self, '0', '1')
        scent_profile_data = json.loads(scent_profile_get.data.decode())
        self.assertEqual(scent_profile_get.status_code, 200)
        self.assertEqual(scent_profile_data['scent_description'], "abcd")
        

    

if __name__ == "__main__":
    unittest.main()
