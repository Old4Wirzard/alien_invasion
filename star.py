import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, self.ai_settings.screen_width)
        self.rect.y = randint(0, self.ai_settings.screen_height)
