# Drawing and Loops
# Author: Vivian
# 14 October 2025

import turtle
window = turtle.Screen()  # Set up the window and its attributes
window.bgcolor("lightpink")
# TMNT - turtles
mikey = turtle.Turtle()
mikey.turtlesize(0.25) # size
mikey.color("orange") # colour
mikey.shape("turtle")
mikey.speed(2)
# Snowman
mikey.color("lightblue")
mikey.pencolor("lightblue")
mikey.fillcolor("lightblue")
mikey.width(5)
mikey.begin_fill()
mikey.circle(100)
mikey.end_fill()
mikey.penup()
mikey.goto(0, 200)
mikey.pd()
mikey.begin_fill()
mikey.circle(80)
mikey.end_fill()
mikey.penup()
mikey.goto(0, 360)
mikey.pd()
mikey.begin_fill()
mikey.circle(60)
mikey.end_fill()
mikey.clear()
# make 100 cookies
def make_cookie(x: int, y: int):
    # make sure turtle is pointing east
    mikey.setheading(0)
    # change the cookie colour
    mikey.color("brown")
    # draw a circle
    mikey.pu()
    mikey.goto(-5 + x,-30 + y)
    mikey.pd()
    mikey.circle(30)
    # put a chocolate chip on top left side
    mikey.pu()
    mikey.goto(-10 + x ,10 + y)
    mikey.stamp()
    # chocolate chip on top right
    mikey.goto(10 + x ,10 + y)
    mikey.stamp()
    # chocolate chip on bottom right
    mikey.goto(10 + x ,-10 + y)
    mikey.stamp()
    # chocolate chip on bottom left
    mikey.goto(-10 + x ,-10 + y )
    mikey.stamp()
    # chocolate chip in middle
    mikey.goto(0 + x ,0 + y)
    mikey.stamp()
mikey.speed(0)
# Make cookies in random locations
# Make 1000 cookies
mikey.speed(0)
make_cookie(0, 0)
make_cookie(100, 100)
make_cookie(100,-100)
make_cookie(-100,100)
make_cookie(-100,-100)
window.exitonclick()
