import turtle as t
import datetime


# Turtle move to foword with out drawing
def jump(distance):
    t.penup()
    t.fd(distance)
    t.pendown()


# Drawing Rect
def rectangle(width, height):

    # Draw half of bottom 
    t.fd(width / 2)

    # Draw Right
    t.fd(height)
    t.lt(90)

    # Draw Top
    t.lt(90)
    t.fd(width)

    # Draw Left
    t.lt(90)
    t.fd(height)

    # Draw half of bottom 
    t.lt(90)
    t.fd(width / 2)


# Make hand : Rect
def make_hand_shape(name, width, height):
    t.reset()                           # Tutle reset

    t.lt(90)                          # Move Tutle's location : Move back by height * 0.15
    jump(-height * 0.15)
    t.rt(90)

    t.begin_poly()                      # Draw polygon : Rect
    rectangle(width, height * 1.15)
    t.end_poly()

    clock_hand = t.get_poly()           # Register the shape as drawn rect
    t.register_shape(name, clock_hand)


# Make analog clock's face
def clockface(radius):
    t.reset()       # Move to start point
    t.pensize(7)    # set pen size
    # Devide clock face as 60
    for i in range(60):
        jump(radius)
        if i % 5 == 0:
            t.fd(25)            # Draw hour's mark
            jump(-radius - 25)  # Move to start point
        else:
            t.dot()             # Draw 10 minute's mark
            jump(-radius)       # Move to start point
        t.rt(6)
