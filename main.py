#modules inclusion
from pyray import *
import random
import src.maze
import src.menu
import src.player
#variables
ScreenWidth      = 1280
ScreenHeight     = 720
#basic initiation
set_trace_log_level(LOG_NONE)
init_window(ScreenWidth,ScreenHeight, "Maze Runner")
set_target_fps(120)
#variable
a = src.maze.Maze(90,46,14)
b = src.player.Player(a.map,14)
c = src.player.Enemy(b,a)
while not window_should_close():
    begin_drawing()
    if src.menu.needMenu:
        src.menu.mainMenu()
        if src.menu.levelSection == 0:
            a.regen(90,46,14)
            b = src.player.Player(a.map,a.size)
            c.create(b,a)
        elif src.menu.levelSection == 1:
            a.regen(40,20,30)
            b = src.player.Player(a.map,a.size)
            c.create(b,a)
        elif src.menu.levelSection == 2:
            a.regen(20,21,12)
            b = src.player.Player(a.map,a.size)
    else:
        if src.menu.levelSection == 0:
            a.draw()
            #a.drawDebug()
            b.move()
            b.draw()
            c.move()
            if c.regen == True:
                c.regen = False
                src.menu.level1Score += 1
                a.regen(90,46,14)
                b.something()
                c.create(b,a)
        elif src.menu.levelSection == 1:
            a.draw()
            #a.drawDebug()
            b.move()
            b.draw()
            c.move()
            if c.regen == True:
                c.regen = False
                src.menu.level1Score += 1
                a.regen(40,20,30)
                b.something()
                c.create(b,a)
    clear_background(src.menu.ColorB)
    end_drawing()
close_window()

