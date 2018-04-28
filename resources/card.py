from flask_restful import Resource, reqparse

from controllers.card import CardController

class Card(Resource):
    """
    /card/<string: mode>
    mode can be 
        1. name - name of the card you want to get
        2. all - all of the cards
    """
    parser = reqparse.RequestParser()
    parser.add_argument('description',
            type=str,
            required=True,
            help="Description field is required and cannot be left blank.",
            )
    parser.add_argument('vid_lnk',
            type=str,
            required=True,
            help="video_lnk field is required and cannot be left blank.",
            )
    parser.add_argument('image_lnk',
            type=str,
            required=True,
            help="picture_lnk field is required and cannot be left blank.",
            )
    parser.add_argument('name',
            type=str,
            required=True,
            help="name field is required and cannot be left blank.",
            )
    parser.add_argument('accord',
            type=str,
            required=True,
            help="accord field is required and cannot be left blank.",
            )
    parser.add_argument('start_time',
            type=str,
            required=True,
            help="accord field is required and cannot be left blank.",
            )


    def post(self, mode):
        data = Card.parser.parse_args()

        error_message, status, response = CardController.make_card(data['name'], data['accord'], data['image_lnk'], data['vid_lnk'], data['start_time'], data['description'])

        if error_message:
            return {"error_message": error_message}, status

        return {"message": "Success!"}, status

    def get(self, mode):

        # get_card needs to return a list
        error_message, status, response = CardController.get_card(mode)

        if error_message:
            return {"error_message": error_message}, status

        return {"response": list(map(lambda x: x.json_debug() if x else None, response))}

