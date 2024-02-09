from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
import html

Question_bank = []
for question in question_data:
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    Question_bank.append(new_question)
quiz = QuizBrain(Question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()
# quiz.final_score()
