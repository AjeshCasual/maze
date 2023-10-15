from astar.search import AStar
class Astar:
    def __init__(self,pointA,pointB):
        self.a
        self.b
        self.path
    def position(self,A,B):
        self.a = A
        self.b = B
    def path(self,maze):
        self.path = AStar(maze).search(self.a,self.b)    