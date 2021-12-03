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
        self.topology = topology

        # Populate the world with creatures
        self.agents = []
        self.GAME_OVER = False

        # Initialize the graphics window.
        self.root = Tk()
        self.root.title(name)
        self.content = Frame.__init__(self, self.root, width=1600,height=900)
        self.canvas = Canvas(self.content, width=1280, height=700,offset='nw')
        self.canvas.configure(background='purple')

        # Handle mouse pointer motion and keypress events.
        self.mouse_position = Point2D(0.0,0.0)
        self.mouse_down     = False
        self.bind_all('<Motion>',self.handle_mouse_motion)
        self.canvas.bind('<Button-1>',self.handle_mouse_press)
        self.canvas.bind('<ButtonRelease-1>',self.handle_mouse_release)
        self.bind_all('<Key>',self.handle_keypress)

    def handle_keypress(self, event):
        Game.handle_keypress(self,event)
        if event.char == '<up>':
            pass
        elif event.char == '<down>':
            pass
        elif event.char == '<left>':
            pass
        elif event.char == '<right>':
            pass
        elif event.char == '<space>':
            pass

    def reset(self,event):
        pass


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

# Open
# Info
##In Game
game = PlaySnake("Snake!", 1600, 900, 1600, 900, topology='bound')
snakey = Canvas(game.content, width=1600, height=320)
scorer = Canvas(game.content, width=200, height=900)
game.canvas.grid(column=1,row=1,columnspan=2, rowspan=2, sticky='NW')
snakey.grid(column=1,row=3,columnspan=3,sticky='S')
scorer.grid(column=3,row=1,sticky='NE')
while not game.GAME_OVER:
    time.sleep(1.0/60.0)
    game.update()

# Gameover

#HiScore