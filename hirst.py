# import the turtle package
from turtle import *
from random import *

# we used colormode to help create our color palette
colormode(255)
# we used speed to make it fast
speed ("fastest")
# this is used to raise the pen up
penup()
# this is used to hide the turtle
hideturtle()

# declare a function to randomly combine different rgb numbers
def x():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    col = (r, g, b)
    # return the combiantion as col
    return col

# set a heading (in degrees)
setheading (225)
# move forward 350 paces
forward (350)
# set another heading (in degrees)
setheading(0)
# this will take the turtle to the bottom left of the screen

# create a for loop to run 100 times
for _ in range (1,101):
    # create dots with a radius of 20 and a random color    
    dot (20,x())
    # let this dot move 50 paces
    forward (50)
    
    # when it loops a number of times divisble by 10
    if _ % 10==0:
        # we set a new heading 90 degrees
        setheading(90)
        # move forward 50 paces
        forward(50)
        # change the heading to 180 degrees
        setheading(180)
        # move 500 paces
        forward (500)
        # change the heading to face right
        setheading(0)
        # the loop reruns

# this keeps the screen on
mainloop()