from quiz_brain import QuizBrain
from data import Questions


# VARIABLES
questions = Questions(
    "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean")
quizBrain = QuizBrain(questions.questions_bank)

# MAIN
while quizBrain.hasQuestions():
    answer = quizBrain.nextQuestion()

print("You've completed the quiz")
print(f"Your score is {quizBrain.score}/{len(quizBrain.questions_list)}")
