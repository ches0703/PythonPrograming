import turtle
from tkinter import *
import time
Disk_thickness = 30
Canvas_Width = 300
Canvas_Height = 300
Colors = ["black", "red", "green", "blue", "orange", "yellow", "purple"]


class Disk(object):
    def __init__(self, size, length, color):
        self.diameter = size
        self.length = length
        self.color = color

    def setTower(self, tower):
        self.tower = tower

    def __str__(self):
        return "Disk_{:>3}".format(self.diameter)


class Tower(object):
    def __init__(self, name, canvas, cv_id):
        self.name = name
        self.disks = []
        self.canvas = canvas
        self.cv_id = cv_id

    def addDisk(self, disk):
        self.disks.append(disk)

    def getLength(self):
        return len(self.disks)

    def top(self):
        if len(self.disks) <= 0:
            return None
        disk = self.disks[-1]
        if disk is None:
            return None
        else:
            return disk.diameter

    def pop(self):
        if len(self.disks) > 0:
            disk = self.disks[-1]
            self.disks.pop(-1)
            return disk
        else:
            return None

    def drawTower(self):
        cv = self.canvas
        x0 = Canvas_Width // 2
        y0 = Canvas_Height - 50
        # print("{} is drawing disks with x0({}), y0({})"\
        # .format(self.name, x0, y0), end=' ')
        for i in range(len(self.disks)):
            disk = self.disks[i]
            if disk is None:
                continue
            # print("{}".format(disk.diameter), end= ' ')
            cv.create_rectangle(x0 - disk.diameter // 2, y0 - i * disk.length,
                                x0 + disk.diameter // 2, y0 - (i + 1) * disk.length, fill=disk.color)
        # print()

    def __str__(self):
        r_str = ""
        r_str += self.name + " : "
        if len(self.disks) <= 0:
            r_str += "Empty"
            return r_str
        for i in range(len(self.disks)):
            disk = self.disks[i]
            if disk is None:
                continue
        r_str += str(self.disks[i].diameter) + " "
        return r_str


def HanoiTower(n, tower_from, tower_tmp, tower_to):
    global Tower_1, Tower_2, Tower_3, window
    if (n == 1):
        if tower_from.getLength() > 0:
            disk = tower_from.pop()
            tower_to.addDisk(disk)
            disk.setTower(tower_to)
        print("{} is moved from({}) to({})"
              .format(disk, tower_from.name, tower_to.name))
        # print(Tower_1); print(Tower_2); print(Tower_3)
        tower_from.canvas.delete("all")
        tower_from.drawTower()
        tower_to.canvas.delete("all")
        tower_to.drawTower()
        tower_from.canvas.update()
        tower_to.canvas.update()
        time.sleep(1)
    else:
        HanoiTower(n - 1, tower_from, tower_to, tower_tmp)
        if tower_from.getLength() > 0:
            disk = tower_from.pop()
            tower_to.addDisk(disk)
            disk.setTower(tower_to)
        print("{} is moved from({}) to({})"
              .format(disk, tower_from.name, tower_to.name))
        # print(Tower_1); print(Tower_2); print(Tower_3)
        tower_from.canvas.delete("all")
        tower_from.drawTower()
        tower_to.canvas.delete("all")
        tower_to.drawTower()
        tower_from.canvas.update()
        tower_to.canvas.update()
        time.sleep(1)
        HanoiTower(n - 1, tower_tmp, tower_from, tower_to)


def initHanoiTower(n):
    global Tower_1, Tower_2, Tower_3, window
    window = Tk()
    window.title("Hanoi Tower with {} disks".format(n))
    canvas_1 = Canvas(window, bg="light blue",
                      width=Canvas_Width, height=Canvas_Height)
    canvas_1.pack(side="left")
    canvas_2 = Canvas(window, bg="light blue",
                      width=Canvas_Width, height=Canvas_Height)
    canvas_2.pack(side="left")
    canvas_3 = Canvas(window, bg="light blue",
                      width=Canvas_Width, height=Canvas_Height)
    canvas_3.pack(side="left")
    Tower_1 = Tower("Tower_1", canvas_1, 1)
    Tower_2 = Tower("Tower_2", canvas_2, 2)
    Tower_3 = Tower("Tower_3", canvas_3, 3)
    for i in range(n, 0, -1):
        disk = Disk(i * Canvas_Width // 10, Disk_thickness,
                    Colors[i % len(Colors)])
        Tower_1.addDisk(disk)


num_disks = 7
if __name__ == "__main__":
    # time.sleep(5)
    initHanoiTower(num_disks)
    HanoiTower(num_disks, Tower_1, Tower_2, Tower_3)
