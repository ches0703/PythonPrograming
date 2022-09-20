# Turtle

import turtle
colors = ["red", "blue", "yellow"]

t = turtle.Turtle()

turtle.bgcolor("black")
t.width(5)
num_vertices = int(input("input num vertices : "))
length = 10
count = 0
turn_angle = (360//num_vertices)-1
while length < 200:
    t.pencolor(colors[count % num_vertices])
    t.forward(length)
    t.right(turn_angle)
    length += 5
    count += 1
