#!/usr/bin/python3
import os
import random
from time import sleep
import numpy as np
#get size of terminal
rows, columns = os.popen('stty size', 'r').read().split()

rows =(int(rows) )
columns =(int(columns) )

#rows=50
#columns=500

alive="x"
dead=" "


#create create game board function. This one.
def init_board(x,y):
    
    grid=np.random.randint(1, size=(x, y), dtype=bool)
    
    for a in range(int(x)): 
         for b in range(int(y)):
            print("Generating X:", str(a), " Y:", str(b))
            if random.randint(1, 100) > 90 : 
              grid[a][b]=1
            else:
              grid[a][b]=0
    
    return grid;




#too many lists
def print_board(thing):

    for x in range(len(thing)):
        for y in range(len(thing[x])):
            if thing[x][y] == True :
               print(alive, end = '')
            else: 
               print(dead, end= '')
        print()

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



def adv_unit(x, y, grid2):
    adj=get_ajacent(x, y, grid2)
    #if alive, and starving
    if   grid2[x][y]  == True and \
     ( adj == 2 or adj == 3 )  : 
         unit = True
    #if dead, but well feed
    elif grid2[x][y] == False and adj == 3: 
         unit = True
    else:
         unit = False
    return(unit);

#move forward one frame
def adv_board(grid):
    grid3=[[ adv_unit(x, y, grid) for y in range(len(grid[x]))] for x in range(len(grid)) ]
    return grid3;







if __name__ == "__main__":
	

 grid=init_board(rows, columns)

 for x in range(10000000000000000000000000000000000000000000000000000):
  os.system('clear')  
  print_board(grid)
  grid=adv_board(grid)


