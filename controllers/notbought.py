from models.notbought import NotBoughtModel
from models.card import CardModel
import sys


class NotBoughtController():

    @classmethod
    def make_notbought(cls, name, quiz_id, q1, q2, q3):
        try: 
            new_notbought = NotBoughtModel(name, quiz_id, q1, q2, q3)
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

    @classmethod
    def get_notbought(cls, mode):
        if mode == 'all':
            try:
                return "", 200, NotBoughtModel.get_all()
            except:
                return "Error retrieving all from db", 500, None
        elif mode.isnumeric():
            try:
                wanted = NotBoughtModel.find_by_id(int(mode))
                if wanted is None:
                    return "Desired Notbought object with the id doesn't exist", 400, None
                result = []
                result.append(wanted)
                return "", 200, result
            except:
                return "Error getting one from db", 500, None
        else:
            return "Invalid mode", 400, None
        
        
    
    @classmethod
    def delete_notbought(cls, _id):
        wanted = NotBoughtModel.find_by_id(int(_id))
        if wanted is None:
            return "Notbought object exists with that id"
        try:
            wanted.delete_from_db()
        except:
            return "Error deleting object from db", 500, None
                
        return "", 200, None


