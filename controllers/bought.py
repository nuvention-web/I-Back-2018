from models.bought import BoughtModel

class BoughtController():

    @classmethod
    def make_bought(cls, q1, q2, q3, name, email):
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
                result = []
                result.append(BoughtModel.find_by_id(int(mode)))
                return "", 200, result
            except:
                return "Error retrieving bought by id", 500, None

        

        





