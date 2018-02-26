from flask_restful import Resource, reqparse

from controllers.scent_profile import ScentProfileController

class ScentProfile(Resource):

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
    
    def get(self, q6, q7):

        error_message, status, response = ScentProfileController.respond_quiz(q6, q7)

        if error_message:
            return {"error_message": error_message}, status

        return {"response": response}, status

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
