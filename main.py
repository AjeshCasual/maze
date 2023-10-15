#modules inclusion
from pyray import *
import random
from src.maze import *

#variables
backgroundColor  = Color(33,34,44,255)
boxColor         = Color(98,114,164,255)
boxSize          =  10
pointA           = (0, 0)
pointB           = (0, 0)
boxX,boxY        =  80,40

#basic initiation
set_trace_log_level(LOG_NONE)
ScreenWidth,ScreenHeight = 810,410
init_window(ScreenWidth,ScreenHeight, "MapSolver")



a = Maze(boxX,boxY,boxSize)
   

while not window_should_close():
    begin_drawing()
    clear_background(backgroundColor)
    
    #drawPath(path)
    a.draw()
    a.drawDebug()
    '''drawPoint()
    movePoint()
    instruction()'''
    end_drawing()
close_window()