from tkinter import *
from tkinter import ttk
import random
import time


#~~~define Constants~~~
#
#DIMENSIONS/SIZES
GAME_WIDTH = 720
GAME_HEIGHT = 720
GRID_WIDTH = 18
GRID_HEIGHT = 18
SQUARE_SIZE = 40
ALL_CELLS =[
  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72,
 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
 91, 92, 93, 94, 95, 96, 97, 98, 99,100,101,102,103,104,105,106,107,108,
109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,
127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,
145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,
163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,
181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,
199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,
217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,
235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,
253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,
271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,
289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,
307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324]


UPPER_BOUNDS  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
BOTTOM_BOUNDS = [307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324]

#COLORS
APPLE_COLOR = '#c20d0a'
SNAKE_COLOR = '#03800d'
GAME_COLOR  = '#000000'

#CELLS/MOVEMENT
SNAKE_START_CELL = 223
APPLE_START_CELL = 228

MOVES = {
    None : 0,
    "right":  1,
    "left" : -1,
    "up"   : -18,
    "down" :  18
    }
CANT_MOVE = {
    None   : 't',
    "right": 'a',
    "left" : 'd',
    "up"   : 's',
    "down" : 'w'
    }
CANT_MOVE_BACK = {
    't' : None,
    'a' : "right",
    'd' : "left",
    's' : "up",
    'w' : "down",
    }


#OTHER 
START_SCORE = 0
SCORE_INCREMENT = 10
DELAY = 8.0

#DEBUG
gameOver = False

#GLOBAL METHODS
def coordtocell(x,y):
    return(y)//40*18 + ((x//40)+1)
def celltocoord(cell):
    #calculates a cells coordinates at it's TOP LEFT corner
    if cell%18 == 0:
        x = 680
    elif cell%18 ==1:
        x = 0
    else: 
        x = (((cell-1)%18)*40)
    if cell in UPPER_BOUNDS:
        y = 0
    elif cell in BOTTOM_BOUNDS:
        y = 680
    else:
        y = (((cell-1)//18)*40)
    return x, y
def check_collision(cell1, cell2):
    if cell1 == cell2:
        return True
    else: 
        return False
def check_wall(cell1):
    x,y = celltocoord(cell1)
    if x >= GAME_WIDTH or x < 0: 
        return True
    if y >= GAME_HEIGHT or y <= 0:
        return True
    else: 
        return False
def cruncher(event):
    root.destroy()
    quit()

#GAME WORLD
class Play:
    def __init__(self,master):
        #Start Canvas
        self.Game = Canvas(
            master,
            height=GAME_HEIGHT,
            width= GAME_WIDTH,
            bg= GAME_COLOR)
        self.Game.grid(in_=master,
                        column=2, 
                        row=1, 
                        sticky='nesw')
        #Bind Keys
        #root.bind_all('<Key>', self.handle_keypress)
        #Game Attributes 
        self.snake_list     = []
        self.snake_location = []
        self.snake_number   = 1        
        self.head           = None
        self.tail           = None
        self.apple          = None
        self.GAME_OVER      = False
        self.score          = START_SCORE

        #Start Game
        snakeHead(self)
        Apple(self)


#GAME LOGIC
    def handle_keypress(self,event):
        if event.char == 'q':
            cruncher(event)
        self.head.handle_keypress(event)


    def clear(self):
        self.Game.delete('all')
    
    def game_over_son(self):
        self.GAME_OVER = True
        print(":(")

#HELPERS 
    def add_me(self, snakePart):
        self.snake_list.append(snakePart)
    def add_location(self, snakePart):
        self.snake_location.append(snakePart.location)
    def new_body(self, tail):
        self.snake_number += 1
        tail.child         = snakeBody(self, tail)
        self.tail          =  tail.child
        self.draw_agent(self.tail)
    def apple_locations(self):
        appleCell = random.choice(ALL_CELLS)
        if appleCell is None or appleCell in self.snake_location:
            return self.apple_locations()
        else:
            return appleCell
#GRAPHICS
    def draw_agent(self,agent):
        x,y = celltocoord(agent.location)
        self.Game.create_rectangle(x,y,x+39,y+39, fill=agent.color)

#UPDATE
    def update(self):
        if self.head.direction is None:
            return
        #UPDATE LOCATIONS
        self.snake_location.clear()
        self.head.update()
        self.clear()
        for snake in self.snake_list:
            self.draw_agent(snake)
        #CHECK 4 COLLISION
        if check_collision(self.head.location, self.apple.location) == True:
            self.apple.eat_me()
            self.new_body(self.tail)
        self.draw_agent(self.apple)

        

        

#SNAKE SUPER CLASS
class Snake:
    def __init__(self, world):
        self.world    = world
        self.color    = SNAKE_COLOR
        self.child    = None
        self.world.tail    = self

#SNAKE HEAD CLASS
class snakeHead(Snake):
    def __init__(self,world):
        super().__init__(world)
        #WHERE
        self.direction = None
        self.location = SNAKE_START_CELL
        self.old_location = 0
        self.world.add_me(self)
        self.world.add_location(self)

        #WHO
        world.head    = self
        world.tail    = self
        #DRAW
        world.draw_agent(self)

#HANDLE KEYPRESS/MOVE
    def handle_keypress(self,event):
        if self.direction is CANT_MOVE_BACK[event.char]:
            return
        else:
            if event.char == 'a':
                self.direction = 'left' 
            if event.char == 'd':
                self.direction = 'right'
            if event.char == 'w':
                self.direction = 'up'
            if event.char == 's':
                self.direction = 'down'
    def move(self):
        self.old_location = self.location
        self.location += MOVES[self.direction]

    def check_wall(self):
        if self.location % 18 == 1 and self.direction == 'left':
            return True
        if self.location % 18 == 0 and self.direction == 'right':
            return True
        if self.location in UPPER_BOUNDS and self.direction == 'up':
            return True
        if self.location in BOTTOM_BOUNDS and self.direction == 'down':
            return True
        return False

#UPDATE - SNAKE HEAD
    def update(self):
        if self.check_wall() is True:
            self.world.game_over_son()
        self.move()
        self.world.add_location(self)
        if self.child is not None:
            self.child.update()

#SNAKE BODY CLASS
class snakeBody(Snake):
    def __init__(self, world, parent):
        super().__init__(world)
        self.parent = parent
        self.parent.child = self
        self.location = self.parent.old_location
        self.old_location = 0
        self.world.add_me(self)
        self.world.add_location(self)

#UPDATE - SNAKE BODY
    def update(self):
        self.old_location = self.location
        self.location = self.parent.old_location
        if check_collision(self.world.head.location,self.location) is True:
            self.world.game_over_son()
        self.world.add_location(self)
        if self.child is not None:
            self.child.update()


class Apple:
    def __init__(self, world):
        world.apple   = self
        self.world    = world
        self.color    = APPLE_COLOR
        self.location = APPLE_START_CELL
        self.old_location = 0
        world.draw_agent(self)

    def eat_me(self):
        self.old_location = self.location
        self.location = self.world.apple_locations()
        self.world.score += SCORE_INCREMENT
        self.world.draw_agent(self)


#TEMP CODE
if __name__ =='__main__':
    root = Tk()
    root.title('Snake!')
    root.geometry('1600x900')
    gamer = Play(master=root)
    root.bind_all('<Key>', gamer.handle_keypress)
    while not gamer.GAME_OVER:
        gamer.update()
        time.sleep(1.0/DELAY)
        root.update()
    root.update()
