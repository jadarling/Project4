from tkinter import *
from tkinter import Image
import tkinter as tk 
from Game import Game, Agent
from geometry import Point2D, Vector2D

import math
import random
import time

def moveOn(event, frame):
    if event.char == 'event':
        frame.clear()
        event += 1
    
class masterWindow(tk.Tk):
    def __init__(self, name, *args, **kwargs):
        tk.Tk.__init__(self, *args,**kwargs)
        self.root = Tk()
        self.root.title(name)
        Frame.__init__(self, self.root)
class framer(Frame):
    def __init__(self,*args,**kwargs):
        Frame.__init__(self,*args,**kwargs)

class playSnake(Game):
    pass
class openScreen(tk.Canvas):
    def __init__(self, parent):
        tk.Canvas.__init__(self,parent)
        Label(master=self,text="gaming",anchor='n')
        self.pack()
class tutorial:
    pass
class gameOver:
    pass

mastery = masterWindow('mastery')
openframe = framer(master=mastery, name='openframe',width=1600,height=900)
openScreen(openframe)
mastery.mainloop()

