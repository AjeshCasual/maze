#modules inclusion
from pyray import *
import random

from raylib.defines import MOUSE_LEFT_BUTTON
from src.maze import *

#variables
backgroundColor  = Color(33,34,44,255)
boxColor         = Color(98,114,164,255)
boxSize          =  10
pointA           = (0, 0)
pointB           = (0, 0)
boxX,boxY        =  80,40
ScreenWidth      = 1280
ScreenHeight     = 720

#basic initiation
set_trace_log_level(LOG_NONE)
init_window(ScreenWidth,ScreenHeight, "Maze Runner")

_mainMenu = ["Game","Settings","About","Quit"]
_levelMenu = ["Game 1","Game 2","Game 3"]
_levelMenuAbout = ["Game 1 instruction","Game 2 instruction","Game 3 instruction"]
_settingMenu = ["Color","Sound","Reset"]
_aboutMenu = ["Ajesh","Gaurangi","Subhranil"]
_aboutMenuAbout = ["Name : Ajesh Sharma\nRegistration Number : RA2211026010383\nContribution : Coding (in Python)",
                  "Name : Gaurangi Rohilla\nRegistration Number : RA2211026010392\nContribution : GUI & Database",
                  "Name : Subhranil Ghosh\nRegistration Number : RA2211026010385\nContribution : Coding (in Java)"]

r = Rectangle(0,0,ScreenWidth,ScreenHeight)
def mainMenu(rec):
    main = Rectangle(0,0,int(rec.width/4),rec.height)
    section = -1
    for i in range(len(_mainMenu)):
        temp = Rectangle(main.x,i*int(main.height/3),main.width,int(main.height/len(_mainMenu))
        if check_collision_point_rec(get_mouse_position(),temp):
            if (is_mouse_button_down(0)):
                draw_rectangle_rec(temp,GREEN)
                i = section
                if section == 1:
                    levelMenu()
                elif section == 2:
                    settingMenu()
                elif section == 3:
                    aboutMenu()
                elif section == 4:
                    quitMenu()
                    
            else:
                draw_rectangle_rec(temp,BLUE)
        else:
            draw_rectangle_rec(temp,RED)

def levelMenu(rec):
    main = Rectangle(int(ScreenWidth/3),0,int(ScreenWidth/3),720)
    for i in range(len(_mainMenu)):
        temp = Rectangle(main.x,i*int(main.height/3),main.width,int(main.height/3))
        if check_collision_point_rec(get_mouse_position(),temp):
            if (is_mouse_button_down(0)):
                draw_rectangle_rec(temp,GREEN)
            else:
                draw_rectangle_rec(temp,BLUE)
        else:
            draw_rectangle_rec(temp,RED)

def settingMenu(rec):
def aboutMenu(rec):
def quitMenu(rec):
        


while not window_should_close():
    begin_drawing()
    mainMenu(r)
    clear_background(backgroundColor)
    end_drawing()
close_window()