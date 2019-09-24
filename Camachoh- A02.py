######################################################################
# Author: Henry Camacho              TODO: Change this to your name, if modifying
# Username: HenryJCamacho                   TODO: Change this to your username, if modifying
#
# Assignment: A02
# Purpose: To draw something we lie with loop
######################################################################
# Acknowledgements:
#
# original from
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################

import turtle

wn = turtle.Screen()

circle = turtle.Turtle()
circle.speed(10)

circle.fillcolor("yellow")
circle.begin_fill()
for face in range(75):
    circle.forward(10)
    circle.right(5)
circle.end_fill()

eyes = turtle.Turtle()
eyes.speed(10)

eyes.penup()
eyes.setpos(50, -50)
eyes.shape("triangle")
eyes.stamp()
eyes.setpos (-50, -50)

mouth = turtle.Turtle()
mouth.speed(10)
mouth.penup()
mouth.setpos(-50, -100)
mouth.pendown()
mouth.right(90)
for smile in range(30):
    mouth.forward(5)
    mouth.left(5)


wn.exitonclick()





