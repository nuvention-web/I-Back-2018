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
    # /notbought

    def test_notbought_post_get(self):

        # create card
        new_card = helper.make_card(self, 'name1', 'accord1', 'image1', 'vid1', 0, 'desc1')
        self.assertEqual(new_card.status_code, 201)
        new_card = helper.make_card(self, 'name2', 'accord2', 'image2', 'vid2', 0, 'desc2')
        self.assertEqual(new_card.status_code, 201)
        new_card = helper.make_card(self, 'name3', 'accord3', 'image3', 'vid3', 0, 'desc3')
        self.assertEqual(new_card.status_code, 201)

        ###### card prep complete, now checking notbought
        # make_notbought q1(card name), q2, q3, name 
        new_notbought = helper.make_notbought(self, 'name1', 'name2', 'name3', 'san')
        helper.print_error(new_notbought, 201)
        # check if the card arrives
        resp_data = json.loads(new_notbought.data.decode())
        self.assertEqual(resp_data['response']['Cards'][0]['name'], 'name1')
        self.assertEqual(resp_data['response']['Cards'][1]['name'], 'name2')
        self.assertEqual(resp_data['response']['Cards'][2]['name'], 'name3')
        # get all
        get_notbought = helper.get_notbought(self, 'all')
        helper.print_error(get_notbought, 200)
        get_data = json.loads(get_notbought.data.decode())
        self.assertEqual(get_data['response'][0]['name'], 'san')
        # get by id
        get_notbought = helper.get_notbought(self, '1')
        helper.print_error(get_notbought, 200)
        get_data = json.loads(get_notbought.data.decode())
        self.assertEqual(get_data['response'][0]['name'], 'san')
    

if __name__ == "__main__":
    unittest.main()
