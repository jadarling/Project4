from tkinter import *
from tkinter import ttk
from Game import Game, Agent
from geometry import Bounds
import math
import random
import time

window = Tk()
window.title("Snake")

class PlaySnake(Game):
    def __init__(self):
        pass

#Intro Screen
Intro = Frame(window, height=900, width=1600, background='purple')
