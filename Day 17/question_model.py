class Question:
    def __init__(self, text, answer):
        self.text = text.replace('&quot;', '\"')
        self.answer = answer

    def __str__(self):
        return "Question: " + self.text + " Answer: " + self.answer
