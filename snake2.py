from tkinter import *
from tkinter import ttk
from Game import Game, Agent
from geometry import Bounds

import threading
import math
import random
import time
# define bounds
topBounds = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
botBounds = [307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324]
#App destroy command
def cruncher(event):
    root.destroy()
    quit()

def move_on(event, frame):
    for widget in frame.winfo_children():
        widget.destroy()
    
#The 'mainframe'
class mainFrame(Frame):
    def __init__ (self, master):
        Frame.__init__(self,master)
        self.configure(height=1600,width=900,background='#476042')
        self.pack(in_=master)
        self.gameOver = False

#the Game
class playSnake:
    def __init__(self,master):
        self.master = master
        self.Game= Canvas(master)
        self.Game.configure(height=720,width=720,bg='#6A7B76')
        self.Game.grid(in_=master,column=2, row=1, sticky='nesw')

        self.agents = []
        self.numberOfRow=18
        self.numberOfCol=18
        self.ticks_before_start=100
        self.score=0
        self.snake = snakeHead(self,124)

# Canvas Functions 
    def clear(self):
        self.Game.delete('all')
# Grid Functions
    def draw_grid(self):
        for x in range(40,720,40):
            self.Game.create_line(x,0,x,720, fill='#476042')
        for y in range(40,720,40):
            self.Game.create_line(0,y,720,y, fill='#476042')
    def coordtocell(self,x,y):
        return(y-40)//40*18 + (x//40)
    def celltocoord(self, cell):
        if cell%18 == 0:
            x = 720
        elif cell%18 ==1:
            x = 40
        else: 
            x = (cell%18)*40
        if cell in topBounds:
            y = 40
        elif cell in botBounds:
            y = 720
        else:
            y = ((cell//18)+1)*40
        return x, y
# Agent Stuff
    def draw_agent(self, agent):
        x,y = self.celltocoord(agent.cell)
        self.Game.create_rectangle(x-40,y-40,x,y, fill=agent.color)

    def add(self, agent):
        self.agents.append(agent)

# Game Logic 
    def handle_keypress(self,event):
        if event.char == 'q':
            cruncher(event)
        self.snake.handle_keypress(event)
    def game_over(self):
        self.clear()
        mained.gameOver = True
        print("You lost :(")

    def update(self):

        if self.snake.direction == None:
            pass
        self.clear()
        for agent in self.agents:
            self.draw_agent(agent)
        self.Game.update()


#the Snake bits
class snake:
    def __init__(self, world):
        self.cell=0
        self.world=world 
        self.world.add(self)
        self.ticks=0
        self.color='#03800d'
    def update(self):
        pass
class snakeBody(snake):
    def __init__(self,world,parent, head):
        snake.__init__(self,world)
        self.parent = parent
        self.child = None
        self.cell = self.parent.child
        self.parent.child = self
        self.is_tail = True
        self.head = head
        self.head.body.append(self.cell)
        
    
    def update(self):
        self.ticks+=1
        self.child = self.cell
        self.cell = self.parent.cell
        if self.child == type(int):
            self.is_tail = True
        else:
            self.is_tail = False


class snakeHead(snake):
    def __init__(self,world,cell):
        snake.__init__(self,world)
        self.world = world
        self.color='#233DFF'
        self.parent=None
        self.child = self.cell
        self.direction=None
        self.body = []
        self.cell = cell
        self.speed= 1/4
        self.world.draw_agent(self)
     
    
    def add(self, bit):
        self.body.append(bit)

    def checkHit(self):
        if self.cell%18 == 1 and self.direction == 'left':
            Tk.after(self.world,ms=20, func=self.world.game_over())
        elif self.cell%18 == 0 and self.direction == 'right':
            Tk.after(self.world,ms=20, func=self.world.game_over())
        elif self.cell in topBounds and self.direction == 'up':
            Tk.after(self.world,ms=20, func=self.world.game_over())
        elif self.cell in botBounds and self.direction == 'down':
            Tk.after(self.world,ms=20, func=self.world.game_over())
        for body in self.body:
            if body == type(int):
                if self.cell == body:
                    Tk.after(self.world,ms=20, func=self.world.game_over())
            if self.cell == body.cell:
                Tk.after(self.world,ms=20, func=self.world.game_over())

    def handle_keypress(self,event):
        if event.char == 'a':
            self.direction = 'left'
            
            print(self.direction)
            print(self.cell)
        if event.char == 'd':
            self.direction = 'right'
            
            print(self.direction)
            print(self.cell)
        if event.char == 'w':
            self.direction = 'up'
            
            print(self.direction)
            print(self.cell)
        if event.char == 's':
            self.direction = 'down'
            
            print(self.direction)
            print(self.cell)
#Movement Functions
    def moveUp(self):
        if self.checkHit() == False: 
            pass
        else:    
            self.cell -= 18
    def moveDown(self):
        if self.checkHit() == False: 
            pass
        else:    
            self.cell += 18
    def moveLeft(self):
        if self.checkHit() == False: 
            pass
        else:    
            self.cell -= 1
    def moveRight(self):
        if self.checkHit() == False: 
            pass
        else:    
            self.cell += 1

    def update(self):
        for body in self.body:
            if body is not type(int):
                body.update()
        self.ticks+=1
        if self.direction == 'left':
            self.moveLeft()
        if self.direction == 'right':
            self.moveRight()
        if self.direction == 'up':
            self.moveUp()
        if self.direction == 'down':
            self.moveDown()
        for body in self.body:
            pass

    

#The Apple
class apple:
    def __init__(self,world,position):
        self.position= position
        self.world=world
        self.world.add(self)
        self.ticks=0
        self.color= '#c20d0a'
        self.cell= 153
    def update(self):
        pass

#Running the Game
if __name__ =='__main__':
    root = Tk()

    root.title('Snake!')
    root.geometry('1600x900')
    mained=mainFrame(root)
    gamer = playSnake(master=mained)
    root.bind_all('<Key>',gamer.handle_keypress)
    while not mained.gameOver:
        gamer.update()
        gamer.snake.update()
        time.sleep(12.0/60.0)

