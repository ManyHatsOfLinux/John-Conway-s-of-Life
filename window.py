
import os
import random
from time import sleep
from golV2 import *
from tkinter import *


xheight=800
xwidth=800
delay=1
pixel_count=10

alive_color="white"
dead_color="black"

rows    = int( xheight / pixel_count )
columns = int( xwidth / pixel_count )
import tkinter


def gui_def_unit(x,y,grid,workspace):
      if grid[int(x/pixel_count)][int(y/pixel_count)] == True : 
        workspace.create_rectangle(x, y, int(x+pixel_count), int(y+pixel_count), fill=alive_color, outline = 'grey')
      else: 
        workspace.create_rectangle(x, y, int(x+pixel_count), int(y+pixel_count), fill=dead_color, outline = 'black')

      

def gui_print_board(grid, workspace):
    w = Canvas(master, width=xwidth, height=xheight)
    [ [ gui_def_unit(x,y,grid, workspace) for y in range(0, xheight, pixel_count)] for x in range(0, xwidth, pixel_count)]
    workspace.pack()
    return;


	
    
    
def gui_board_init(): 	
   master = Tk()
   master.title = "Game of Life"
   master.geometry( str(xwidth) + "x" + str(xheight) )
   master.resizable(0,0)
   master.wm_attributes("-topmost", 1)
   w = Canvas(master, width=xwidth, height=xheight)
   #w.pack()
   return(master, w);
   


class board: 
    def __init__(self, grid, canvas):
        self.canvas    =  canvas
        self.grid      =  grid
        gui_print_board(self.grid, self.canvas)
      
		
    def advance(self): 
      #  print("1")
        self.grid = adv_board(self.grid)
      #  print("2")
        gui_print_board(self.grid, self.canvas)
       # print("3")
        self.canvas.after(delay, self.advance)
       # print("4")

if __name__ == "__main__":
 grid=init_board(rows, columns)
 master, w=gui_board_init()
 
 while True:
     grid=adv_board(grid)
     gui_print_board(grid, w)
     w.update()
     w.delete(ALL)
 
 
 
 #gui_print_board(grid, w)
 #print("Building Board Class")
 #borked=board(grid, w)
 #print("attepting update thing")
 #borked.advance()
 #print("Broke out to mainloop")
 #w.mainloop()
