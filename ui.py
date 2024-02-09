from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text="Score : 0", background=THEME_COLOR, fg="white", font=("Agency FB", 16, "bold"))
        self.score_label.grid(row=0, column=1)
        self.q_area = Canvas(width=300, height=250, background="white")
        self.question_text = self.q_area.create_text(
            150, 125,
            width=280,
            text="hello",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR)
        self.q_area.grid(row=1, column=0, columnspan=2, pady=50)

        # True Button
        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(self.window, image=self.true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        # False Button
        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(self.window, image=self.false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        # while self.quiz.still_has_questions():
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.q_area.config(background="white")
        if self.quiz.still_has_questions():
            self.q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")

            self.q_area.itemconfig(self.question_text, text=self.q_text)
        else:
            self.q_area.itemconfig(self.question_text, text=f"You've completed the quiz.\n Your final score was: "
                                                            f"{self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("true")
        self.feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("false")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right:
            self.q_area.config(background="lightgreen")
        else:
            self.q_area.config(background="red")
        self.window.after(1000, self.get_next_question)

