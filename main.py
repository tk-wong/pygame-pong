import pygame


def main():
    pygame.init()
    # Set up the display
    screen_width = 800
    screen_height = 600
    fps = 10
    target_fps = 60
    speed = 1
    ball_x, ball_y = (400, 300)
    ball_radius = 5
    is_reversed_x = False
    is_reversed_y = False

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Ping Pong")
    clock = pygame.time.Clock()
    # Set up colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    screen.fill(white)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        # Update the display
        pygame.display.flip()
        # Fill the screen with white color

        delta_time = clock.tick()
        screen.fill(white)
        print(clock.get_fps())
        ball = pygame.draw.circle(screen, black, (ball_x, ball_y), ball_radius)
        hitbox_x = ball_x - ball_radius
        hitbox_y = ball_y - ball_radius
        hitbox_size = ball_radius * 2
        hitbox = pygame.Rect(hitbox_x, hitbox_y, hitbox_size, hitbox_size)
        # pygame.draw.rect(screen, red, hitbox,1)
        moving_speed = speed * (delta_time / 1000) * target_fps
        if is_reversed_x:
            ball_x -= moving_speed
            # ball_y += moving_speed
        else:
            ball_x += moving_speed
            # ball_y -= moving_speed
        if hitbox_x + hitbox_size >= screen_width or hitbox_y < 0:
            is_reversed_x = True
        elif hitbox_x <= 0 or hitbox_y + hitbox_size> screen_height:
            is_reversed_x = False
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


if __name__ == '__main__':
    main()
