from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 15, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("QUIZZLER")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.ques_text = self.canvas.create_text(150, 125, text="Question", font=FONT, fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        tick_image = PhotoImage(file="./images/true.png")
        cross_image = PhotoImage(file="./images/false.png")
        self.tick_button = Button(image=tick_image, borderwidth=0, bg=THEME_COLOR, command=self.true_ans)
        self.tick_button.grid(row=2, column=0)
        self.cross_button = Button(image=cross_image, borderwidth=0, bg=THEME_COLOR, command=self.false_ans)
        self.cross_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.ques_text, text=q_text)
        else:
            self.canvas.itemconfig(self.ques_text, text="You have reached the end.")

    def true_ans(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        self.update_score()

    def false_ans(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
