import pygame


class GameScreen:
    def __init__(self, width: int, height: int, target_fps: int = 60, background_color=(0, 0, 0),
                 object_color=(255, 255, 255), font=None, font_size=36):
        self.width = width
        self.height = height
        self.target_fps = target_fps
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background_color = background_color
        self.object_color = object_color
        self.border = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        if font is None:
            self.font = pygame.font.Font(pygame.font.get_default_font(), font_size)
        else:
            self.font = font
        pygame.display.set_caption("Ping Pong")

    def fill_background(self):
        self.screen.fill(self.background_color)
