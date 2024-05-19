import pygame
from pygame.locals import *
import random

from Constants import *

# Wall class 
class Score():

    def __init__(self, window):
        self.window = window  # remember the window, so we can draw later
        self.score = 0
        self.font = pygame.font.Font('freesansbold.ttf', 28)
        self.text = self.font.render(str(self.score), True, (0, 255, 0), (0, 0, 128))
        self.textRect = self.text.get_rect()
        self.textRect.center = (WINDOW_WIDTH - 75, WINDOW_HEIGHT - 75)        

    def increase(self, i):
        self.score += i
        self.text = self.font.render(str(self.score), True, (0, 255, 0), (0, 0, 128))
        
    def reset(self):
        self.score = 0
        self.text = self.font.render(str(self.score), True, (0, 255, 0), (0, 0, 128))
        
    def draw(self):
        self.window.blit(self.text, self.textRect)
