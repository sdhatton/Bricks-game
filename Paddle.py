import pygame
from pygame.locals import *
import random

from Constants import *

# Wall class 
class Paddle(pygame.sprite.Sprite):

    def __init__(self, window):
        super().__init__()
        self.window = window  # remember the window, so we can draw later
        self.height = 10
        self.width = 60
        self.x = WINDOW_WIDTH / 2
        self.y = WINDOW_HEIGHT - self.width/2
        self.image = pygame.Surface([self.width, self.height])
        
    def move(self, x):
        self.x = x
        
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def draw(self):
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        pygame.draw.rect(self.window, 'red', self.rect)

