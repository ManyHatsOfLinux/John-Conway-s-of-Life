#!/usr/bin/env python
import os
import random
from time import sleep
from gol import *
from tkinter import *
import tkinter
from datetime import datetime
import datetime as dt

xheight=800
xwidth=1200
delay=1
pixel_count=4

alive_color="white"
dead_color="black"

grid_x   = int( xheight / pixel_count )
grid_y = int( xwidth / pixel_count )



def gui_def_unit(x,y,z,workspace):
      if z == True : 
        workspace.create_rectangle(x, y, int(x+pixel_count), int(y+pixel_count), fill=alive_color, outline = 'black')
      else:
        workspace.create_rectangle(x, y, int(x+pixel_count), int(y+pixel_count), fill=dead_color, outline = 'black')

def gui_print_board(grid, workspace):
    [ [ gui_def_unit(y,x,grid[int(x / pixel_count)][int(y/ pixel_count)], workspace) for y in range(0, xwidth, pixel_count)] for x in range(0, xheight, pixel_count)]
    return;


	
    
    
def gui_init(): 	
   x_window = Tk()
   x_window.title = "Game of Life"
   x_window.geometry( str(xwidth) + "x" + str(xheight) )
   x_window.resizable(0,0)
   x_window.wm_attributes("-topmost", 1)
   canvas = Canvas(x_window, width=xwidth, height=xheight)
   return(x_window, canvas);


class gui_game_board(game_board):
   
    def __init__(self, grid_x, grid_y, xheight, xwidth):
     super().__init__( grid_x, grid_y )
     self.x_window = Tk()
     self.x_window.title = "Game of Life"
     self.x_window.geometry( str(xwidth) + "x" + str(xheight) )
     self.x_window.resizable(0,0)
     self.x_window.wm_attributes("-topmost", 1)
     self.canvas = Canvas(self.x_window, width=xwidth, height=xheight)

    def gui_update(self):
      self.grid = adv_board(self.grid)
      self.canvas.delete(ALL)
      gui_print_board(self.grid, self.canvas)
      self.canvas.pack()
      self.x_window.update()
      self.canvas.after(1, self.gui_update)
      


if __name__ == "__main__":
   
   

   
   
   game = gui_game_board( grid_x, grid_y, xheight, xwidth)
   game.x_window.after(1, game.gui_update)
   game.x_window.mainloop()

   print("broke out")

