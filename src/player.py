from astar.search import AStar
from pyray import *
import random
import src.menu
class Player:
    def __init__(self,arr,size):
        self.x = 1
        self.y = 1
        self.arr = arr
        self.size = size
        self.timer = 0.05
        self.dt = 0
        
    def move(self):
        if is_key_down(KEY_RIGHT_SHIFT) or is_key_down(KEY_LEFT_SHIFT):
            self.timer = 0.15
        else:
            self.timer = 0.05
        self.dt += get_frame_time()
        if self.dt > self.timer:
            if is_key_down(KEY_DOWN):
                if self.arr[self.y + 1][self.x] != 1 and self.y != len(self.arr):
                    self.y += 1
            if is_key_down(KEY_UP):
                if self.arr[self.y - 1][self.x] != 1 and self.y != 0:
                    self.y -= 1
            if is_key_down(KEY_RIGHT):
                if self.arr[self.y][self.x + 1] != 1 and self.x != len(self.arr[0]):
                    self.x += 1
            if is_key_down(KEY_LEFT):
                if self.arr[self.y][self.x - 1] != 1 and self.y != 0:
                    self.x -= 1
            self.dt = 0
    def something(self):
        self.x = 1
        self.y = 1
           
    def draw(self):
        draw_rectangle(self.x*self.size + int(self.size/4), self.y*self.size + int(self.size/4), int(self.size/2), int(self.size/2), WHITE)
        
class Enemy:
    def __init__(self,player,maze):
        self.x = 2
        self.y =2
        self.maze = maze
        self.size = maze.size
        self.timer = 0.5
        self.dt = 0.1
        self.player = player
        self.points = 0
        self.gx,self.gy = self.x,self.y
        self.regen = False
    def move(self):
        
        nex = AStar(self.maze.map).search((self.y,self.x),(self.player.y,self.player.x))
        self.dt += get_frame_time()
        if self.dt > self.timer:
            self.dt = 0
            if (len(nex)) > 1:
                self.x = nex[1][1]
                self.y = nex[1][0]
        draw_rectangle(nex[0][1]*self.maze.size,nex[0][0]*self.maze.size,self.maze.size,self.maze.size,RED)
        
        if self.x == self.player.x and self.y == self.player.y:
            src.menu.needMenu = True
        if self.player.x == self.gx and self.player.y == self.gy:
            self.regen = True
        draw_rectangle(self.gx*self.size + int(self.size/4), self.gy*self.size + int(self.size/4), int(self.size/2), int(self.size/2), WHITE)

        
            
                
        
    def create(self,player,maze):
        
        self.maze = maze
        self.size = maze.size
        self.player = player
        self.x = random.randint(1,len(self.maze.map[0]) - 2)
        self.y = random.randint(1,len(self.maze.map) - 2)
        self.gx,self.gy = self.x,self.y
        if self.maze.map[self.y][self.x] == 1:
            self.create(self.player,self.maze)
        
