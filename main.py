from turtle import Turtle,Screen
import random
screen = Screen()
screen.colormode(255)
rgb_colors = [(235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (114, 160, 193), (134, 168, 231), (15, 77, 146), (205, 87, 0), (244, 194, 194), (250, 218, 94), (244, 0, 161), (15, 192, 252), (255, 153, 51), (153, 51, 204), (255, 102, 204), (17, 238, 238)]

turt = Turtle()
turt.hideturtle()
turt.speed('fastest')
turt.setheading(220)
turt.penup()
turt.fd(260)
turt.setheading(0)


def print_dots():
    for _ in range(10):
        turt.pendown()
        turt.dot(15, random.choice(rgb_colors))
        turt.penup()
        turt.fd(45)


for _ in range(10):
    print_dots()
    turt.left(90)
    turt.fd(45)
    turt.left(90)
    turt.fd(450)
    turt.left(180)

screen.exitonclick()
