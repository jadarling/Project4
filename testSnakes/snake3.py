from tkinter import *
from tkinter import ttk
from tkinter import font
from Game import Game, Agent
from geometry import Point2D, Vector2D
import tkinter as tk
import math
import random
import time


root= Tk()
GAMED_OVER = False
root.title='snake'
mainframe=ttk.Frame(root,name='snake')
mainframe.configure(
    width=1600,
    height=900,
    borderwidth=10,
)
mainframe.grid(column=1,row=1,sticky=('N E S W'))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


class intro(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master,class_='intro')
        self.configure(height=1600,width=900, background='purple')
        self.pack()
        label = ttk.Label(master=self,class_='intro', text="fuck you")
        label.configure(background='green',
        anchor='center')
        label.pack()
    def handle_keypress(self,event):
        pass

        


    
while __name__=="__main__":
    root= Tk()
    root.title='snake'
    mainframe=ttk.Frame(root,name='snake')
    mainframe.configure(
        width=1600,
        height=900,
        borderwidth=10,
    )
    mainframe.grid(column=1,row=1,sticky=('N E S W'))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    intro(root)
root.mainloop()




