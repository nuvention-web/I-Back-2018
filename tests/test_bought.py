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
    # /bought

    def test_bought_delete(self):
        # create card, bought
        new_card = helper.make_card(self, 'name1', 'accord1', 'image1', 'vid1', 0, 'desc1')
        self.assertEqual(new_card.status_code, 201)
        new_card = helper.make_card(self, 'name2', 'accord2', 'image2', 'vid2', 0, 'desc2')
        self.assertEqual(new_card.status_code, 201)
        new_card = helper.make_card(self, 'name3', 'accord3', 'image3', 'vid3', 0, 'desc3')
        self.assertEqual(new_card.status_code, 201)
        new_bought = helper.make_bought(self, 'name1', 'name2', 'name3', 'san_email', 'san', 0)
        self.assertEqual(new_bought.status_code, 201)
        get_bought = helper.get_bought(self, '1')
        self.assertEqual(get_bought.status_code, 200)

        delete_bought = helper.delete_bought(self, '1')
        self.assertEqual(delete_bought.status_code, 200)
        get_bought = helper.get_bought(self, '1')
        self.assertEqual(get_bought.status_code, 400)


    def test_bought_post_get(self):
        # create card
        new_card = helper.make_card(self, 'name1', 'accord1', 'image1', 'vid1', 0, 'desc1')
        self.assertEqual(new_card.status_code, 201)
        new_card = helper.make_card(self, 'name2', 'accord2', 'image2', 'vid2', 0, 'desc2')
        self.assertEqual(new_card.status_code, 201)
        new_card = helper.make_card(self, 'name3', 'accord3', 'image3', 'vid3', 0, 'desc3')
        self.assertEqual(new_card.status_code, 201)

        ###### card prep complete, now checking bought
        # make_bought q1(card name), q2, q3, name 
        new_bought = helper.make_bought(self, 'name1', 'name2', 'name3', 'san_email', 'san', 0)
        helper.print_error(new_bought, 201)
        # check if the bought was made
        self.assertEqual(new_bought.status_code, 201)
    
        get_bought = helper.get_bought(self, 'all')
        helper.print_error(get_bought, 200)
        self.assertEqual(get_bought.status_code, 200)
        get_data = json.loads(get_bought.data.decode())
        self.assertEqual(get_data['response'][0]['email'], 'san_email')
    
        get_bought = helper.get_bought(self, '1')
        helper.print_error(get_bought, 200)
        self.assertEqual(get_bought.status_code, 200)
        get_data = json.loads(get_bought.data.decode())
        self.assertEqual(get_data['response'][0]['email'], 'san_email')

if __name__ == "__main__":
    unittest.main()
