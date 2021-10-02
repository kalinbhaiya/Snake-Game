import winsound
import turtle
import time
import random
from tkinter.messagebox import askquestion, showerror
from tkinter import *

delay = 0

score = 0
high_score = 0
master = Tk()
def enter(event):
    button.config(relief=GROOVE, fg='black', bg='grey')

def leave(event):
    button.config(relief=RAISED, fg='yellow', bg='red')

def button1():
    global delay
    value = spin.get()
    if value in ['Beginner','Normal','Pro','Expert','Veteran']:

        if value=='Beginner':
            delay=0.15
            master.destroy()

        elif value=='Normal':
            delay=0.09
            master.destroy()

        elif value=='Pro':

            delay=0.07
            master.destroy()

        elif value=='Expert':
            delay=0.05
            master.destroy()

        elif value=='Veteran':
            delay=0.03
            master.destroy()
    else:
        showerror('M-SNEK','Please select a valid difficulty level!')

def close():
    result = askquestion('M-SNEK','Do you want to exit?')
    if result=='yes':
        sys.exit()
    else:
        pass

master.config(background='black')
master.resizable(0,0)
master.geometry('300x150+600+300')
master.title('M-SNEK')
master.protocol('WM_DELETE_WINDOW',close)
label1 = Label(master,text='Welcome To M-SNEK!',font='cursive 15 bold italic',fg='white',bg='black').pack()
label2 = Label(master,text='Select Your In-Game Difficulty: ',font='cursibe 9 bold italic',bg='black',fg='white').place(x=20,y=50)
spin = Spinbox(master,values=('Beginner','Normal','Pro','Expert','Veteran'),width=10)
spin.place(x=210,y=51)
button = Button(master,text='PLAY!',fg='yellow',bg='red',activeforeground='red',activebackground='yellow',borderwidth=4,font='cursive 12 bold italic',cursor='hand2',command=button1)
button.pack(side=BOTTOM)
button.bind('<Enter>',enter)
button.bind('<Leave>',leave)
master.mainloop()

wn = turtle.Screen()
wn.title("M-SNEK")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color('white')
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

while True:
    wn.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        score = 0
        delay =delay

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))
    time.sleep(delay)

wn.mainloop()
