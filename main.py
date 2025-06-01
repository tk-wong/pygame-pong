import pygame


def main():
    pygame.init()
    # Set up the display
    screen_width = 800
    screen_height = 600
    fps = 60
    ball_x, ball_y = (400, 300)
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Ping Pong")
    # Set up colors
    WHITE = (255, 255, 255)
    screen.fill(WHITE)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        # Update the display
        pygame.display.flip()
        # Fill the screen with white color
        screen.fill(WHITE)
        ball = pygame.draw.circle(screen, (0, 0, 0), (ball_x, ball_y), 15)
        ball_x += 5
        ball_y -= 1
        if ball_x > screen_width:
            ball_x = 0
        if ball_y < 0:
            ball_y = screen_height
        # screen.blit(ball, (400, 300))
        # Update the display
        pygame.display.update()
        # Limit the frame rate
        pygame.time.Clock().tick(fps)
        # ball.move(5,5)


if __name__ == '__main__':
    main()
