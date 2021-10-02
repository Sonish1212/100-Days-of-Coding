class QuizBrain:
    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print(f'Your total score is {self.score} / {self.question_number}')
            print("Thanks for playing")
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"{self.question_number}: {current_question.text} (True/False):")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct answer")
            print(f"Your current score is: {self.score}/{self.question_number}")
        else:
            print("You got it wrong")
            print(f"Your current score is: {self.score}/{self.question_number}")

        print(f"Correct answer is {correct_answer}")
        print("\n")



