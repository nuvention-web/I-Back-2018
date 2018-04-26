from models.Card import CardModel
import sys


class CardController():

    @classmethod
    def make_card(cls, name, accord, image_lnk, video_lnk, start_time, description):
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
        elif mode in cards:
            try: 
                result = CardModel.find_by_name(mode)
            except
                return "Error getting specified card.", 500, None
        
        if not result:
            return "Empty result. the name must be EXACT", 400, None
        else:
            return "", 200, result





            





