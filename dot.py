from time import sleep
import curses 

scr = curses.initscr()
curses.noecho()
scr.nodelay(True)

y = 10
x = 6
dx = 1
go = 1
while True:
    c = scr.getch()
    if c == ord('a'):
        dx = -1
    elif c == ord('s'):
        dx = +1
    elif c == ord(' '):
        go = (1-go)
    elif c == ord('q'):
        break
    x += go * dx
    if x > 40:
        x = 40
        dx *= -1
    elif x < 4:
        x = 4
        dx *= -1
    scr.clear()
    scr.addch(y, 3, ord('['))
    scr.addch(y, x, ord('o'))
    scr.addch(y, 41, ord(']'))
    scr.move(0,0)
    scr.refresh()
    sleep(0.1)
    
