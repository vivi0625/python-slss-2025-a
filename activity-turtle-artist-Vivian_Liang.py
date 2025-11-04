# Turtle Artist
# Author: Vivian
# 28 October

import turtle

wn = turtle.Screen()
wn.bgcolor("#FFEFF7")
t = turtle.Turtle()
t.speed(15)
t.turtlesize(0.25)

# draw the first cherry
t.color("#DA627D")
t.begin_fill()
t.circle(50)
t.end_fill()

# draw the second cherry
t.penup()
t.goto(130, 5)
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()

# draw the stem
t.penup()
t.turtlesize(0.5)
t.pensize(5)
t.goto(130, 105)
t.pendown()
t.color("#A9C250")
t.right(30)
t.left(30)
t.setheading(120)
t.forward(100)

# draw another stem
t.penup()
t.turtlesize(0.5)
t.goto(5, 100)
t.pendown()
t.color("#A9C250")
t.setheading(50)
t.forward(120)

#finish the stem
t.penup()
t.goto(55, 195)
t.pendown()
t.color("#A9C250")
t.setheading(180)
t.backward(50)
t.hideturtle()
turtle.done()

wn.exitonclick()
