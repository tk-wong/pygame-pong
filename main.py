import pygame
import sys
from end_game_state import EndGameState
# from bat import Bat
from game_running_state import GameRunningState
from game_screen import GameScreen


def main():
    pygame.init()
    # Set up the display
    screen_width = 800
    screen_height = 600
    # Set up colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    game_screen = GameScreen(width=screen_width, height=screen_height, background_color=black, object_color=white)

    current_game_state = GameRunningState(game_screen)
    # current_game_state = EndGameState(game_screen,0,0)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        new_state = current_game_state.execute()
        if new_state is not None:
            current_game_state = new_state
        pygame.display.update()


if __name__ == '__main__':
    main()
