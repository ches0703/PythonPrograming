# HW0901.py
"""
Project : Turtle_Drawing user-Turtle defined module for drawing polygon with given center position
Author: Eun-seong Choi
Date of last update: 2022 / 11 / 09
Update list:
    - v1.1 : 11 / 09
        Import Turtle_Drawing
        Add for Turtle_Drawing : Circle drawing part
                               : some variavle calc part
        Make Funtion : fget_drawings()
"""

import turtle
import math
from Turtle_Drawing import*


def fget_drawings(fin):
    L_drawings = []
    # Read lines for file
    drawings = fin.readlines()
    for drawing in drawings:
        # Split line as blank char
        color, shape, cx, cy, radius = drawing.split()
        # Append to List & Change type some value
        L_drawings.append((int(cx), int(cy), shape, int(radius), color))
    return L_drawings

if __name__ == "__main__":
    turtle.setup(900, 500)
    turtle.title("Drawing polygons with user-defined Turtle_Drawing.py")
    t = turtle.Turtle()
    t.shape("classic")
    fin = open("HW09/polygon_drawings.txt")
    L_drawings = fget_drawings(fin)
    fin.close()
    for drawing in L_drawings:
        (cx, cy, shape, radius, color) = drawing
        center_pos = (cx, cy)
        print("drawing a {} {} of circumscribed circle's radius {} at center_pos({}, {}).".format(
            color, shape, radius, cx, cy))
        t.color(color)
        t.up()
        t.goto(center_pos)
        t.down()
        t.dot(10, "blue")
        t.write(center_pos)
        t.width(5)
        num_vert = getNumVertex(shape)
        drawPolygon(t, center_pos, num_vert, radius, color)
    # For prevent close window
    turtle.exitonclick()
