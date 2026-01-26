from turtle import Turtle,Screen
#creating the instance called timmy the turtle
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
#to draw a square
# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)
def moveforward():
    timmy.forward(50)
def movebackward():
    timmy.backward(50)
def turn_left():
    timmy.left(50)
def turn_right():
    timmy.right(50)
screen = Screen()
screen.listen()
screen.onkey(key="w",fun=moveforward)
screen.onkey(key="s",fun=movebackward)
screen.onkey(key="a",fun=turn_left)
screen.onkey(key="d",fun=turn_right)
screen.exitonclick()