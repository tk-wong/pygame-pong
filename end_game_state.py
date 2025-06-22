import pygame
import sys

from game_running_state import GameRunningState
from game_state import GameState


class EndGameState(GameState):
    def __init__(self, game_screen, left_score, right_score):
        self.game_screen = game_screen
        self.left_score = left_score
        self.right_score = right_score

    def execute(self):
        screen = self.game_screen.screen
        font = self.game_screen.font
        button_font = pygame.font.Font(None, 24)
        object_color = self.game_screen.object_color

        screen.fill(self.game_screen.background_color)
        if self.left_score > self.right_score:
            result_text = "Left Player Wins!"
        else:
            result_text = "Right Player Wins!"
        # else:
        #     result_text = "It's a Draw!"

        text_surface = font.render(result_text, True, object_color)
        text_rect = text_surface.get_rect(center=(self.game_screen.width // 2, self.game_screen.height // 2))
        screen.blit(text_surface, text_rect)
        restart_button_width = 100
        restart_button_height = 50
        restart_button = pygame.Rect(text_rect.left + (text_rect.width - (restart_button_width*2 +10)) // 2,
                                     text_rect.bottom + 20, restart_button_width, restart_button_height)
        exit_button = pygame.Rect(restart_button.left + restart_button_width + 10, text_rect.bottom + 20 , restart_button_width,
                                  restart_button_height)
        pygame.draw.rect(screen, object_color, restart_button, width=2)
        restart_text = button_font.render("Restart", True, self.game_screen.object_color)
        restart_text_rect = restart_text.get_rect(center=restart_button.center)
        screen.blit(restart_text, restart_text_rect)
        pygame.draw.rect(screen, object_color, exit_button, width=2)
        exit_text = button_font.render("Exit", True, self.game_screen.object_color)
        exit_text_rect = exit_text.get_rect(center=exit_button.center)
        screen.blit(exit_text, exit_text_rect)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if restart_button.collidepoint(event.pos):
                        return GameRunningState(self.game_screen)
                    elif exit_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
            elif event.type == pygame.QUIT:
                self.game_screen.quit()
        return None