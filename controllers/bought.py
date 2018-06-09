from models.bought import BoughtModel

class BoughtController():

    @classmethod
    def make_bought(cls, name, email, quiz_id, q1, q2, q3):
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
    def get_bought(cls, mode):
        if mode == 'all':
            try:
                return "", 200, BoughtModel.get_all()
            except:
                return "Error retrieving all bought", 500, None
        elif mode.isnumeric():
            try:
                wanted = BoughtModel.find_by_id(int(mode))
                if wanted is None:
                    return "Desired Bought object with the id doesn't exist", 400, None
                result = []
                result.append(wanted)
                return "", 200, result
            except:
                return "Error retrieving bought by id", 500, None

        
    @classmethod
    def delete_bought(cls, _id):
        wanted = BoughtModel.find_by_id(int(_id))
        if wanted is None:
            return "Object trying to delete doesn't exist in db", 400, None
        
        try:
            wanted.delete_from_db()
        except:
            return "Error in deleting Bought object in db", 400, None
        
        return "", 200, None
        

