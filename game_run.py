import pygame
import sys
from snake import Snake
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from background import Background
from food import Food


pygame.init()
pygame.display.set_caption("贪吃蛇小作战")

settings = Settings()
screen = pygame.display.set_mode(settings.size)
font = pygame.font.SysFont('yaheiconsolashybrid', 17)

Tip = font.render('If you want to try again, please press Q ~', True, (65, 105, 225))

bg = Background(settings, screen)
bg.update()
snake = Snake(settings, screen, bg)

clock = pygame.time.Clock()

gameover_blit = True

food = Food(settings, screen, bg)
food.update()

while True:
    gf.check_events(settings, screen, snake, food, clock, bg)

    if settings.running:
        if gf.collision(settings, screen, snake, food, bg):
            gf.snake_move(settings, screen, snake, clock, bg)
        gf.update_screen(settings, screen, snake, food, clock, bg)

        pygame.display.flip()
    elif gameover_blit:
        gameover_blit = False
        screen.blit(settings.gameover, (70, 0))
        pygame.display.flip()


