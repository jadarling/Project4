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
from geometry import Point2D, Vector2D
import math
import random
import time

#Game Class
class PlaySnake(Game):

    def __init__(self):
        Game.__init__(self,"Snake",60.0,33.75,1600,900, topology='bound', console_lines=6)

        self.report("SnakeSnakeSnakeSnakeSnake")


#Snake agent
class Snake(Agent):
    
    pass
class snakeHead(Snake):
    pass
class snakeBody(Snake):
    pass
#Apple Agent 
class Apple(Agent):
    pass


game = PlaySnake()
while not game.GAME_OVER:
    time.sleep(1.0/60.0)
    game.update()