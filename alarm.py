#project: LinkedList
#author: Rick Anderson

import Tkinter
import datetime
from Tkinter import *
from threading import Timer
import sys

class alarm:

    def __init__(self):
        self.initGUI()

    def updateTime(self):
        self.text.pack_forget()
        self.text = Text(self.top, height=1)
        self.text.insert(INSERT, "Current Time: ")
        self.currentHour = int(self.getCurrentTime().hour)
        self.currentMin = int(self.getCurrentTime().minute)
        self.text.insert(END, str(self.getCurrentTime().hour) + ":"+str(self.getCurrentTime().minute)+":"+str(self.getCurrentTime().second))
        if hasattr(self, 'setHour') and hasattr(self, 'setMin'):
            self.checkForDone()
        self.text.pack()
        self.t = Timer(1, self.updateTime)
        self.t.start()

    def goOff(self):
        print("Beep beep!")
        sys.stdout.write('\a')
        sys.stdout.flush()

    def checkForDone(self):
        if self.setHour == self.currentHour and self.setMin == self.currentMin:
            self.goOff()

    def setAlarm(self):
        self.setHour = int(self.hourEntry.get())
        self.setMin = int(self.minEntry.get())

        if hasattr(self, 'setText'):
            self.setText.pack_forget()
        if (self.setHour > 23) or (self.setMin > 59):
            self.setText = Text(self.top, height=1)
            self.setText.insert(INSERT, "Invalid entry time!")
            self.setText.pack()
            return
        self.setText = Text(self.top, height = 1)
        self.setText.insert(INSERT, "Set Time: ")
        self.setText.insert(END, self.hourEntry.get() + ":" + self.minEntry.get())
        self.setText.pack()

    def getCurrentTime(self):
        return datetime.datetime.now().time()

    def initGUI(self):
        self.top = Tkinter.Tk()
        set = Tkinter.Button(text ="Set", command = self.setAlarm)
        set.pack(side=BOTTOM)

        hourLabel = Label(self.top, text="Hour")
        hourLabel.pack(side=BOTTOM)
        self.hourEntry = Entry(self.top, bd=1)
        self.hourEntry.pack(side=BOTTOM)

        minLabel = Label(text="Min")
        minLabel.pack(side=BOTTOM)
        self.minEntry = Entry(bd=1)
        self.minEntry.pack(side=BOTTOM)

        self.text = Text(self.top, height = 1)
        self.text.insert(INSERT, "Current Time: ")
        self.text.insert(END, self.getCurrentTime())
        self.text.pack()

        self.t = Timer(1, self.updateTime)
        self.t.start()
        self.top.mainloop()