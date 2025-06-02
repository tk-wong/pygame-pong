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
        hit_box_x = ball_x - ball_radius
        hit_box_y = ball_y - ball_radius
        hit_box_size = ball_radius * 2
        hit_box = pygame.Rect(hit_box_x, hit_box_y, hit_box_size, hit_box_size)
        # pygame.draw.rect(screen, red, hit_box,1)
        moving_speed = speed * (delta_time / 1000) * target_fps
        if is_reversed_x:
            ball_x -= moving_speed
            # ball_y += moving_speed
        else:
            ball_x += moving_speed
            # ball_y -= moving_speed
        if hit_box_x + hit_box_size >= screen_width or hit_box_y < 0:
            is_reversed_x = True
        elif hit_box_x <= 0 or hit_box_y + hit_box_size > screen_height:
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


# https://stackoverflow.com/questions/55626092/how-to-calculate-reflection-angle-of-a-ball-colliding-with-a-wall
if __name__ == '__main__':
    main()
