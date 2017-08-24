import pygame


pygame.init()

class Settings:
    def __init__(self):
        self.size = 800, 600
        self.bg_color = 230, 230, 230
        self.line_color = 100, 255, 200
        self.s_width = 50
        self.score = 0
        self.count = 0

        self.running = True
        self.heart = 3
        self.gameover_blit = True
        self.tick = 10
        self.collision = False
        self.move = True

        self.heart_image = pygame.image.load('.\\resources\\timg.jpg')
        self.background = pygame.image.load('.\\resources\\background.jpg')
        self.gameover = pygame.image.load('.\\resources\\gameover.png')
