from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self,quizbrain:QuizBrain):
        self.quiz=quizbrain
        self.windows=Tk()
        self.windows.title(string="Quizzler")
        self.windows.config(bg=THEME_COLOR,pady=20,padx=20)

        self.score_text=Label(text='Score',bg=THEME_COLOR,padx=20,pady=20,fg='white')
        self.score_text.grid(row=0,column=1)

        self.canvas=Canvas()
        self.quiz_text=self.canvas.create_text(150,125,text="Question",fill=THEME_COLOR,width=280,font=('arial',20,'italic'))
        self.canvas.config(height=250,width=300)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=20)

        self.right_img=PhotoImage(file='./images/true.png')
        self.right_button=Button(image=self.right_img,padx=20,pady=20,command=self.right_pressed)
        self.right_button.grid(row=2,column=0)

        self.wrong_img=PhotoImage(file='./images/false.png')
        self.wrong_button=Button(image=self.wrong_img,padx=20,pady=20,command=self.wrong_pressed)
        self.wrong_button.grid(row=2,column=1)

        self.get_next_que()

        self.windows.mainloop()

    def get_next_que(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score :{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text,text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text,text=f"You've reached at end of the quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state='disabled')

    def right_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.windows.after(1000,self.get_next_que)

