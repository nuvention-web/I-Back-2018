from flask_restful import Resource, reqparse

from controllers.bought import BoughtController

class Bought(Resource):
    """
    /notbought
    """
    parser = reqparse.RequestParser()
    parser.add_argument('q1',
            type=str,
            required=True,
            help="q1 field is required and cannot be left blank.",
            )
    parser.add_argument('q2',
            type=str,
            required=True,
            help="q2 field is required and cannot be left blank.",
            )
    parser.add_argument('q3',
            type=str,
            required=True,
            help="q3 field is required and cannot be left blank.",
            )
    parser.add_argument('name',
            type=str,
            required=True,
            help="name field is required and cannot be left blank.",
            )
    parser.add_argument('email',
            type=str,
            required=True,
            help="email field is required and cannot be left blank.",
            )


    def post(self, mode):
        data = Bought.parser.parse_args()

        error_message, status, response = BoughtController.make_bought(data['q1'], data['q2'], data['q3'], data['name'], data['email'])

        if error_message:
            return {"error_message": error_message}, status

        return {"response": "Success!"}, status

    def get(self, mode):

        error_message, status, response = BoughtController.get_bought(mode)

        if error_message:
            return {"error_message": error_message}, status

        return {"response": list(map(lambda x : x.json() if x else None, response))}, status

