import turtle
import time
turtle.setup(500, 500, 200, 200)  # window width, height, startx, starty
turtles = []
turtle_names = ['square', 'circle', 'triangle', 'turtle', 'arrow', 'classic']
turtle_colors = ['red', 'green', 'blue', 'orange', 'brown', 'magenta']
turtle_positions = [(-175, 100), (0, 100), (175, 100),
                    (-175, -100), (0, -100), (175, -100)]
for i in range(len(turtle_names)):
    t = turtle.Turtle()  # create turtle.Pen()
    t.shape(name=turtle_names[i])
    t.color(turtle_colors[i])
    t.shapesize(5)
    t.up()
    t.setpos(turtle_positions[i])
    t.down()
    turtles.append(t)
turn_angle = 5  # 5 degree for each rotation
for i in range(360//turn_angle):  # repeat the rotation with given angle
    for t in turtles:
        t.up()
        t.right(turn_angle)
        t.down()  # turn right by the given angle
        t.dot(5, 'red')
    time.sleep(1)
turtle.exitonclick()
