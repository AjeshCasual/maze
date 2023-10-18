# map is with 0s and 1s for walls and clear path
# info is with 1,2,3,4 for different shapes
from pyray import *
import random
import src.menu
src.menu.ColorF


class Maze:
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.size = size
        self.info = []
        self.createInfo()
        self.map = []
        self.translateInfo()
    # 4 3 2 1

    def draw(self):
        for i in range(self.y + 1):
            for j in range(self.x + 1):
                if self.map[i][j]:
                    if (is_key_down(KEY_SPACE)):
                        draw_rectangle_lines(j*self.size, i*self.size, self.size, self.size, src.menu.ColorF)
                    else:
                        draw_rectangle(j*self.size, i*self.size, self.size, self.size, src.menu.ColorF)
                    
    def regen(self,x,y,size):
        self.x = x
        self.y = y
        self.size = size
        self.createInfo()
        self.translateInfo()
                        
    def createInfo(self):
        self.info = []
        for i in range(int(self.y/2)):
            temp = []
            for j in range(int(self.x/2)):
                temp.append(1)
            self.info.append(temp)
    
        for i in range(int(self.y/2)):
            self.info[i][int(self.x/2) - 1] = 2
        tablet = []
        for k in range(1,int(self.y/2)):
            for i in range(int(self.x/2)):
                if i != int(self.x/2) - 1:
                    if random.randint(1, 2) != 1:
                        tablet.append([k,i])
                    else:
                        self.info[k][i] = 2
                        tablet.append([k,i])
                        test = random.randint(0, len(tablet) - 1)
                        if self.info[tablet[test][0] - 1][tablet[test][1]] == 1:
                            self.info[tablet[test][0] - 1][tablet[test][1]] = 3
  
                        if self.info[tablet[test][0] - 1][tablet[test][1]] == 2:
                            self.info[tablet[test][0] - 1][tablet[test][1]] = 4
  
                        tablet = []
                else:

                    tablet.append([k,i])
  
                    test = random.randint(0, len(tablet) - 1)
                    if self.info[tablet[test][0] - 1][tablet[test][1]] == 1:
                        self.info[tablet[test][0] - 1][tablet[test][1]] = 3

                    if self.info[tablet[test][0] - 1][tablet[test][1]] == 2:
                        self.info[tablet[test][0] - 1][tablet[test][1]] = 4

                    tablet = []
    # 4 3 2 1 into 0s and 1s
    def translateInfo(self):
        self.map = []
        for i in range(int(self.y)):
            temp = []
            for j in range(int(self.x)):
                temp.append(0)
            self.map.append(temp)
        for k in range(int(self.y/2)):
            for i in range(int(self.x/2)):
                if self.info[k][i] == 1:
                    self.map[k*2 + 1][i*2]     = 1
                    self.map[k*2 + 1][i*2 + 1] = 1
                if self.info[k][i] == 2:
                    self.map[k*2 + 1][i*2]     = 1
                    self.map[k*2 + 1][i*2 + 1] = 1
                    self.map[k*2]    [i*2 + 1] = 1
                if self.info[k][i] == 4:
                    self.map[k*2 + 1][i*2 + 1] = 1
                    self.map[k*2]    [i*2 + 1] = 1
        for i in range(int(self.y)):
            self.map[i].insert(0,1)
        temp = []
        for i in range(int(self.x) + 1):
            temp.append(1)
        self.map.insert(0,temp)
     
    def drawDebug(self):
        for i in range(int(self.y/2)):
            for j in range(int(self.x/2)):
                draw_text(f"{self.info[i][j]}",int((j+0.5)*self.size*2),int((i+0.5)*self.size*2),self.size*2,WHITE)
                
    