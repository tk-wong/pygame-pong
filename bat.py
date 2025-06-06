import pygame


class Bat:
    def __init__(self, top_left_x, top_left_y, width, height, color=(0,0,0)):
        self.rect = pygame.Rect(top_left_x, top_left_y, width, height)
        self.color = color

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
        pygame.draw.rect(screen, self.color, self.rect)
