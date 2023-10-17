#modules inclusion
from pyray import *
import random
from raylib.defines import MOUSE_LEFT_BUTTON
import src.maze
import src.menu
#variables
ScreenWidth      = 1280
ScreenHeight     = 720

#basic initiation
set_trace_log_level(LOG_NONE)
init_window(ScreenWidth,ScreenHeight, "Maze Runner")
set_target_fps(120)

a = src.maze.Maze(30,30,20)

while not window_should_close():
    begin_drawing()
    src.menu.mainMenu()
    #a.draw()
    #a.drawDebug()
    clear_background(src.menu.ColorB)
    end_drawing()
close_window()