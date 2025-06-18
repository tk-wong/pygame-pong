import math
import random

from game_state import GameState
import pygame


# from bat import Bat


class GameRunningState(GameState):
    def __init__(self, game_screen, left_bat, right_bat, ball_speed=4.5, ball_radius=5):
        self.game_screen = game_screen
        self.left_bat = left_bat
        self.right_bat = right_bat
        self.ball_x, self.ball_y = game_screen.border.center
        self.ball_radius = ball_radius
        self.is_reversed_x = False
        self.is_reversed_y = False
        self.left_score = 0
        self.right_score = 0
        self.ball_speed = ball_speed

    def execute(self):
        pad_speed = self.left_bat.bat_speed
        delta_time = self.game_screen.clock.tick()
        screen_width = self.game_screen.width
        screen_height = self.game_screen.height
        font = self.game_screen.font
        screen = self.game_screen.screen
        object_color = self.game_screen.object_color
        border = self.game_screen.border

        moving_speed = self.ball_speed * (delta_time / 1000) * self.game_screen.target_fps
        pad_moving_speed = math.ceil(pad_speed * (delta_time / 1000) * self.game_screen.target_fps)
        bat_height = self.left_bat.rect.height
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        self.game_screen.fill_background()
        center_line_spacing = 20
        center_line_width = 10
        for i in range(0, screen_height, center_line_spacing):
            pygame.draw.line(self.game_screen.screen, self.game_screen.object_color, (screen_width // 2, i),
                             (screen_width // 2, i + 10),
                             center_line_width)
        left_score_text = font.render(str(self.left_score), True, object_color)
        right_score_text = font.render(str(self.right_score), True, object_color)
        text_padding = 20
        screen.blit(left_score_text, (screen_width // 4, text_padding))
        screen.blit(right_score_text, (screen_width * 3 // 4, text_padding))
        self.left_bat.draw(self.game_screen.screen)
        self.right_bat.draw(self.game_screen.screen)
        ball = pygame.draw.circle(screen, object_color, (self.ball_x, self.ball_y), self.ball_radius)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.right_bat.rect.y > 0:
            self.right_bat.move_up(pad_moving_speed, border.top)
        if keys[pygame.K_DOWN] and self.right_bat.rect.y + bat_height < border.bottom:
            self.right_bat.move_down(pad_moving_speed, border.bottom)
        if keys[pygame.K_w] and self.left_bat.rect.y > 0:
            self.left_bat.move_up(pad_moving_speed, border.top)
        if keys[pygame.K_s] and self.left_bat.rect.y + bat_height < border.bottom:
            self.left_bat.move_down(pad_moving_speed, border.bottom)
        if self.is_reversed_x:
            self.ball_x -= moving_speed
        else:
            self.ball_x += moving_speed

        if self.is_reversed_y:
            self.ball_y += moving_speed
        else:
            self.ball_y -= moving_speed
        if self.hit_top() or self.hit_bottom():
            self.is_reversed_y = not self.is_reversed_y
        left_bat_hit = self.left_bat.ball_hit(ball)
        right_bat_hit = self.right_bat.ball_hit(ball)
        hit_left_border = self.hit_left()
        hit_right_border = self.hit_right()
        if left_bat_hit or right_bat_hit:
            self.is_reversed_x = not self.is_reversed_x
            if left_bat_hit:
                self.ball_x = self.left_bat.rect.right + self.ball_radius
            elif right_bat_hit:
                self.ball_x = self.right_bat.rect.left - self.ball_radius
        elif hit_left_border or hit_right_border:
            self.ball_x, self.ball_y = border.center
            if hit_left_border:
                self.is_reversed_x = False
                self.right_score += 1
            else:
                self.is_reversed_x = True
                self.left_score += 1
            self.is_reversed_y = random.choice([True, False])
        return None

    def hit_bottom(self):
        return self.ball_y + self.ball_radius >= self.game_screen.border.bottom

    def hit_top(self):
        return self.ball_y - self.ball_radius <= self.game_screen.border.top

    def hit_right(self):
        return self.ball_x + self.ball_radius > self.game_screen.border.right

    def hit_left(self):
        return self.ball_x - self.ball_radius < self.game_screen.border.left
