import pygame

from game_screen import GameScreen
from menu_state import MenuState


def main():
    pygame.init()
    # Set up the display
    screen_width = 800
    screen_height = 600
    # Set up colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    # Create the game screen for managing the game display
    game_screen = GameScreen(width=screen_width, height=screen_height, background_color=black, object_color=white)
    # set up the game state
    current_game_state = MenuState(game_screen)
    running = True
    # Main game loop
    while running:
        for event in pygame.event.get():
            # check for quit event
            if event.type == pygame.QUIT:
                game_screen.quit_game()
        # get the current game state and execute it
        new_state = current_game_state.execute()
        # if the new state is not None, update the current game state
        if new_state is not None:
            current_game_state = new_state
        pygame.display.update()


if __name__ == '__main__':
    main()
