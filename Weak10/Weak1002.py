import turtle
turtle.setup(600, 500)
turtle.mode("standard") # mode standard sets initial heading right
t = turtle.Turtle()
t.pensize(2)
t.up(); t.shape(name='classic'); t.down()
radius = 50
polygons = [(-225, 150, "red", 3), (-75, 150, "blue", 4), (75, 150, "green", 5),\
(225, 150, "magenta", 6), (-225, -50, "brown", 7), (-75, -50, "chocolate", 8),\
(75, -50, "black", 9), (225, -50, "indigo", 0)]
for i in range(len(polygons)):
    (pos_x, pos_y, shape_color, num_vertices) = polygons[i]
    t.up(); t.goto(pos_x, pos_y); t.setheading(180); t.down()
    t.color(shape_color)
    if num_vertices > 2:
        t.circle(radius, steps = num_vertices)
    else:
        t.circle(radius)

turtle.exitonclick()