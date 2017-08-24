import pygame


class Snake:

    def __init__(self, settings, screen, background):
        self.length = 7

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.firstx = background.line_x[len(background.line_x)// 2]
        self.firsty = background.line_y[len(background.line_y)// 2]
        self.bg = background

        self.mv_right = True
        self.mv_left = False
        self.mv_up = False
        self.mv_down = False

        self.grow = False

        self.rect_tuple = []

        for i in range(self.length):
            rect = pygame.Rect(self.firstx - i * self.bg.s_width, self.firsty, background.s_width, background.s_width)
            self.rect_tuple.append(rect)
            pygame.draw.rect(self.screen, (127, 255, 0), rect, 0)


    def blitme(self):
        for rect in self.rect_tuple:
            pygame.draw.rect(self.screen, (127, 255, 0) , rect, 0)


