import pygame


class Background:

    def __init__(self, settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        self.s_width = 20
        self.line_x = []
        self.line_y = []


    def update(self):
        for i in range(int(self.screen_rect.width / self.s_width)):
            x = (i + 1) * self.s_width
            self.line_x.append(x)
            pygame.draw.line(self.screen, self.settings.line_color, (x, 0), (x, self.screen_rect.bottom), 2)
        self.line_x.pop()
        self.line_x.append(0)

        for j in range(int(self.screen_rect.height / self.s_width)):
            y = (j + 1) * self.s_width
            self.line_y.append(y)
            pygame.draw.line(self.screen, self.settings.line_color, (0, y), (self.screen_rect.right, y), 2)
        self.line_y.pop()
        self.line_x.append(0)
