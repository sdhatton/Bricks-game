import pygame
from pygame.locals import *
import random

from Constants import *

# Ball class 
class Ball(pygame.sprite.Sprite):


    def __init__(self, window):
        super().__init__()
        self.window = window  # remember the window, so we can draw later
        self.radius = 6
        self.x = WINDOW_WIDTH/2 - self.radius
        self.y = WINDOW_HEIGHT - 30 - self.radius
        self.x_speed = 1
        self.y_speed = -1
        self.image = pygame.Surface((self.radius * 2, self.radius * 2))
        
    def get_x(self):
        return self.x

    def move_released(self):
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect = self.image.get_rect(center=(self.x, self.y))
        
    def move_on_paddle(self, x):
        self.x = x
        self.y = WINDOW_HEIGHT - 30 - self.radius
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def bounce_l_r(self):
        self.x_speed = -self.x_speed
        
    def bounce_u_d(self):
        self.y_speed = -self.y_speed

    def check_for_window(self):
        if self.x < self.radius:
            self.bounce_l_r()
        if self.x > WINDOW_WIDTH - self.radius:
            self.bounce_l_r()
        if self.y < self.radius:
            self.bounce_u_d()

    def check_for_paddle(self, paddle):
        if pygame.sprite.collide_rect(self, paddle):
            self.bounce_u_d()
            self.move_released()

    def check_for_game_over(self):
        return self.y > WINDOW_HEIGHT
        
    def draw(self):
        pygame.draw.circle(self.window, 'white', (self.x, self.y), self.radius)
