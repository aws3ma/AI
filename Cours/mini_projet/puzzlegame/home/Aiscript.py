from copy import deepcopy
import numpy as np
import math
class Taquin:
    def __init__(self,br):
        self.br=br
        
        
        DIRECTIONS = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}
        self.goal=[]
        self.makegoal()
    def makegoal(self):
        br=deepcopy(self.br)
        for k in range(len(br)):
            for i in range(len(br)):
                l=[]
                lindex_min=0
                cindex_min=0
                minn=math.inf
                maxx=-math.inf

                for n in range(len(br)):
                    if(minn>min(br[n])):
                        lindex_min=np.argmin(br[n])
                        cindex_min=n
                        minn=min(br[n])
                    if(maxx<min(br[n])):
                        maxx=max(br[n])
                br[cindex_min][lindex_min]=maxx
                l.append(minn)
                
            self.goal.append(l)

        print(self.goal)
        print(self.br)
br = [[8, 7, 0],
               [2, 4, 6],
               [1, 5, 3]]
t= Taquin(br)