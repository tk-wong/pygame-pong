import pygame


class Bat:

    def __init__(self, game_screen,top_left_x, width=10, height=50,bat_speed=5):
        top_left_y = game_screen.height // 2 - height // 2
        self.game_screen = game_screen
        self.rect = pygame.Rect(top_left_x, top_left_y, width, height)
        self.bat_speed = bat_speed

    def move_up(self, speed, border_top):
        if self.rect.top > border_top:
            self.rect.y -= speed

    def move_down(self, speed, border_bottom):
        if self.rect.bottom < border_bottom:
            self.rect.y += speed

    def ball_hit(self, ball):
        return self.rect.colliderect(ball)

    def y(self):
        return self.rect.y

    def draw(self, screen):
        pygame.draw.rect(screen,self.game_screen.object_color , self.rect)

    def set_bat_speed(self, speed):
        self.bat_speed = speed
