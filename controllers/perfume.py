from models.perfume import PerfumeModel
from models.scent_profile import ScentProfileModel

from werkzeug.security import safe_str_cmp

class PerfumeController():

    def make_perfume(name, designer, image_lnk, buy_lnk, scent_profile_id):
        """
        5 input params: stuff in a scent profile.
        3 output: error message, status code, response object(none)

        it param checks and then generates a perfume object
        """
        #valid scent_profile_id
        if not ScentProfileModel.find_by_id(scent_profile_id):
            return "Invalid scent_profile_id.", 400, None
        
        if PerfumeModel.find_by_name(name):
            return "Perfume already exists.", 400, None

        """
        need a way to validate image_lnk inputs
        """

        """
        need to find out what errors are raised when saving and creating objects fail so i don't have to do this repetitive dumb coding.
        """

        try:
            new_perfume = PerfumeModel(name, designer, image_lnk, buy_lnk, scent_profile_id)
        except:
            print("Error in creating perfume object")
            return "Error making model", 500, None

        try:
            new_perfume.save_to_db()
        except:
            print ("Error in saving perfume object to db")
            return "Error saving model", 500, None

        return "", 201, None 

    def update_perfume(name, designer, image_lnk, buy_lnk, scent_profile_id):
        """
        5 input params: stuff in a scent profile.
        3 output: error message, status code, response object(none)

        it param checks and then generates a perfume object
        """

        #valid scent_profile_id for update
        if not ScentProfileModel.find_by_id(scent_profile_id):
            return "Invalid scent_profile_id.", 400, None
        
        if not PerfumeModel.find_by_name(name):
            return "Perfume does not exists.", 400, None
        
        target_perfume = PerfumeModel.find_by_name(name)
        
        target_perfume.name = name
        target_perfume.designer = designer
        target_perfume.image_lnk = image_lnk
        target_perfume.buy_lnk = buy_lnk
        target_perfume.scent_profile_id = scent_profile_id

        try :
            target_perfume.save_to_db()
            
        except:
            print ("Error in saving perfume object to db")
            return "Error saving model", 500, None

        return "", 200, None

    def get_perfume(mode, inp1):
        """
        2 input params: mode of getting, input1(mandatory), and input2(optional)
        3 output params: error message, status code, response
        it serves as the hub for getting perfume object, as there are various ways to access this data
        """

        if safe_str_cmp(mode, 'name'):
            return PerfumeController.get_by_name(inp1)
        else:
            return "Unsupported mode.", 400, None

    def get_by_name(name):
        """
        1 input param: name of the perfume it's looking for
        3 output param: error message, status code, response object from the query
        """

        try:
            target = PerfumeModel.find_by_name(name)
        except:
            return "Error getting by name", 500, None

        if not target: 
            return "No such name found", 400, None

        return "", 200, target

        
    
