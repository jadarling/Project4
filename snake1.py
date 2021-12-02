#          _                 _                   _                   _                 _      
#         / /\              /\ \     _          / /\                /\_\              /\ \    
#        / /  \            /  \ \   /\_\       / /  \              / / /  _          /  \ \   
#       / / /\ \__        / /\ \ \_/ / /      / / /\ \            / / /  /\_\       / /\ \ \  
#      / / /\ \___\      / / /\ \___/ /      / / /\ \ \          / / /__/ / /      / / /\ \_\ 
#      \ \ \ \/___/     / / /  \/____/      / / /  \ \ \        / /\_____/ /      / /_/_ \/_/ 
#       \ \ \          / / /    / / /      / / /___/ /\ \      / /\_______/      / /____/\    
#   _    \ \ \        / / /    / / /      / / /_____/ /\ \    / / /\ \ \        / /\____\/    
#  /_/\__/ / /       / / /    / / /      / /_________/\ \ \  / / /  \ \ \      / / /______    
#  \ \/___/ /       / / /    / / /      / / /_       __\ \_\/ / /    \ \ \    / / /_______\   
#   \_____\/        \/_/     \/_/       \_\___\     /____/_/\/_/      \_\_\   \/__________/   
#                                                             

from tkinter import *
from Game import Game, Agent
from geometry import Point2D, Vector2D, Bounds
import math
import random
import time

#Game Class

class PlaySnake(Game):

    def __init__(self, name, w, h, ww, wh, topology ='bound',console_lines=0):

        self.WINDOW_WIDTH = ww
        self.WINDOW_HEIGHT = wh
        self.bounds = Bounds(-w/2,-h/2,w/2,h/2)
        self.topology = topology

        # Populate the world with creatures
        self.agents = []
        self.GAME_OVER = False

        # Initialize the graphics window.
        self.root = Tk()
        self.root.title(name)
        self.content = Frame.__init__(self, self.root, width=1600,height=900)
        self.canvas = Canvas(self.content, width=1280, height=700,background='gray75',offset='nw')
        self.snakey = Canvas(self.content, width=1600, height=320)
        self.scorer = Canvas(self.content, width=200, height=900)
        self.canvas.grid(column=1,row=1,sticky='NW')
        self.snakey.grid(column=1,row=2,columnspan=2,sticky='NE')
        self.scorer.grid(column=2,row=1,sticky='S')




        # Handle mouse pointer motion and keypress events.
        self.mouse_position = Point2D(0.0,0.0)
        self.mouse_down     = False
        self.bind_all('<Motion>',self.handle_mouse_motion)
        self.canvas.bind('<Button-1>',self.handle_mouse_press)
        self.canvas.bind('<ButtonRelease-1>',self.handle_mouse_release)
        self.bind_all('<Key>',self.handle_keypress)




#Snake agent (Snake and Head/Body subclasses)
class Snake(Agent):
    
    pass
class snakeHead(Snake):
    pass
class snakeBody(Snake):
    pass
#Apple Agent 
class Apple(Agent):
    pass


game = PlaySnake("Snake!", 1600, 900, 1600, 900, topology='bound')

while not game.GAME_OVER:
    time.sleep(1.0/60.0)
    game.update()