import pygame
import time
import sys
from food import Food


def check_events(settings, screen, snake, clock):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                if snake.mv_down is False:
                    snake.mv_up = True
                    snake.mv_right = False
                    snake.mv_left = False
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if snake.mv_up is False:
                    snake.mv_down = True
                    snake.mv_right = False
                    snake.mv_left = False
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if snake.mv_left is False:
                    snake.mv_right = True
                    snake.mv_up = False
                    snake.mv_down = False
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if snake.mv_right is False:
                    snake.mv_left = True
                    snake.mv_up = False
                    snake.mv_down = False
            elif event.key == pygame.K_f:
                settings.food_position = True
            elif event.key == pygame.K_q:
                settings.running = True
                settings.heart = 3
                snake.zero(screen)
                clock.tick()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_f:
                settings.food_position = False
        elif event.type == pygame.QUIT:
            sys.exit()


def creat_food(settings, screen, foods):
    for i in range(10):
        food = Food(settings, screen)
        foods.add(food)


def update_food(settings, screen, snakes, foods):
    collisions = pygame.sprite.groupcollide(snakes, foods, False, True)
    if collisions != {}:
        settings.score += 100
        snakes.sprites()[0].length += 20

    if len(foods) < 1:
        creat_food(settings, screen, foods)


def update_screen(settings, screen, snake, foods, clock):
    screen.fill(settings.bg_color)

    # 游戏帧率控制
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    settings.speed = time_passed_seconds * 150  # 速度核心参数

    foods.update()
    snake_move(snake, settings, screen, clock)
    snake.blitme()

    heart_rect = settings.heart_image.get_rect()
    for i in range(settings.heart):
        screen.blit(settings.heart_image, (screen.get_rect().right -
                                           (heart_rect.width + 10) * (i + 1) - 10, 10))

    if settings.food_position:
        foods.update()

    pygame.display.flip()


def snake_move(snake, settings, screen, clock):
    if snake.mv_right is True and snake.firstx + 25 <= snake.screen_rect.right:
        snake.firstx += settings.speed
        settings.count += 1
    elif snake.mv_up is True and snake.firsty >= 5:
        snake.firsty -= settings.speed
        settings.count += 1
    elif snake.mv_down is True and snake.firsty + 25 <= snake.screen_rect.bottom:
        snake.firsty += settings.speed
        settings.count += 1
    elif snake.mv_left is True and snake.firstx >= 5:
        snake.firstx -= settings.speed
        settings.count += 1
    else:
        heart_rect = settings.heart_image.get_rect()
        for i in range(settings.heart):
            screen.blit(settings.heart_image, (screen.get_rect().right -
                                               (heart_rect.width + 10) * (i + 1) - 10, 10))

        pygame.display.flip()
        time.sleep(0.2)
        snake.blitme()
        pygame.display.flip()
        time.sleep(0.3)

        for i in range(2):
            for rect in snake.rect_tuple:
                pygame.draw.rect(snake.screen, (230, 230, 230), rect, 0)
            pygame.display.flip()
            time.sleep(0.2)
            snake.blitme()
            pygame.display.flip()
            time.sleep(0.3)

        settings.heart -= 1
        if settings.heart < 1:
            settings.running = False
            screen.blit(settings.gameover, (100, 0))
        clock.tick()
        snake.zero(screen)
        settings.count = 0

    if settings.count == 10:  # 控制帧率核心参数
        rect_first = pygame.Rect(snake.firstx, snake.firsty, 20, 20)
        settings.count = 0
        snake.rect_tuple.append(rect_first)
        snake.rect = snake.rect_tuple[-1]
        while len(snake.rect_tuple) >= snake.length:
            del snake.rect_tuple[0]



    '''
    for i in range(self.length):
        if i == 0:
            rect_first = pygame.Rect(self.firstx, self.firsty, 25, 25)
            self.rect_tuple.append(rect_first)

        if self.mv_right:
            rect = pygame.Rect(self.rect_tuple[-1].x - 30, self.rect_tuple[-1].y, 25, 25)
            self.rect_tuple.append(rect)
        elif self.mv_up:
            rect = pygame.Rect(self.rect_tuple[-1].x, self.rect_tuple[-1].y + 30, 25, 25)
            self.rect_tuple.append(rect)
    '''

