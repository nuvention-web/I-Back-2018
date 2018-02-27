from flask_restful import Resource, reqparse

from controllers.quiz import QuizController

class Quiz(Resource):
    """
    /quiz/<int:q6>/<int:q7>
    """

    def get(self, q6, q7):

        error_message, status, scent_profile, perfumes = QuizController.get_perfumes(q6, q7)

        if error_message:
            return {"error_message": error_message}, status

        return {"response": {"scent_profile": scent_profile.json(), "perfumes": list(map(lambda x: x.json() if x else None, perfumes))}}, status

