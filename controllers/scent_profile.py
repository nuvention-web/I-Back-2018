from models.scent_profile import ScentProfileModel

from werkzeug.security import safe_str_cmp

class ScentProfileController():

    def make_scent_profile(q6, q7, tag1, tag2, sillage, image_lnk, vid_lnk, start_time, description):
        """
        7 input params: stuff in a scent profile.
        3 output: error message, status code, response object(none)

        it param checks and then generates a scent_profile
        """
        categories = ["Fresh", "Floral", "Spicy", "Woody"]

        if not(q6 is 0 or q6 is 1):
            return "q6 can only be 0 or 1", 400, None

        if not(q7 is 0 or q7 is 1 or q7 is 2 or q7 is 3):
            return "q7 can only be 0, 1, 2, or 3", 400, None

        """
        Not known yet.

        if tag1 not in categories:
            return "Unexpected category for tag1", 400, None
        """

        #if tag2 not in categories:
        #    return "Unexpected category for tag2", 400, None

        """
        need a way to validate image_lnk inputs
        """

        """
        need to find out what errors are raised when saving and creating objects fail so i don't have to do this repetitive dumb coding.
        """

        try:
            new_scent_profile = ScentProfileModel(q6, q7, tag1, tag2, sillage, image_lnk, vid_lnk, start_time, description)

        except:
            print("Error in creating scent_profile object")
            return "Error making model", 500, None

        try:
            new_scent_profile.save_to_db()
        except:
            print ("Error in saving scent_profile to db")
            return "Error saving model", 500, None

        return "", 201, None

    def get_scent_profile(mode, inp1, inp2):
        """
        3 input params: mode of getting, input1(mandatory), and input2(optional)
        3 output params: error message, status code, response
        it serves as the hub for getting scent profile, as there are various ways to access this data
        """

        if safe_str_cmp(mode, 'qs'):
            return ScentProfileController.get_by_qs(inp1, inp2)
        else:
            return "Unsupported mode.", 400, None
    
    def get_by_qs(q6, q7):
        """
        2 input params: answer for q6 and q7
        3 ouptut params: error message, status code, and response
        it finds the ScentProfileModel by filter->all for the first tag and filter->first the second tag.
        """

        try:
            target = ScentProfileModel.find_by_qs(q6, q7)
        except:
            return "Error in find_by_tags", 500, None
        target1 = ScentProfileModel.find_by_id(1)

        return "", 200, target


