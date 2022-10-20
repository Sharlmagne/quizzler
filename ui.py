from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.quiz = quiz_brain

        # Score count
        self.score_count = Label(self.window, text="Score: 0", font=("Arial", 8, "bold"), bg=THEME_COLOR, fg="white")
        self.score_count.grid(row=0, column=1, pady=20, padx=20)

        # Question window
        self.canvas = Canvas(width=300, height=250)
        self.question_window = self.canvas.create_window(150, 125)
        self.question = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20, padx=20)

        # Buttons
        true_btn_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_btn_img, highlightthickness=0, command=self.true_answer)
        self.true_btn.grid(row=2, column=0, pady=20, padx=20)

        false_btn_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_btn_img, highlightthickness=0, command=self.false_answer)
        self.false_btn.grid(row=2, column=1, pady=20, padx=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            final_text = f"You've completed the quiz\nYour final score was: {self.quiz.score}/{self.quiz.question_number}"
            self.canvas.itemconfig(self.question, text=final_text)
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def false_answer(self):
        answer = self.quiz.check_answer("False")
        self.give_feedback(answer)

    def true_answer(self):
        answer = self.quiz.check_answer("True")
        self.give_feedback(answer)

    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
            self.score_count.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)








