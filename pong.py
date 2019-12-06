#Simple Pong game in Python 3.
#Created by Pretam.

import turtle
import os

win=turtle.Screen()
win.title("Pong by Pretam")
win.bgcolor("black")
win.setup(width=800,height=600)
win.tracer(0)

#Paddle_A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)
#Paddle_B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball=turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.speed(0)
ball.penup()
ball.goto(0,0)
ball.dx=1
ball.dy=-1

#Score
score_a=0
score_b=0


#Function
def paddle_a_up():
    y=paddle_a.ycor()
    y+=10
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=10
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=10
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=10
    paddle_b.sety(y)

#Keyboard Binding
win.listen()
win.onkeypress(paddle_a_up,"w")
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_b_up,"Up")
win.onkeypress(paddle_b_down,"Down")

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,200)
pen.write("Player  A: 0  Player  B: 0",align="center",font=("Arial",18, "normal"))

#Main game Loop
while True:
    win.update()

    #Move the Ball
    ball.sety(ball.ycor()+0.15*ball.dy)
    ball.setx(ball.xcor()+0.15*ball.dx)

    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1
        os.system("aplay Beep1.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*=-1
        os.system("aplay Beep1.wav&")

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player  A: {}  Player  B: {}".format(score_a,score_b),align="center",font=("Arial",18, "normal"))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player  A: {}  Player  B: {}".format(score_a,score_b),align="center",font=("Arial",18, "normal"))


    #Paddle and ball collisions
    if ball.xcor() >340 and ball.xcor()<350 and ball.ycor() < paddle_b.ycor()+40 and ball.ycor() > paddle_b.ycor()-40:
        ball.setx(340)
        ball.dx*=-1
        os.system("aplay Beep1.wav&")

    if ball.xcor() <-340 and ball.xcor() >-350 and ball.ycor() < paddle_a.ycor()+40 and ball.ycor() > paddle_a.ycor()-40:
        ball.setx(-340)
        ball.dx*=-1
        os.system("aplay Beep1.wav&")
