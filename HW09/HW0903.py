# HW0903.py
"""
Project : Stop Watch program
Author: Eun-seong Choi
Date of last update: 2022 / 11 / 09
Update list:
    - v1.1 : 11 / 09
        Define : runTimer(), start(), reset()
        Global variable declaration
        Make screen layout : Add Time text, stat, stop reset Btn
        Delete Useless variable : timer, stop_time
"""
import time
from tkinter import *

# RunTimer : Print increse time when running, if not running, print elapsed_time
def runTimer():
    global start_time, elapsed_time, prev_elapsed_time
    if (running):
        cur_time = time.time()  # Current time record
        time_diff = cur_time - start_time  # Calc difference of time : current time - when click'start' time(start_time)
        elapsed_time = time_diff + prev_elapsed_time  # elapsed time is prev_elapsed_time + difference of time
        timeText.configure(text="{:7.3f}".format(elapsed_time))  # Print elapsed time to Label of timeText
    window.after(10, runTimer)  # wait 10ms

# Start : if runing is False, change true, record start_time
def start():
    global running, start_time, elapsed_time, prev_elapsed_time
    if (running != True):
        running = True
        start_time = time.time() # record Start time
        prev_elapsed_time = elapsed_time  # prev_elapsed_time is before running's elapsed_time

# Stop : Cahnge running False, Stop the running
def stop():
    global running, prev_elapsed_time, elapsed_time
    running = False
    prev_elapsed_time = elapsed_time # prev_elapsed_time is before running's elapsed_time

# Reset : First, running be stop, elapsed time, prev elapsed_time set the 0.0
def reset():
    global running, elapsed_time, prev_elapsed_time
    running = False  # Stop running
    elapsed_time = 0.0       # Reset
    prev_elapsed_time = 0.0  # Reset
    timeText.configure(text=str(elapsed_time)) # Print Reset value : 0.0


running = False             # bool value : if it is run, True, else False
start_time = time.time()    # Save the time value  when clcik 'start'
elapsed_time = 0.0          # Save the elapsed time value. prev elapsed time - now time(when click 'stop')
prev_elapsed_time = 0.0     # Save the time value. that is during 'start' click time to 'stop' click time

# Make screen layout
window = Tk()
window.title("My Simple Stop Watch")
# To Print time Value : increase time value
timeText = Label(window, height = 5, text="0", font=("Arial 40 bold"))
timeText.pack(side = TOP)
# Button : start, stop, reset
startButton = Button(window, width=10, text="Start", bg="green", command=start)
startButton.pack(side = LEFT)
stopButton = Button(window, width=10, text="Stop", bg="red", command=stop)
stopButton.pack(side = LEFT)
resetButton = Button(window, width=10, text="Reset", bg="yellow", command=reset)
resetButton.pack(side = LEFT)

# Application
if __name__ == '__main__':
    runTimer()
    window.mainloop()