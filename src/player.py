from curses import KEY_LEFT, KEY_RIGHT
from pyray import *
class player:
    def __init__(self,arr,size):
        self.x = 1
        self.y = 1
        self.arr = arr
        self.size = size
    def move(self):
        if is_key_pressed(KEY_DOWN):
            if arr[self.y + 1][self.x] != 1 and x != len(self.arr):
                self.y += 1
        elif is_key_pressed(KEY_UP):
            self.y -= 1
        elif is_key_pressed(KEY_RIGHT):
            self.x += 1
        elif is_key_pressed(KEY_LEFT):
            self.x -= 1
           
    def draw(self):
        draw_rectangle(x*self.size + int(self.size/4), y*self.size + int(self.size/4), int(self.size/2), int(self.size/2), WHITE)