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

    def test_card_post_get(self):

        # create card
        # make_card name, accord, image_lnk, video_lnk, start_time, description
        new_card = helper.make_card(self, 'name', 'accord', 'image', 'video', '0', 'desc')
        self.assertEqual(new_card.status_code, 201)
        new_card_get = helper.get_card(self, 'name')
        helper.print_error(new_card_get, 200)
        self.assertEqual(new_card_get.status_code, 200)
        new_card_data = json.loads(new_card_get.data.decode())
        self.assertEqual(new_card_data['response'][0]['name'], 'name')
        self.assertEqual(new_card_data['response'][0]['accord'], 'accord')

        new_card_get = helper.get_card(self, 'all')
        helper.print_error(new_card_get, 200)
        self.assertEqual(new_card_get.status_code, 200)
        new_card_data = json.loads(new_card_get.data.decode())
        self.assertEqual(new_card_data['response'][0]['name'], 'name')
        self.assertEqual(new_card_data['response'][0]['accord'], 'accord')

    def test_card_edit(self):
        # create card
        new_card = helper.make_card(self, 'name', 'accord', 'image', 'video', '0', 'desc')
        self.assertEqual(new_card.status_code, 201)
        new_card_get = helper.get_card(self, 'name')
        helper.print_error(new_card_get, 200)
        self.assertEqual(new_card_get.status_code, 200)
        new_card_data = json.loads(new_card_get.data.decode())
        self.assertEqual(new_card_data['response'][0]['name'], 'name')
        self.assertEqual(new_card_data['response'][0]['accord'], 'accord')

        # get card and check
        new_card_get = helper.get_card(self, 'all')
        helper.print_error(new_card_get, 200)
        self.assertEqual(new_card_get.status_code, 200)
        new_card_data = json.loads(new_card_get.data.decode())
        self.assertEqual(new_card_data['response'][0]['name'], 'name')
        self.assertEqual(new_card_data['response'][0]['accord'], 'accord')

        #edit card
        #edit_card = helper.edit_card(self, 'all

        

if __name__ == "__main__":
    unittest.main()
