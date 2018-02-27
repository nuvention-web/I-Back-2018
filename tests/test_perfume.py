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
    
    # make request to new endline
    def make_scent_profile(self, q6, q7, tag1, tag2, sillage, image_lnk, sound_lnk):
        return self.app.post(
                '/scentprofile/0/0',
                data = dict(q6=q6, q7=q7, tag1=tag1, tag2=tag2, sillage=sillage, image_lnk=image_lnk, sound_lnk=sound_lnk),
                )
    def get_scent_profile(self, q6, q7):
        return self.app.get(
                '/scentprofile/' + q6 + '/' + q7
                )

    def make_perfume(self, name, designer, image_lnk, vid_lnk, scent_id):
        return self.app.post(
                '/perfume/hai',
                data = dict(name=name, designer=designer, image_lnk=image_lnk, vid_lnk=vid_lnk, scent_id=scent_id)
                )
    def get_perfume(self, name):
        return self.app.get(
                '/perfume/' + name
                )

    def quiz_req(self, q6, q7):
        return self.app.get(
                '/quiz/' + q6 + '/' + q7,
                )
                
 
    ###############
    #### tests ####
    ###############

    def test_perfume_generation(self):
        # create scent_profile
        scent_profile_create = self.make_scent_profile(0, 1, 'Fresh', '', 'Light', 'aha', '')
        self.assertEqual(scent_profile_create.status_code, 201)
        scent_profile_get = self.get_scent_profile('0', '1')
        scent_profile_data = json.loads(scent_profile_get.data.decode())
        self.assertEqual(scent_profile_data['response']['id'], 1)
        _id = scent_profile_data['response']['id']

        # make perfume
        valid_post = self.make_perfume('3', 'b', 'c', 'd', str(_id))
        self.assertEqual(valid_post.status_code, 201)

        # make bad perfume -wrong scent_id
        invalid_post = self.make_perfume('3', 'b', 'c', 'd', '8')
        invalid_post_data = json.loads(invalid_post.data.decode())
        self.assertEqual(invalid_post.status_code, 400)
        self.assertEqual(invalid_post_data['error_message'], 'Invalid scent_profile_id.')

        # get perfume
        valid_get = self.get_perfume('3')
        self.assertEqual(valid_get.status_code, 200)
        valid_get_data = json.loads(valid_get.data.decode())
        self.assertEqual(valid_get_data['response']['name'], '3')
        

    

if __name__ == "__main__":
    unittest.main()

