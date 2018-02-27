from models.perfume import PerfumeModel
from models.scent_profile import ScentProfileModel

from werkzeug.security import safe_str_cmp

class QuizController():

    def get_perfumes(q6, q7):
        """
        2 input params: answer for q6 and q7
        3 output params: error message, status code, response
        it serves as the hub for getting perfume object, as there are various ways to access this data
        """
        if not(q6 is 0 or q6 is 1):
            return "q6 can only be 0 or 1", 400, None

        if not(q7 is 0 or q7 is 1 or q7 is 2 or q7 is 3):
            return "q7 can only be 0, 1, 2, or 3", 400, None
        try:     
            target_scent = ScentProfileModel.find_by_qs(q6, q7)
        except:
            return "Error retrieving scent_profile.", 500, None

        response = []
        response.append(target_scent)
        response = response + target_scent.children

        return "", 200, response


