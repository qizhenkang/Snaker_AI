import pygame
import random


class Food(pygame.sprite.Sprite):

    def __init__(self, settings, screen):
        super().__init__()

        self.rect = pygame.Rect(-10, -10, 7, 7)
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = random.uniform(10, self.screen_rect.right - 10)
        self.rect.centery = random.uniform(10, self.screen_rect.bottom - 10)
        self.color = 230, 0, 0

    def update(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
