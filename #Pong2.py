# Pong 2.0


import turtle
import os

os.system("aplay coolsaber.wav&")

wn = turtle.Screen()
wn.title("Pong2.0")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = .5
ball.dy = .5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: 0       Player 2: 0".format(score_a, score_b), align="center", font=("Times New Roman", 18, "normal"))

# Function
def paddle_a_up():
    y=paddle_a.ycor()
    y +=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y -=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y +=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y -=20
    paddle_b.sety(y)

# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main Game Loop
while True:
    wn.update()
    
    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *=-1
        os.system("aplay Slap.wav&")
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1
        os.system("aplay Slap.wav&")

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        os.system("aplay sicko.wav&")
        pen.clear()
        pen.write("Player 1: {}       Player 2: {}".format(score_a, score_b), align="center", font=("Times New Roman", 18, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        os.system("aplay chewy.wav&")
        pen.clear()
        pen.write("Player 1: {}       Player 2: {}".format(score_a, score_b), align="center", font=("Times New Roman", 18, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        os.system("aplay lasrhit2.wav&")
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        os.system("aplay lasrhit2.wav&")
        ball.dx *= -1