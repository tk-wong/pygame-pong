import math

import pygame


def main():
    pygame.init()
    # Set up the display
    screen_width = 800
    screen_height = 600
    target_fps = 60
    ball_speed = 4.5
    ball_x, ball_y = (400, 300)
    ball_radius = 5
    is_reversed_x = False
    is_reversed_y = False
    screen = pygame.display.set_mode((screen_width, screen_height))
    border = screen.get_rect()
    pygame.display.set_caption("Ping Pong")
    clock = pygame.time.Clock()
    # Set up colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)

    bat_width = 10
    bat_height = 50
    padding = 10
    left_bat = pygame.Rect(0 + padding, screen_height // 2 - bat_height // 2, bat_width, bat_height)
    right_bat = pygame.Rect(screen_width - bat_width - padding, screen_height // 2 - bat_height // 2, bat_width,
                            bat_height)
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

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and right_bat.y > 0:
            right_bat.y -= pad_moving_speed
        if keys[pygame.K_DOWN] and right_bat.y + bat_height< border.bottom:
            right_bat.y += pad_moving_speed
        if keys[pygame.K_w] and left_bat.y > 0:
            left_bat.y -= pad_moving_speed
        if keys[pygame.K_s] and left_bat.y + bat_height < border.bottom:
            left_bat.y += pad_moving_speed
        # Update the display
        pygame.display.flip()
        # Fill the screen with white color

        screen.fill(white)
        ball = pygame.draw.circle(screen, black, (ball_x, ball_y), ball_radius)
        hit_box_x = ball_x - ball_radius
        hit_box_y = ball_y - ball_radius
        hit_box_size = ball_radius * 2
        hit_box = pygame.Rect(hit_box_x, hit_box_y, hit_box_size, hit_box_size)
        # pygame.draw.rect(screen, red, hit_box,1)
        pygame.draw.rect(screen, black, left_bat)
        pygame.draw.rect(screen, black, right_bat)
        if is_reversed_x:
            ball_x -= moving_speed
        else:
            ball_x += moving_speed

        if is_reversed_y:
            ball_y += moving_speed
        else:
            ball_y -= moving_speed
        if hit_left(ball_radius, ball_x, border) or hit_right(ball_radius, ball_x, border):
            is_reversed_x = not is_reversed_x
        if hit_top(ball_radius, ball_y, border) or hit_bottom(ball_radius, ball_y, border):
            is_reversed_y = not is_reversed_y
        # if ball_y < 0:
        #     is_reversed_y = True
        # elif ball_y > screen_height:
        #     is_reversed_y = False
        # screen.blit(ball, (400, 300))
        # Update the display
        pygame.display.update()
        # Limit the frame rate
        # pygame.time.Clock().tick(fps)
        # ball.move(5,5)


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
