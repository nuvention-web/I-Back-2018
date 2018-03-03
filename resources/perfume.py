from flask_restful import Resource, reqparse

from controllers.perfume import PerfumeController

class Perfume(Resource):
    """
    /perfume/<str:name>
    """

    parser = reqparse.RequestParser()
    parser.add_argument('name',
            type=str,
            required=True,
            help="This field is required and cannot be left blank."
            )
    parser.add_argument('designer',
            type=str,
            required=True,
            help="This field is required and cannot be left blank."
            )
    parser.add_argument('image_lnk',
            type=str,
            required=True,
            help="This field is required and cannot be left blank."
            )
    parser.add_argument('buy_lnk',
            type=str,
            required=True,
            help="This field is required and cannot be left blank."
            )
    parser.add_argument('scent_id',
            type=int,
            required=True,
            help="This field is required and cannot be left blank."
            )
    
    
    def post(self, name):
        data = Perfume.parser.parse_args()

        error_message, status, response = PerfumeController.make_perfume(data['name'], data['designer'], data['image_lnk'], data['buy_lnk'], data['scent_id'])

        if error_message:
            return {"error_message": error_message}, status

        return {"message": "Success!"}, status

    def get(self, name):

        error_message, status, response = PerfumeController.get_perfume('name', name)

        if error_message:
            return {"error_message": error_message}, status

        return response.json(), status

