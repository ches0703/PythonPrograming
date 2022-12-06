# Analog Clock Animation
# HW1301.py
"""
Project : Analog Clock Animation
Author: Eun-seong Choi
Date of last update: 2022 / 12 / 07
Update list:
    - v1.1 : 12 / 01
        Fix Funtion : tick()
            t.tracer(True) call just once in loof
        Add commit
"""
import turtle as t
import datetime


# Turtle move to foword with out drawing
def jump(distance):
    t.pu()
    t.fd(distance)
    t.pd()


# Drawing Rect
def rectangle(width: float, height: float):

    # Draw half of bottom
    t.fd(width / 2)
    t.lt(90)

    # Draw Right
    t.fd(height)
    t.lt(90)

    # Draw Top
    t.fd(width)
    t.lt(90)

    # Draw Left
    t.fd(height)
    t.lt(90)

    # Draw half of bottom
    t.fd(width / 2)


# Make hand : Rect
def make_hand_shape(name: str, width: float, height: float):
    t.reset()                           # Tutle reset

    # Move Tutle's location : Move back by height * 0.15
    t.lt(90)
    jump(-height * 0.15)
    t.rt(90)

    t.begin_poly()                      # Draw polygon : Rect
    rectangle(width, height * 1.15)
    t.end_poly()

    clock_hand = t.get_poly()           # Register the shape as drawn rect
    t.register_shape(name, clock_hand)


# Make analog clock's face
def clockface(radius: float):
    t.reset()       # Move to start point
    t.pensize(7)    # set pen size
    # Devide clock face as 60
    for i in range(60):
        jump(radius)
        if i % 5 == 0:
            t.fd(25)            # Draw hour's mark
            jump(-radius - 25)  # Move to start point
        else:
            t.dot(3)             # Draw 10 minute's mark
            jump(-radius)       # Move to start point
        t.rt(6)


# Setup clock's time
def setup():
    # Define clock's hand, svae time's Stirg Value : writer
    global sec_hand, min_hand, hour_hand, writer
    t.mode("logo")  # Set the basic direction
    # Make hands
    make_hand_shape("sec_hand", 5, 150)     # Sec's hand
    make_hand_shape("min_hand", 10, 130)    # Min's hane
    make_hand_shape("hour_hand", 15, 110)   # Hour's hand

    clockface(160)  # Make clock's hand

    # Get object from resisterd hour hand
    hour_hand = t.Turtle()
    hour_hand.shape("hour_hand")
    hour_hand.color("black", "black")

    # Get object from resisterd min hand
    min_hand = t.Turtle()
    min_hand.shape("min_hand")
    min_hand.color("blue", "blue")

    # Get object from resisterd sec hand
    sec_hand = t.Turtle()
    sec_hand.shape("sec_hand")
    sec_hand.color("red", "red")

    # Resize hand
    for hand in sec_hand, min_hand, hour_hand:
        hand.resizemode("user")
        hand.shapesize(1, 1, 3)
        hand.speed(0)

    # Hide turtle's cursor
    t.ht()

    writer = t.Turtle()
    writer.ht()     # Hide turtle's cursor
    writer.pu()     # Pen up
    writer.bk(85)   # Backword : move to back


# Return String of week
def getWeekDayString(t: datetime.date) -> str:
    WeekdayString = ["Monday", "Tuesday", "Wednesday",
                     "Thursday", "Friday", "Saturday", "Sunday"]
    return WeekdayString[t.weekday()]


# Return String of date
def getDateString(date: datetime.date) -> str:
    month_name = ["Jan", "Feb", "Mar", "Apr", "May",
                  "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
    year = date.year
    month = month_name[date.month - 1]
    day = date.day
    return "{} {} {}".format(month, day, year)


# Clock's motion : tick
def tick():
    # Get now's date info
    now = datetime.datetime.today()
    # Calc time data as float type : to hand motion look like analog
    sec = now.second + now.microsecond * 0.000001
    minute = now.minute + sec / 60.0
    hour = now.hour + minute / 60.0
    try:
        t.tracer(False)      # Turtle's motion temporary stop
        writer.clear()       # Writer's clear
        writer.home()
        writer.pencolor("darkred")
        writer.fd(65)
        # Write date's week name
        writer.write(getWeekDayString(now),
                     align="center", font=("Courier", 14, "bold"))
        writer.bk(150)
        writer.pencolor("brown")
        # Write date's info
        writer.write(getDateString(now),
                     align="center", font=("Courier", 14, "bold"))
        writer.bk(30)
        writer.pencolor("red")
        writer.write("[{:2d} : {:2d} : {:2d}]".format(int(sec), int(minute), int(hour)),
                     align="center", font=("Courier", 14, "bold"))
        writer.forward(115)
        # Hand motion
        hour_hand.setheading(30 * hour + 90)
        min_hand.setheading(6 * minute + 90)
        sec_hand.setheading(6 * sec + 90)
        t.tracer(True)      # Apply changed motion
        # Re-Call "tick" funtion after 100ms
        t.ontimer(tick, 100)
    except t.Terminator:    # User pressed STOP
        pass                # End this funtion


# Main funtion
def main() -> str:
    t.tracer(False)
    setup()
    t.tracer(True)
    tick()
    return "Analog clock demo"


# Applicaition
if __name__ == "__main__":
    t.mode("logo")
    t.setup(500, 500)                       # Set window's size
    t.title("My Analog Clock with Python")  # Set window's tiltle
    msg = main()
    print(msg)
    t.mainloop()
