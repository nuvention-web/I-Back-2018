from models.notbought import NotBoughtModel
from models.card import CardModel
import sys


class NotBoughtController():

    @classmethod
    def make_notbought(cls, q1, q2, q3, name):
        try: 
            new_notbought = NotBoughtModel(name, q1, q2, q3)
        except:
            return "Error creating a notbought response", 500, None
        try:
            new_notbought.save_to_db()
        except:
            return "Error saving to db", 500, None

        
        result = []
        try:
            result = NotBoughtController.calculate_cards(q1, q2, q3)
        except:
            return "Error in forming response", 400, None

        return "", 201, result

    @classmethod
    def calculate_cards(cls, q1, q2, q3):
        result = []
        ### some logic to calculate the cards.
        result.append(CardModel.find_by_name(q1))
        result.append(CardModel.find_by_name(q2))
        result.append(CardModel.find_by_name(q3))
        
        return result









            




