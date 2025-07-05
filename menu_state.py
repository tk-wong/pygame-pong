

import pygame
import game_state
import game_running_state




class MenuState(game_state.GameState):
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

        button_font = pygame.font.Font(None, 24)
        button_width = 100
        button_height = 50
        restart_button = pygame.Rect(title_rect.left + (title_rect.width - (button_width * 2 + 10)) // 2,
                                     title_rect.bottom + 20, button_width, button_height)
        exit_button = pygame.Rect(restart_button.left + button_width + 10, title_rect.bottom + 20, button_width,
                                  button_height)

        pygame.draw.rect(screen, object_color, restart_button, width=2)
        start_text = button_font.render("Start", True, self.game_screen.object_color)
        start_text_rect = start_text.get_rect(center=restart_button.center)
        screen.blit(start_text, start_text_rect)
        pygame.draw.rect(screen, object_color, exit_button, width=2)
        exit_text = button_font.render("Exit", True, self.game_screen.object_color)
        exit_text_rect = exit_text.get_rect(center=exit_button.center)
        screen.blit(exit_text, exit_text_rect)
        # start_text = font.render("Press Enter to Start", True, object_color)
        # start_rect = start_text.get_rect(center=(self.game_screen.width // 2, self.game_screen.height // 2 + 50))
        # screen.blit(start_text, start_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_screen.quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if restart_button.collidepoint(event.pos):
                        return game_running_state.GameRunningState(self.game_screen)
                    elif exit_button.collidepoint(event.pos):
                        self.game_screen.quit_game()

        return None