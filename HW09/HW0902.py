# HW0902.py
"""
Project : Distance convert program
Author: Eun-seong Choi
Date of last update: 2022 / 11 / 09
Update list:
    - v1.1 : 11 / 09
        Make class : DistanceConvert
        Add Component : Entry(km, Mile), Label(km, Mile),
                        Button(Km to Mile. Mile to Km)
        Define Command : Km_to_Mile, Mile_to_Km
"""
from math import *
from tkinter import *


class DistanceConvert:
    def __init__(self, master):
        L_frame = Frame(master)
        L_frame.grid(row=0, column=0)  # L_frame = left of Frame
        R_frame = Frame(master)
        R_frame.grid(row=0, column=1)  # R_frame = right of Frame

        # Km Entry, Label -> L_frame = masterFrame(0,0)
        self.Km_var = DoubleVar()
        Entry(L_frame, textvariable=self.Km_var).grid(row=0, column=0)
        Label(L_frame, text='Km').grid(row=0, column=1)

        # Mile Entry, Label -> R_frame = masterFrame(0,1)
        self.Mile_var = DoubleVar()
        Entry(R_frame, textvariable=self.Mile_var).grid(row=0, column=0)
        Label(R_frame, text='Mile').grid(row=0, column=1)

        # Km_to_Mile button -> masterFarme(1,0)
        Km_to_Mile_button = Button(
            master, text='km -> Mile', command=self.Km_to_Mile)
        Km_to_Mile_button.grid(row=1, column=0)
        # Mile_to_Km button -> masterFarme(1,1)
        Mile_to_Km_button = Button(
            master, text='Mile -> Km', command=self.Mile_to_Km)
        Mile_to_Km_button.grid(row=1, column=1)

    # Convert : Km to Mile
    def Km_to_Mile(self):
        Km = self.Km_var.get()
        Mile = Km / 1.60934  # 1Km = 1.60934Mile, Mile = 1Km/1.60934
        Mile = round(Mile, 3)
        self.Mile_var.set(Mile)

    # Convert : Mile to Km
    def Mile_to_Km(self):
        Mile = self.Mile_var.get()
        Km = Mile * 1.60934  # 1Km = 1.60934Mile, 1Mile = 1.6093Km
        Mile = round(Mile, 3)
        self.Km_var.set(Km)


window = Tk()
window.wm_title('Distance Convert')
DistanceConvert(window)
window.mainloop()
