from tkinter import *
from tkinter import ttk
from Game import Game, Agent
from geometry import Bounds
import math
import random
import time

class mainFrame(Frame):
    def __init__ (self, master):
        ttk.Frame.__init__(self,master)
        self.gameOver= False
        self.grid()
        self.configure(height=1600,width=900)

    def killer(self,event):
        if event.char=='q':
            self.gameOver= True


class playSnake:
    def __init__(self,master):
        self.Game= Canvas(master)
        self.Game.configure(height=720,width=1280)
        self.Game.grid(column=1, row=1,rowspan=2,columnspan=2)


    def draw(self,event):
        pass

if __name__ =='__main__':
    w = Toplevel(master=None)
    w.geometry('1600x900')
    mained=mainFrame(w)   
    playSnake(master=mained)  
    while not mained.gameOver:
        time.sleep(1.0/60.0)
        mained.mainloop()
