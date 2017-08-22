import pygame
import sys


def check_events(settings, screen, snake, food, clock, bg):
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
                        snake.grow = False
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
                        snake.grow = False
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
                        snake.grow = False
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
                        snake.grow = False
                    rect = pygame.Rect(snake.rect_tuple[0].x - bg.s_width, snake.rect_tuple[0].y, bg.s_width,bg.s_width)
                    snake.rect_tuple.insert(0, rect)
            elif event.key == pygame.K_q:
                snake.__init__(settings, screen, bg)
                food.update()
                settings.running = True
        elif event.type == pygame.QUIT:
            sys.exit()


def collision(settings, screen, snake, food, background):
    '''碰撞检测'''

    # 吃到食物
    if food.rect.x == snake.rect_tuple[0].x and food.rect.y == snake.rect_tuple[0].y:
        food.update()
        snake.grow = True

    # 碰到身体
    for rect in snake.rect_tuple[3:]:
        if snake.rect_tuple[0].x == rect.x and snake.rect_tuple[0].y == rect.y:
            settings.running = False
            return False

    return True


def update_screen(settings, screen, snake, food, clock, bg):
    screen.fill((230, 230, 230))
    bg.update()
    food.blitme()
    snake.blitme()
    clock.tick(15)


def snake_move(settings, screen, snake, clock, bg):
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




