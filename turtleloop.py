# from turtle import Turtle, Screen
#
# sirash = Turtle()
# sirash.shape("turtle")
# sirash.color("red")
#
#
# sirash.forward(100)
# sirash.right(90)
# sirash.forward(100)
# sirash.right(90)
# sirash.forward(100)
# sirash.right(90)
# sirash.forward(100)
#
#
#
from turtle import Turtle, Screen
import random
sirash = Turtle()
sirash.shape("turtle")
#
#
# for _ in range(15):
#     sirash.forward(10)
#     sirash.penup()
#     sirash.forward(10)
#
#     sirash.pendown()
#
#
#

colors = ["red", "green", "yellow", "violet"]
def draw_shape(n):
    for _ in range(n):
        sirash.forward(100)
        sirash.right(360/n)


for shape_side in range(3, 11):
    draw_shape(shape_side)
    sirash.color(random.choice(colors))



screen = Screen()
screen.exitonclick()
