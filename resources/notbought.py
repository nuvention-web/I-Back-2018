from flask_restful import Resource, reqparse

from controllers.notbought import NotBoughtController

class NotBought(Resource):
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


    def post(self):
        data = NotBought.parser.parse_args()

        error_message, status, response = NotBoughtController.make_notbought(data['q1'], data['q2'], data['q3'], data['name'])

        if error_message:
            return {"error_message": error_message}, status

        return {"response": {"Cards": list(map(lambda x: x.json() if x else None, response))}}, status

    def get(self):


        return {"response": "hi"} 

