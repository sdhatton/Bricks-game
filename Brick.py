import pygame
from pygame.locals import *
import random

class Brick(pygame.sprite.Sprite):

    def __init__(self, window, x, y, width, height):
        super().__init__()
        self.window = window  # remember the window, so we can draw later
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = random.choice(['red', 'blue', 'yellow'])
        self.image = pygame.Surface((self.width, self.height))
        
    def get_x(self):
        return self.x

    def get_width(self):
        return self.width

    def draw(self):
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        pygame.draw.rect(self.window, self.colour, self.rect)
