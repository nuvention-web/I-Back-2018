from flask_restful import Resource, reqparse

from controllers.response import ResponseController

class Response(Resource):
    """
    /response/{quantity}
    """

    def get(self, quantity):

        error_message, status, responses = ResponseController.get_responses(quantity)

        if error_message:
            return {"error_message": error_message}, status

        return {"responses": list(map(lambda x: x.json() if x else None, responses))}, status
