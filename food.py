import pygame
import random


class Food():

    def __init__(self, settings, screen, background):

        self.screen = screen
        self.settings = settings
        self.background = background

        self.rect = pygame.Rect(-10, -10, settings.s_width, settings.s_width)
        self.rect.x = random.choice(background.line_x)
        self.rect.y = random.choice(background.line_y)
        self.color = 230, 0, 0

    def update(self):
        print(self.rect.x, self.rect.y)
        self.rect.x = random.choice(self.background.line_x)
        self.rect.y = random.choice(self.background.line_y)


    def blitme(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
