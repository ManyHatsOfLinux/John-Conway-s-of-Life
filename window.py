#!/usr/bin/env python
import os
import random
from time import sleep
from golV2 import *
from tkinter import *
import tkinter
from datetime import datetime
import datetime as dt

xheight=400
xwidth=800
delay=1
pixel_count=4

alive_color="white"
dead_color="black"

rows    = int( xheight / pixel_count )
columns = int( xwidth / pixel_count )



def gui_def_unit(x,y,z,workspace):
      if z == True : 
        workspace.create_rectangle(x, y, int(x+pixel_count), int(y+pixel_count), fill=alive_color, outline = 'black')
      else:
        workspace.create_rectangle(x, y, int(x+pixel_count), int(y+pixel_count), fill=dead_color, outline = 'black')


def gui_print_board(grid, workspace):
    [ [ gui_def_unit(x,y,grid[int(x/pixel_count)][int(y/pixel_count)], workspace) for y in range(0, xwidth, pixel_count)] for x in range(0, xheight, pixel_count)]
    return;


	
    
    
def gui_board_init(): 	
   master = Tk()
   master.title = "Game of Life"
   master.geometry( str(xwidth) + "x" + str(xheight) )
   master.resizable(0,0)
   master.wm_attributes("-topmost", 1)
   w = Canvas(master, width=xwidth, height=xheight)
   return(master, w);


if __name__ == "__main__":
 print(rows, columns)
 grid=init_board(rows, columns)
 print(grid)
 master, w=gui_board_init()
 

#total_time = datetime.now() - datetime.now() 
for z in range(50):
     
     grid=adv_board(grid)
#     start_time = datetime.now()
     gui_print_board(grid, w)
#     time_elapsed = datetime.now() - start_time 
#     total_time = time_elapsed + total_time
#     print(total_time)
#     print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))
     
     
     w.update()
     w.pack()
     w.delete(ALL)

 
 
 #gui_print_board(grid, w)
 #print("Building Board Class")
 #borked=board(grid, w)
 #print("attepting update thing")
 #borked.advance()
 #print("Broke out to mainloop")
 #w.mainloop()
