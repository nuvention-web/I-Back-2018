from flask_restful import Resource, reqparse

from controllers.quiz import QuizController

class Quiz(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('ans1',
            type=str,
            required=True,
            help="This field is required and cannot be left blank."
            )
    parser.add_argument('ans2',
            type=str,
            required=True,
            help="This field is required and cannot be left blank."
            )
    parser.add_argument('ans3',
            type=str,
            required=True,
            help="This field is required and cannot be left blank."
            )
    parser.add_argument('ans4',
            type=str,
            required=True,
            help="This field is required and cannot be left blank."
            )

    def post(self):
        data = Quiz.parser.parse_args()

        error_message, status, response = QuizController.respond_quiz(int(data['ans1']), int(data['ans2']), int(data['ans3']), int(data['ans4']))

        if error_message:
            return {"error_message": error_message}, status

        return {"response": response}, status

