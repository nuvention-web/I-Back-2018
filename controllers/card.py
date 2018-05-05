from models.card import CardModel
import sys


class CardController():

    @classmethod
    def make_card(cls, name, accord, image_lnk, video_lnk, start_time, description):

        if CardModel.find_by_name(name):
            return "Card with that name already exists. To edit, use PUT not POST", 400, None

        try: 
            new_card = CardModel(name, accord, image_lnk, video_lnk, start_time, description)
        except:
            print("Error in creating new card!", file=sys.stderr)
            return "Error in creating new card.", 500, None
        try:
            new_card.save_to_db()
        except:
            print("Error in saving new card!", file=sys.stderr)
            return "Error in saving new card.", 500, None

        return "", 201, None

    @classmethod
    def get_card(cls, mode):
        result = []
        if mode == 'all':
            try: 
                result = CardModel.get_all()
            except: 
                return "Error getting all cards.", 500, None
        else:
            try: 
                result.append(CardModel.find_by_name(mode))
            except:
                return "Error getting specified card.", 500, None
        
        if result[0] is None:
            return "Empty result. the name must be EXACT", 400, None
        else:
            return "", 200, result

    @classmethod
    def delete_card(cls, name):
        wanted = CardModel.find_by_name(name)
        if not wanted:
            return "Card with that name doesn't exist", 400, None
        
        try:
            wanted.delete_from_db()
        except:
            return "Error deleting from db", 500, None

        return "", 200, None




            





