# HW0502.py
"""
Project : Turtle graphic - Polygon with given center position
Author: Eun-seong Choi
Date of last update: 2022 / 10 / 06
Update list:
    - v1,1 : 10 /6
        Make a funtion of drawPolygon
            - Calc start position
            - drawing part

"""

# Import part
import turtle
import math


# Draw Polygon
def drawPolygon(t, center_x, center_y, line_length, num_vertices):
    # Calc poligon angle : one vertex
    poligon_angle = 180 * (num_vertices-2)/num_vertices
    t.up()
    # Calc start point x, y & Move start position
    t.goto(center_x-(1/2*line_length),
           center_y-(1/2*line_length*math.tan(math.radians(poligon_angle/2))))
    # Start draw
    t.down()
    for i in range(num_vertices):
        t.dot(10, "red")
        t.write(t.position())  # Print now position
        t.forward(line_length)
        t.left(180 - poligon_angle)


# Application of drawPolygon
t = turtle.Turtle()
center_x, center_y, num_vertices, line_length =\
    map(int,
        input("input center_x, center_y, num_vertices, and line_length : ")
        .split(' '))
center_pos = (center_x, center_y)
line_width = 3
t.up()
t.goto(center_pos)
t.down()
t.dot(10, "red")
t.write(center_pos)
t.width(line_width)
t.pencolor("blue")
drawPolygon(t, center_x, center_y, line_length, num_vertices)
# To not close turtle graphic program immediately, use this code
turtle.exitonclick()
