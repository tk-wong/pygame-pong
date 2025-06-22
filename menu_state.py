import sys

import pygame

from game_state import GameState


class MenuState(GameState):
    def __init__(self, game_screen):
        self.game_screen = game_screen

    def execute(self):
        screen = self.game_screen.screen
        font = self.game_screen.font
        object_color = self.game_screen.object_color

        screen.fill(self.game_screen.background_color)
        title_text = font.render("Pong Game", True, object_color)
        title_rect = title_text.get_rect(center=(self.game_screen.width // 2, self.game_screen.height // 2 - 50))
        screen.blit(title_text, title_rect)

        # start_text = font.render("Press Enter to Start", True, object_color)
        # start_rect = start_text.get_rect(center=(self.game_screen.width // 2, self.game_screen.height // 2 + 50))
        # screen.blit(start_text, start_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_screen.quit()
            # elif event.type == self.game_screen.KEYDOWN:
            #     if event.key == self.game_screen.K_RETURN:
            #         return GameState(self.game_screen)  # Replace with actual game state

        return None