import pygame
import sys


def check_events(settings, screen, snake, food, bg):
    for event in pygame.event.get():
        if settings.event:
            settings.event = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    Turn_UP(settings, snake, bg)
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    Turn_DOWN(settings, snake, bg)
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    Turn_RIGHT(settings, snake, bg)
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    Turn_LEFT(settings, snake, bg)
                elif event.key == pygame.K_SPACE:
                    settings.tick = 12                           #按下空格可实现加速~
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_q:
                    bg.__init__(settings, screen)
                    bg.update()
                    snake.__init__(settings, screen, bg)
                    food.update(snake)
                    settings.running = True
                    settings.gameover_blit = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    settings.tick = 7
            elif event.type == pygame.QUIT:
                sys.exit()

    settings.event = True


def Eat_food(snake, food):

    # 吃到食物
    if int(food.rect.x) == int(snake.rect_tuple[0].x) and int(food.rect.y) == int(snake.rect_tuple[0].y):
        food.update(snake)
        snake.grow = True


def collision(settings, screen, snake, food, background):
    '''碰撞检测'''

    # 碰到身体
    for rect in snake.rect_tuple[3:]:
        if snake.rect_tuple[0].x == rect.x and snake.rect_tuple[0].y == rect.y:
            settings.running = False
            return True
    return False


def update_screen(settings, screen, snake, food, clock, bg):
    screen.fill((230, 230, 230))
    bg.update()
    food.blitme()
    snake.blitme()
    clock.tick(settings.tick)


def snake_move(settings, screen, snake, bg):
    if not settings.turn:
        if snake.mv_right is True and snake.rect_tuple[0].right < snake.screen_rect.right:
            if snake.grow is False:
                del snake.rect_tuple[-1]
            else:
                snake.grow = False
            rect = pygame.Rect(snake.rect_tuple[0].x + bg.s_width, snake.rect_tuple[0].y, bg.s_width, bg.s_width)
            snake.rect_tuple.insert(0, rect)
            settings.count += 1
        elif snake.mv_up is True and snake.rect_tuple[0].y > 0:
            if snake.grow is False:
                del snake.rect_tuple[-1]
            else:
                snake.grow = False
            rect = pygame.Rect(snake.rect_tuple[0].x, snake.rect_tuple[0].y - bg.s_width, bg.s_width, bg.s_width)
            snake.rect_tuple.insert(0, rect)
            settings.count += 1

        elif snake.mv_down is True and snake.rect_tuple[0].bottom < snake.screen_rect.bottom:
            if snake.grow is False:
                del snake.rect_tuple[-1]
            else:
                snake.grow = False
            rect = pygame.Rect(snake.rect_tuple[0].x, snake.rect_tuple[0].y + bg.s_width, bg.s_width, bg.s_width)
            snake.rect_tuple.insert(0, rect)
            settings.count += 1

        elif snake.mv_left is True and snake.rect_tuple[0].x > 0:
            if snake.grow is False:
                del snake.rect_tuple[-1]
            else:
                snake.grow = False
            rect = pygame.Rect(snake.rect_tuple[0].x - bg.s_width, snake.rect_tuple[0].y, bg.s_width, bg.s_width)
            snake.rect_tuple.insert(0, rect)
            settings.count += 1
        else:
            settings.running = False
    else:
        if snake.rect_tuple[0].right <= snake.screen_rect.right and snake.rect_tuple[0].bottom <= snake.screen_rect.bottom and snake.rect_tuple[0].y >= 0 or snake.rect_tuple[0].x >= 0:
            if snake.mv_right:
                if snake.grow is False:
                    del snake.rect_tuple[-1]
                else:
                    snake.grow = False
                rect = pygame.Rect(snake.rect_tuple[0].x + bg.s_width, snake.rect_tuple[0].y, bg.s_width, bg.s_width)
                snake.rect_tuple.insert(0, rect)
            elif snake.mv_left:
                if snake.grow is False:
                    del snake.rect_tuple[-1]
                else:
                    snake.grow = False
                rect = pygame.Rect(snake.rect_tuple[0].x - bg.s_width, snake.rect_tuple[0].y, bg.s_width, bg.s_width)
                snake.rect_tuple.insert(0, rect)
            elif snake.mv_up:
                if snake.grow is False:
                    del snake.rect_tuple[-1]
                else:
                    snake.grow = False
                rect = pygame.Rect(snake.rect_tuple[0].x, snake.rect_tuple[0].y - bg.s_width, bg.s_width, bg.s_width)
                snake.rect_tuple.insert(0, rect)
            elif snake.mv_down:
                if snake.grow is False:
                    del snake.rect_tuple[-1]
                else:
                    snake.grow = False
                rect = pygame.Rect(snake.rect_tuple[0].x, snake.rect_tuple[0].y + bg.s_width, bg.s_width, bg.s_width)
                snake.rect_tuple.insert(0, rect)
        else:
            settings.running = False
    settings.turn = False


def AI_choice(settings, screen, snake, food, bg):
    pass


def Turn_UP(settings, snake, bg):
    if snake.mv_down is False:
        snake.mv_up = True
        snake.mv_right = False
        snake.mv_left = False
        settings.turn = True
        return True
    else:
        return False
def Turn_DOWN(settings, snake, bg):
    if snake.mv_up is False:
        snake.mv_down = True
        snake.mv_right = False
        snake.mv_left = False
        settings.turn = True
        return True
    else:
        return False

def Turn_RIGHT(settings, snake, bg):
    if snake.mv_left is False:
        snake.mv_right = True
        snake.mv_up = False
        snake.mv_down = False
        settings.turn = True
        return True
    else:
        return False

def Turn_LEFT(settings, snake, bg):
    if snake.mv_right is False:
        snake.mv_left = True
        snake.mv_up = False
        snake.mv_down = False
        settings.turn = True
        return True
    else:
        return False