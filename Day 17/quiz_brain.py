class QuizBrain:
    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.question_number = 0
        self.score = 0

    def nextQuestion(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        self.checkAnswer(input(
            f"{self.question_number}) {question.text} (True/False)?:"), question.answer)

    def hasQuestions(self):
        return len(self.questions_list) > self.question_number

    def checkAnswer(self, answer, correctAnswer):
        if(answer.lower() == correctAnswer.lower()):
            print("You got it right!")
            self.score += 1
        else: 
            print("That's wrong")
            print(f"The correct answer was: {correctAnswer}")
        print(f"Your current score is {self.score}/{len(self.questions_list)}")
        print("")
