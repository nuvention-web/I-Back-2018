from models.response import ResponseModel
from models.perfume import PerfumeModel

from werkzeug.security import safe_str_cmp

class ResponseController():

    def make_response(perfume_id, q1, q2, q3, q4, q5):
        """
        6 input params: stuff in a response model.
        1 output: response object(none)

        it param checks and then generates a response object
        """
        # valid perfume_id
        if not PerfumeModel.find_by_id(perfume_id):
            return "Invalid perfume_id.", 400, None
        
        """
        need a way to validate image_lnk inputs
        """

        """
        need to find out what errors are raised when saving and creating objects fail so i don't have to do this repetitive dumb coding.
        """

        try:
            new_response = ResponseModel(perfume_id, q1, q2, q3, q4, q5)
        except:
            # print("Error in logging response")
            return "Error making responses", 500, None

        try:
            new_response.save_to_db()
        except:
            # print ("Error in saving response object to db")
            return "Error saving response", 500, None

        return new_response 

    def get_responses(quantity):
        """
        0 input params: get all responses
        3 output params: error message, status code, response
        it gets responses, specified by the quantity value.
        """
        try:
            responses = ResponseModel.filter_below_id(quantity)
        except:
            return "Error retrieving responses", 500, None
        
        return "", 200, responses
