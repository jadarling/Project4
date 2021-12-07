from tkinter import *
from tkinter import ttk
from Game import Game, Agent
from geometry import Bounds
import math
import random
import time
#App destroy command
def cruncher(event):
    root.destroy()
#The 'mainframe'
class mainFrame(Frame):
    def __init__ (self, master):
        Frame.__init__(self,master)
        self.configure(height=1600,width=900,background='#476042')
        self.grid()
        self.gameOver = False

#the Game
class playSnake:
    def __init__(self,master):
        self.Game= Canvas(master)
        self.Game.configure(height=720,width=1280,bg='purple')
        self.Game.grid(column=1, row=1,rowspan=2,columnspan=2,sticky='NW')
        self.Game.bind_all('<Key>',self.handle_keypress)

    def init_grid(self):
        for x in range(40,1280,40):
            self.Game.create_line(x,0,x,720, fill='#476042')
        for y in range(40,1280,40):
            self.Game.create_line(0,y,1280,y, fill='#476042')
    def handle_keypress(self,event):
        if event.char == '<KP_left>':
            self.init_grid()
        if event.char == '<KP_left>':
            pass
        if event.char == '<KP_left>':
            pass
        if event.char == '<KP_left>':
            pass  
    def draw(self,event):
        pass
    def update(self):
        pass
#the Snake bits

#The Apple

if __name__ =='__main__':
    root = Tk()
    root.bind_all('<q>',cruncher)
    root.title('Snake!')
    root.geometry('1600x900')
    mained=mainFrame(root)
    gamer = playSnake(master=mained)
    gamer.init_grid()

    while not mained.gameOver:
        time.sleep(1.0/60.0)
        mained.mainloop()
