import pygame
import sys
from snake import Snake
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from background import Background


pygame.init()
pygame.display.set_caption("贪吃蛇小作战")

settings = Settings()
screen = pygame.display.set_mode(settings.size)
font = pygame.font.SysFont('yaheiconsolashybrid', 17)

Tip = font.render('If you want to try again, please press Q ~', True, (65, 105, 225))

bg = Background(settings, screen)
snake = Snake(settings, screen, bg)

foods = Group()

clock = pygame.time.Clock()

count = 0

while True:
    gf.check_events(settings, screen, snake, clock, bg)
    screen.fill((230, 230, 230))
    bg.update()
    gf.snake_move(settings, screen, snake, clock, bg)
    snake.blitme()
    clock.tick(15)



    pygame.display.flip()

