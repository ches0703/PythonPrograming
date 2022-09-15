import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("red")
t.width(3)

wihth = int(input("width : "))
turn_angle = 90
loop_count = 0
t.home()
t.write(t.position())
start_x = wihth//2
start_y = wihth//2
t.up()
t.goto((-start_x, -start_y))
t.down()
while loop_count < 4:
    t.write(t.position())
    t.forward(wihth)
    t.left(turn_angle)
    loop_count += 1
t.up()
t.home()
t.down()
