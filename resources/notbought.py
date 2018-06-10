from flask_restful import Resource, reqparse

from controllers.notbought import NotBoughtController

class NotBought(Resource):
    """
    /notbought/mode
        1. mode can be all
        2. or id
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


    def post(self, mode):
        data = NotBought.parser.parse_args()
        quiz_id = int(mode)

        error_message, status, response = NotBoughtController.make_notbought(data['name'], quiz_id, data['q1'], data['q2'], data['q3'])

        if error_message:
            return {"error_message": error_message}, status

        return {"response": {"Cards": list(map(lambda x: x.json() if x else None, response))}}, status

    def get(self, mode):

        error_message, status, response = NotBoughtController.get_notbought(mode)

        if error_message:
            return {"error_message": error_message}, status

        return {"response": list(map(lambda x: x.json() if x else None, response))}, status


    def delete(self, mode):

        error_message, status, response = NotBoughtController.delete_notbought(mode)

        if error_message:
            return {"error_message": error_message}, status

        return {"response": "Success!"}, status
