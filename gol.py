#!/usr/bin/env python
import os
import random
from time import sleep
import numpy as np
#get size of terminal

#move to function because, 
grid_x, grid_y = os.popen('stty size', 'r').read().split()

grid_x =(int(grid_x) )
grid_y =(int(grid_y) )



alive="x"
dead=" "











#create create game board function. This one.
def init_board(x,y):
    return np.array(np.array([ a - 90 for a in np.random.randint(1,100, size=(x,y))]).clip(min=0), dtype=bool);



#too many lists
def print_board(grid):
    print('\n'.join(' '.join(map(str, x))  for x in grid).replace("False", dead).replace("True",alive))
    return;


#get ajacent "pixles" from grid.
def get_ajacent(x, y, grid2):
 #if not near zero or upper limmit
  z=[]
  for a in [x-1, x, x+1]:
      for b in [y-1, y, y+1]:
          if not (a == x  and b == y): 
             if not (a >= len(grid2) or b >= len(grid2[a]) ): 
                if not ( a < 0  or b < 0 ) :
                    z.append(grid2[a][b]) 
			  
			  
  return z.count(True); 



def adv_unit(x, y, grid):
    adj=get_ajacent(x, y, grid)
    #if alive, and starving
    if   grid[x][y]  == True and \
     ( adj == 2 or adj == 3 )  : 
         unit = True
    #if dead, but well feed
    elif grid[x][y] == False and adj == 3: 
         unit = True
    else:
         unit = False
    return(unit);

#move forward one frame
def adv_board(grid):
    
    return [[ adv_unit(x,y,grid) for y in range(len(grid[x]))] for x in range(len(grid)) ];






class game_board:
       
    def __init__(self, grid_x, grid_y):
        self.grid = init_board(grid_x, grid_y)
        self.grid_x = grid_x
        self.grid_y = grid_y
    
    def update(self):
        self.grid= adv_board(self.grid)
    
    def print(self):
        print_board(self.grid)







if __name__ == "__main__":
	

 
 game=game_board(grid_x, grid_y)
 

 for x in range(50):
   game.update()
   game.print() 



