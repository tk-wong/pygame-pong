import pygame
from bat import Bat
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
    bat_width = 10
    bat_height = 50
    padding = 10
    game_screen = GameScreen(width=screen_width, height=screen_height, background_color=black, object_color=white)
    left_bat = Bat(top_left_x=+ padding, top_left_y=screen_height // 2 - bat_height // 2, width=bat_width,
                   height=bat_height, color=game_screen.object_color)
    right_bat = Bat(top_left_x=screen_width - bat_width - padding, top_left_y=screen_height // 2 - bat_height // 2,
                    width=bat_width,
                    height=bat_height, color=game_screen.object_color)

    current_game_state = GameRunningState(game_screen, left_bat, right_bat)
    running = True
    while running:
        new_state = current_game_state.execute()
        if new_state is not None:
            current_game_state = new_state
        pygame.display.update()


if __name__ == '__main__':
    main()
