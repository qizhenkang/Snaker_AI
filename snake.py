import pygame


class Snake(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.zero(screen)

    def zero(self, screen):
        self.length = 50

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.firstx = self.screen_rect.centerx
        self.firsty = self.screen_rect.centery

        self.mv_right = True
        self.mv_left = False
        self.mv_up = False
        self.mv_down = False

        self.rect_tuple = []

        rect_first = pygame.Rect(self.firstx, self.firsty, 20, 20)
        self.rect_tuple.append(rect_first)
        self.rect = self.rect_tuple[-1]

        self.blitme()

    def blitme(self):
        for rect in self.rect_tuple:
            pygame.draw.rect(self.screen, (127, 255, 0), rect, 0)
        if self.rect_tuple:
            self.head_rect = pygame.Rect(-10, -10, 10, 10)
            self.head_rect.centerx = self.rect_tuple[-1].centerx
            self.head_rect.centery = self.rect_tuple[-1].centery
            pygame.draw.rect(self.screen, (255, 255, 0), self.head_rect, 0)

