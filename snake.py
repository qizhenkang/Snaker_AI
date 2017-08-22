import pygame


class Snake:

    def __init__(self, settings, screen, background):
        self.length = 5

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.firstx = self.screen_rect.centerx
        self.firsty = self.screen_rect.centery
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



        '''
        else:
            settings.heart -= 1
            if settings.heart < 1:
                settings.running = False
                self.screen.blit(settings.gameover, (100, 0))
            settings.count = 0
            '''
'''
        if settings.count == 10:  # 控制帧率核心参数
            rect_first = pygame.Rect(snake.firstx, snake.firsty, 20, 20)
            settings.count = 0
            snake.rect_tuple.append(rect_first)
            snake.rect = snake.rect_tuple[-1]
            while len(snake.rect_tuple) >= snake.length:
                del snake.rect_tuple[0]
'''

'''
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
'''

