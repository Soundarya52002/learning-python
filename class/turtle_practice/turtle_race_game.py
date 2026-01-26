from turtle import Turtle, Screen
import random

# -------------------- Screen Setup --------------------
screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race 🐢")

# -------------------- User Bet --------------------
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color:"
)

# -------------------- Game Data --------------------
colours = ["red", "blue", "brown", "green", "orange", "black", "yellow"]
y_positions = [-70, -40, -10, 20, 50, 80, 110]
all_turtles = []

# -------------------- Create Turtles --------------------
for i in range(len(colours)):
    turtle = Turtle(shape="turtle")
    turtle.color(colours[i])
    turtle.penup()
    turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(turtle)

# -------------------- Start Game --------------------
is_game_on = False
if user_bet:
    is_game_on = True

# -------------------- Race Logic --------------------
while is_game_on:
    for turtle in all_turtles:
        # Check if turtle reached finish line
        if turtle.xcor() > 230:
            is_game_on = False
            winning_colour = turtle.pencolor()

            if winning_colour == user_bet.lower():
                print(f"You WON 🎉 The {winning_colour} turtle is the winner!")
            else:
                print(f"You LOST 😢 The {winning_colour} turtle won the race.")

            break

        # Move turtle forward randomly
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# -------------------- Exit on Click --------------------
screen.exitonclick()
