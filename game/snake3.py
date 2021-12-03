from tkinter import *
from Game import Game, Agent
from geometry import Point2D, Vector2D
import tkinter as tk
import math
import random
import time

class window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Snaker")
        self.geometry('1600x900')
        self.configure(background='green')

    def introduction(self,master):
        intro(master)

class intro(Frame):
    def __init__(self,master):
        Frame.__init__(master)
        self.configure(height=1000,width=800, background='purple',anchor='center')

    

if __name__ == "__main__":
    window = window()
    window.introduction()
    window.mainloop()





