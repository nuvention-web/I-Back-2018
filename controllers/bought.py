from models.bought import BoughtModel
from models.card import CardModel


class BoughtController():

    @classmethod
    def make_bought(cls, q1, q2, q3, name):
        try: 
            new_bought = BoughtModel(name, email, q1, q2, q3)
        except:
            return "Error creating a bought response", 500, None
        try:
            new_bought.save_to_db()
        except:
            return "Error saving to db", 500, None

        return "", 201, None

    @classmethod
    def get_bought(cls):
        try:
            return "", 200, BoughtModel.get_all()
        except:
            return "Error retrieving bought", 500, None
        

        





