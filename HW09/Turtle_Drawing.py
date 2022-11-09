# Turtle_Drawing.py
# 21912070 최은성
# For 0903.py
import turtle
import math

# Transform Polygon name to Num of vertex
def getNumVertex(polygon_name):
    polygon_name_to_num = {
        "triangle": 3,
        "square": 4,
        "pentagon": 5,
        "hexagon": 6,
        "heptagon": 7,
        "octagon": 8,
        "nonagon": 9,
        "decagon": 10
    }
    return polygon_name_to_num[polygon_name]


# Transform Num of vertex to Polygon name
def getPolygonName(num_vertex):
    polygon_num_to_name = {
        3: "triangle",
        4: "square",
        5: "pentagon",
        6: "hexagon",
        7: "heptagon",
        8: "octagon",
        9: "nonagon",
        10: "decagon"
    }
    return polygon_num_to_name[num_vertex]


def drawPolygon(t, center_pos, num_vertex, radius, color):
    # Set Color
    t.color(color)
    # Calc : Need variable for Draw polygon
    poligon_angle = 180 * (num_vertex - 2) / num_vertex
    theta = math.pi / num_vertex
    side = (math.sin(theta) * (2 * radius))
    # Go to Center
    t.up()
    t.goto(center_pos[0], center_pos[1])
    # Start draw
    # Draw Circle
    t.goto(center_pos[0], center_pos[1] - radius)
    t.width(1)
    t.down()
    t.circle(radius)
    t.up()
    # Draw polygon
    # Calc start point x, y & Move start position
    t.width(3)
    t.goto(center_pos[0] - side / 2,
           center_pos[1] - radius * (math.cos(theta)))
    t.dot(10, "red")  # Print dot : Start Position, red
    t.write(t.position())  # Print now position : Start Position
    t.down()
    for i in range(num_vertex):
        t.forward(side)  # Draw Line
        t.left(180 - poligon_angle)  # Turn angle 
