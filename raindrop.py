import pygame
from pygame.sprite import Sprite
from random import randint

class Raindrop(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, self.ai_settings.screen_width)
        self.rect.y = 0
        self.y = float(self.rect.y)
    def update(self):
	    #Moving raindrop
        self.y += self.ai_settings.raindrop_speed_factor
        self.rect.y = self.y
    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom > screen_rect.bottom:
            return True
