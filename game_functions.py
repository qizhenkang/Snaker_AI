import pygame
import time
import sys
from food import Food


def check_events(settings, screen, snake, clock, bg):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                if snake.mv_down is False:
                    snake.mv_up = True
                    snake.mv_right = False
                    snake.mv_left = False

                    if snake.grow is False:
                        del snake.rect_tuple[-1]
                    else:
                        snake.grow = True
                    rect = pygame.Rect(snake.rect_tuple[0].x, snake.rect_tuple[0].y - bg.s_width, bg.s_width, bg.s_width)
                    snake.rect_tuple.insert(0, rect)
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if snake.mv_up is False:
                    snake.mv_down = True
                    snake.mv_right = False
                    snake.mv_left = False
                    if snake.grow is False:
                        del snake.rect_tuple[-1]
                    else:
                        snake.grow = True
                    rect = pygame.Rect(snake.rect_tuple[0].x, snake.rect_tuple[0].y + bg.s_width, bg.s_width, bg.s_width)
                    snake.rect_tuple.insert(0, rect)
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if snake.mv_left is False:
                    snake.mv_right = True
                    snake.mv_up = False
                    snake.mv_down = False
                    if snake.grow is False:
                        del snake.rect_tuple[-1]
                    else:
                        snake.grow = True
                    rect = pygame.Rect(snake.rect_tuple[0].x + bg.s_width, snake.rect_tuple[0].y, bg.s_width, bg.s_width)
                    snake.rect_tuple.insert(0, rect)
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if snake.mv_right is False:
                    snake.mv_left = True
                    snake.mv_up = False
                    snake.mv_down = False
                    if snake.grow is False:
                        del snake.rect_tuple[-1]
                    else:
                        snake.grow = True
                    rect = pygame.Rect(snake.rect_tuple[0].x - bg.s_width, snake.rect_tuple[0].y, bg.s_width,bg.s_width)
                    snake.rect_tuple.insert(0, rect)
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


def creat_food(settings, screen, snake, food, background):
    if food.rect.x == snake.rect_tuple[0].x and food.rect.y == snake.rect_tuple[0].y:
        food.update()
        snake.grow = True


def update_food(settings, screen, snakes, foods):
    collisions = pygame.sprite.groupcollide(snakes, foods, False, True)
    if collisions != {}:
        settings.score += 100
        snakes.sprites()[0].length += 20

    if len(foods) < 1:
        creat_food(settings, screen, foods)


def Eat_food(settings, screen, snake, food):
    if food.rect.x == snake.rect_tuple[0].x and food.rect.y == snake.rect_tuple[0].y:
        print('EAT!!!!!!!!!!!!!!!!!')


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


def snake_move(settings, screen, snake, clock, bg):
    if snake.mv_right is True and snake.rect_tuple[0].right < snake.screen_rect.right:
        if snake.grow is False:
            del snake.rect_tuple[-1]
        else:
            snake.grow = True
        rect = pygame.Rect(snake.rect_tuple[0].x + bg.s_width, snake.rect_tuple[0].y, bg.s_width, bg.s_width)
        snake.rect_tuple.insert(0, rect)
        settings.count += 1
    elif snake.mv_up is True and snake.rect_tuple[0].y > 0:
        if snake.grow is False:
            del snake.rect_tuple[-1]
        else:
            snake.grow = True
        rect = pygame.Rect(snake.rect_tuple[0].x, snake.rect_tuple[0].y - bg.s_width, bg.s_width, bg.s_width)
        snake.rect_tuple.insert(0, rect)
        settings.count += 1

    elif snake.mv_down is True and snake.rect_tuple[0].bottom < snake.screen_rect.bottom:
        if snake.grow is False:
            del snake.rect_tuple[-1]
        else:
            snake.grow = True
        rect = pygame.Rect(snake.rect_tuple[0].x, snake.rect_tuple[0].y + bg.s_width, bg.s_width, bg.s_width)
        snake.rect_tuple.insert(0, rect)
        settings.count += 1

    elif snake.mv_left is True and snake.rect_tuple[0].x > 0:
        if snake.grow is False:
            del snake.rect_tuple[-1]
        else:
            snake.grow = True
        rect = pygame.Rect(snake.rect_tuple[0].x - bg.s_width, snake.rect_tuple[0].y, bg.s_width, bg.s_width)
        snake.rect_tuple.insert(0, rect)
        settings.count += 1
    else:
        pass




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

