# Bricks game - pygame

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random

from Wall import *
from Brick import *
from Ball import *
from Paddle import *
from Score import *

# 2 - Define constants
from Constants import *
POINTS_PER_BRICK = 10
SPEED = 10
       
# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  

# 4 - Load assets: image(s), sounds, etc.

# 5 - Initialize variables

o_wall = Wall(window)
o_wall.add_bricks(2, 8)
o_ball = Ball(window)    #numbers need changing
o_paddle = Paddle(window)
x_mouse, y_mouse = pygame.mouse.get_pos()
o_paddle.move(x_mouse)
o_score = Score(window)

# 6 Loop

game_state = 'ball_on_bat'

while game_state == 'ball_on_bat':
    
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()          

    if pygame.mouse.get_pressed()[0]:
        game_state = 'ball_in_play'
        break
 
    # 8 - Do any "per frame" actions
    x_mouse, y_mouse = pygame.mouse.get_pos()
    o_paddle.move(x_mouse - 30)
    o_ball.move_on_paddle(x_mouse)

    # 9 - Clear the window before drawing it again
    window.fill(BLACK)
    
    # 10 - Draw the window elements
    o_wall.draw()
    o_ball.draw()
    o_paddle.draw()
    o_score.draw()
    
    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait


while game_state == 'ball_in_play':
    
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()          

    # 8 - Do any "per frame" actions
    x_mouse, y_mouse = pygame.mouse.get_pos()
    o_paddle.move(x_mouse - 30)
    for i in range(SPEED):
        o_ball.move_released()
        o_ball.check_for_window()
        o_ball.check_for_paddle(o_paddle)

        if o_wall.check_for_collision(o_ball):
            o_score.increase(POINTS_PER_BRICK)
	
    # 9 - Clear the window before drawing it again
    window.fill(BLACK)
    
    # 10 - Draw the window elements
    o_wall.draw()
    o_ball.draw()
    o_paddle.draw()
    o_score.draw()
    
    # 11 - Update the window
    pygame.display.update()

    if o_wall.no_bricks_check() == 0:
        game_state = 'winner'
        break
        
    if o_ball.check_for_game_over():
        game_state = 'game_over'
        break

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
    
while game_state == 'winner':
    
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()   

    font = pygame.font.Font('freesansbold.ttf', 28)
    text = font.render('WINNER', True, (0, 255, 0), (0, 0, 128))
    textRect = text.get_rect()
    textRect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    pygame.display.update(window.blit(text, textRect))
 
while game_state == 'game_over':
    
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  

    font = pygame.font.Font('freesansbold.ttf', 28)
    text = font.render('GAME OVER', True, (0, 255, 0), (0, 0, 128))
    textRect = text.get_rect()
    textRect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    pygame.display.update(window.blit(text, textRect))
   

    # ADD GAME OVER CODE