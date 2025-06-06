import math
import random

import pygame
from bat import Bat


def main():
    pygame.init()
    # Set up the display
    screen_width = 800
    screen_height = 600
    target_fps = 60
    ball_speed = 4.5
    ball_radius = 5
    is_reversed_x = False
    is_reversed_y = False
    screen = pygame.display.set_mode((screen_width, screen_height))
    border = screen.get_rect()
    ball_x, ball_y = border.center
    pygame.display.set_caption("Ping Pong")
    clock = pygame.time.Clock()
    # Set up colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    background_color = black
    object_color = white
    bat_width = 10
    bat_height = 50
    padding = 10
    left_bat = Bat(top_left_x=+ padding, top_left_y=screen_height // 2 - bat_height // 2, width=bat_width,
                   height=bat_height, color=object_color)
    right_bat = Bat(top_left_x=screen_width - bat_width - padding, top_left_y=screen_height // 2 - bat_height // 2,
                    width=bat_width,
                    height=bat_height, color=object_color)
    pad_speed = 5

    screen.fill(white)
    running = True
    while running:
        delta_time = clock.tick()
        moving_speed = ball_speed * (delta_time / 1000) * target_fps
        pad_moving_speed = math.ceil(pad_speed * (delta_time / 1000) * target_fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill(background_color)
        left_bat.draw(screen)
        right_bat.draw(screen)
        ball = pygame.draw.circle(screen, object_color, (ball_x, ball_y), ball_radius)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and right_bat.rect.y > 0:
            right_bat.move_up(pad_moving_speed, border.top)
        if keys[pygame.K_DOWN] and right_bat.rect.y + bat_height < border.bottom:
            right_bat.move_down(pad_moving_speed, border.bottom)
        if keys[pygame.K_w] and left_bat.rect.y > 0:
            left_bat.move_up(pad_moving_speed, border.top)
        if keys[pygame.K_s] and left_bat.rect.y + bat_height < border.bottom:
            left_bat.move_down(pad_moving_speed, border.bottom)
        if is_reversed_x:
            ball_x -= moving_speed
        else:
            ball_x += moving_speed

        if is_reversed_y:
            ball_y += moving_speed
        else:
            ball_y -= moving_speed
        if hit_top(ball_radius, ball_y, border) or hit_bottom(ball_radius, ball_y, border):
            is_reversed_y = not is_reversed_y
        left_bat_hit = left_bat.ball_hit(ball)
        right_bat_hit = right_bat.ball_hit(ball)
        hit_left_border = hit_left(ball_radius, ball_x, border)
        hit_right_border = hit_right(ball_radius, ball_x, border)
        if left_bat_hit or right_bat_hit:
            is_reversed_x = not is_reversed_x
            if left_bat_hit:
                ball_x = left_bat.rect.right + ball_radius
                # is_hit_left = True
                # is_hit_right = False
            elif right_bat_hit:
                ball_x = right_bat.rect.left - ball_radius
                # is_hit_right = True
                # is_hit_left = False
        elif hit_left_border or hit_right_border:
            ball_x, ball_y = border.center
            if hit_left_border:
                is_reversed_x = False
            else:
                is_reversed_x = True
            is_reversed_y = random.choice([True, False])
        pygame.display.update()


def hit_bottom(ball_radius, ball_y, border):
    return ball_y + ball_radius > border.bottom


def hit_top(ball_radius, ball_y, border):
    return ball_y - ball_radius < border.top


def hit_right(ball_radius, ball_x, border):
    return ball_x + ball_radius > border.right


def hit_left(ball_radius, ball_x, border):
    return ball_x - ball_radius < border.left


if __name__ == '__main__':
    main()
