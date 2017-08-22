import pygame
from snake import Snake
from pygame.sprite import Group
import game_functions as gf
from settings import Settings


pygame.init()
pygame.display.set_caption("贪吃蛇小作战")

settings = Settings()
screen = pygame.display.set_mode(settings.size)
font = pygame.font.SysFont('yaheiconsolashybrid', 17)

Tip = font.render('If you want to try again, please press Q ~', True, (65, 105, 225))

snake = Snake(screen)
snakes = Group()
snakes.add(snake)
foods = Group()

clock = pygame.time.Clock()

count = 0

while True:
    gf.check_events(settings, screen, snake, clock)
    if settings.running:
        gf.update_food(settings, screen, snakes, foods)
        gf.update_screen(settings, screen, snake, foods, clock)
    elif count == 0:
        screen.blit(settings.gameover, (100, 0))
        screen.blit(Tip, (240, 500))
        pygame.display.flip()
        count += 1
