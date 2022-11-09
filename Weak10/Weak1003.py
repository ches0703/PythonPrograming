# Simple tkinter GUI for Temperature Converter
from math import *
from tkinter import *

class TempConvert:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.c_var = DoubleVar()
        Entry(frame, textvariable=self.c_var).grid(row=0, column=1)
        Label(frame, text='Km').grid(row=0, column=2)

        self.result_var = DoubleVar()
        Entry(frame, textvariable=self.result_var).grid(row=0, column=3)
        Label(frame, text='Mile').grid(row=0, column=4)

        K_to_M_button = Button(frame, text='k - M', command=self.convert)
        K_to_M_button.grid(row=2, column= 0)

        M_to_K_button = Button(frame, text='M - K', command=self.convert)
        M_to_K_button.grid(row=2, column= 1)
        

    def convert(self):
        c = self.c_var.get()
        f = c * 1.8 + 32
        f_round = round(f, 3)
        self.result_var.set(f_round)


window = Tk()
window.wm_title('Temp Converter')
app = TempConvert(window)
window.mainloop()
