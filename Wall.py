import pygame
from pygame.locals import *
import random

from Brick import *
from Ball import *

from Constants import *

# Wall class 
class Wall():

    def __init__(self, window):
        self.window = window  # remember the window, so we can draw later
        
        self.bricks_list = []
        
    def add_bricks(self, no_rows, no_cols):
        width = (WINDOW_WIDTH - 50) // no_cols
        height = ((WINDOW_HEIGHT // 3) - 25) // no_rows
        for i in range(no_rows):
            for j in range(no_cols):
                x = 20 + j * width
                y = 20 + i * height
                o_brick = Brick(self.window, x, y, width, height)
                self.bricks_list.append(o_brick)

    def check_for_collision(self, o_ball):
        collision_flag = False
        for o_brick in self.bricks_list:
            if pygame.sprite.collide_rect(o_brick, o_ball):
                self.bricks_list.remove(o_brick)
                collision_flag = True
                if o_ball.get_x() - o_brick.get_x() < 0 or o_ball.get_x() - (o_brick.get_x() + o_brick.get_width()) > 0:
                    o_ball.bounce_l_r()
                else:
                    o_ball.bounce_u_d()
        return collision_flag
    		
    def draw(self):
        for o_brick in self.bricks_list:
            o_brick.draw()
    
    def no_bricks_check(self):
        return len(self.bricks_list)