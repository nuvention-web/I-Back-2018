from flask_restful import Resource, reqparse

from controllers.scent_profile import ScentProfileController

class ScentProfile(Resource):
    """
    /scentprofile/int:q6/int:q7
    """

    parser = reqparse.RequestParser()
    parser.add_argument('q6',
            type=int,
            required=True,
            help="This field is required and cannot be left blank."
            )
    parser.add_argument('q7',
            type=int,
            required=True,
            help="This field is required and cannot be left blank."
            )
    parser.add_argument('tag1',
            type=str,
            required=True,
            help="This field is required and cannot be left blank."
            )
    parser.add_argument('tag2',
            type=str,
            required=True,
            help="This field is required and cannot be left blank."
            )
    parser.add_argument('sillage',
            type=str,
            required=True,
            help="This field is required and cannot be left blank."
            )
    parser.add_argument('image_lnk',
            type=str,
            required=True,
            help="This field is required and cannot be left blank."
            )
    parser.add_argument('sound_lnk',
            type=str,
            required=True,
            help="This field is required and cannot be left blank."
            )
    
    def post(self, q6, q7):
        data = ScentProfile.parser.parse_args()

        error_message, status, response = ScentProfileController.make_scent_profile(data['q6'], data['q7'], data['tag1'], data['tag2'], data['sillage'], data['image_lnk'], data['sound_lnk'])

        if error_message:
            return {"error_message": error_message}, status

        return {"message": "Success!"}, status

    def get(self, q6, q7):

        error_message, status, response = ScentProfileController.get_scent_profile('qs', q6, q7)
        

        if error_message:
            return {"error_message": error_message}, status

        return {"response": response.json()}, status


class ScentProfileAdmin(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('q6',
            type=int,
            required=True,
            help="This field is required and cannot be left blank."
            )
    parser.add_argument('q7',
            type=int,
            required=True,
            help="This field is required and cannot be left blank."
            )
    
    def get(self, Q6, Q7):
        if error_message:
            return {"error_message": error_message}, status

        return {"response": response}, status        
