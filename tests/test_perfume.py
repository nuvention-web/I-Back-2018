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

    def test_perfume_generation(self):
        # create scent_profile
        scent_profile_create = helper.make_scent_profile(self, 0, 1, 'Fresh', '', 'Light', 'aha', '', 0, 'hah')
        self.assertEqual(scent_profile_create.status_code, 201)
        scent_profile_get = helper.get_scent_profile(self, '0', '1')
        scent_profile_data = json.loads(scent_profile_get.data.decode())
        self.assertEqual(scent_profile_data['id'], 1)
        _id = scent_profile_data['id']

        # make perfume
        valid_post = helper.make_perfume(self, '3', 'b', 'c', 'd', str(_id))
        if valid_post.status_code is not 201:
            post_data = json.loads(valid_post.data.decode())
            print(post_data)
        self.assertEqual(valid_post.status_code, 201)

        # make bad perfume -wrong scent_profile_id
        invalid_post = helper.make_perfume(self, '3', 'b', 'c', 'd', '8')
        invalid_post_data = json.loads(invalid_post.data.decode())
        self.assertEqual(invalid_post.status_code, 400)
        self.assertEqual(invalid_post_data['error_message'], 'Invalid scent_profile_id.')

        # get perfume
        valid_get = helper.get_perfume(self, '3')
        self.assertEqual(valid_get.status_code, 200)
        valid_get_data = json.loads(valid_get.data.decode())
        self.assertEqual(valid_get_data['name'], '3')
        
        
    def test_perfume_update(self):
        # create scent_profile
        scent_profile_create = helper.make_scent_profile(self, 0, 1, 'Fresh', '', 'Light', 'aha', '', 0, 'hah')
        self.assertEqual(scent_profile_create.status_code, 201)
        scent_profile_get = helper.get_scent_profile(self, '0', '1')
        scent_profile_data = json.loads(scent_profile_get.data.decode())
        self.assertEqual(scent_profile_data['id'], 1)
        _id = scent_profile_data['id']

        # make perfume
        valid_post = helper.make_perfume(self, '3', 'b', 'c', 'd', str(_id))
        if valid_post.status_code is not 201:
            post_data = json.loads(valid_post.data.decode())
            print(post_data)
        self.assertEqual(valid_post.status_code, 201)

        # put perfume
        valid_put = helper.put_perfume(self, '3', 'b', 'd', 'd', str(_id))
        if valid_put.status_code is not 200:
            put_data = json.loads(valid_post.data.decode())
            print(put_data)
        self.assertEqual(valid_put.status_code, 200)

        # get perfume
        valid_get = helper.get_perfume(self, '3')
        self.assertEqual(valid_get.status_code, 200)
        valid_get_data = json.loads(valid_get.data.decode())
        self.assertEqual(valid_get_data['image_lnk'], 'd')


if __name__ == "__main__":
    unittest.main()
