from models.quiz import QuizModel

from werkzeug.security import safe_str_cmp

class QuizController():

    def respond_quiz(ans1, ans2, ans3, ans4):
        """
        4 input params: answer for questions 1, 2, 3, 4
        3 output params: error message, status code, response object

        processes the answers of the quiz
        """
        if ans1 > 1 or ans2 > 1 or ans3 > 1 or ans4 > 1:
            return "invalid answer(s)", 400, None

        quiz = QuizModel(ans1, ans2, ans3, ans4)
        quiz.save_to_db()
        """
        try:
        except:
            return "Error in creating and saving user", 500, None
            """

        out = str(ans1) + ' ' + str(ans2) + ' ' +  str(ans3) + ' ' + str(ans4)
        return "", 200, out 

