import math
import random

from bat import Bat
from game_state import GameState
import pygame


# from bat import Bat


class GameRunningState(GameState):
    # left_bat = Bat(top_left_x= padding, top_left_y=screen_height // 2 - bat_height // 2, width=bat_width,
    #                height=bat_height, color=game_screen.object_color)
    # right_bat = Bat(top_left_x=screen_width - bat_width - padding, top_left_y=screen_height // 2 - bat_height // 2,
    #                 width=bat_width,
    #                 height=bat_height, color=game_screen.object_color)
    def __init__(self, game_screen, ball_speed=4.5, ball_radius=5):
        padding = 10
        self.game_screen = game_screen
        self.left_bat = Bat(top_left_x=padding, game_screen=game_screen)
        self.right_bat = Bat(top_left_x=game_screen.width - self.left_bat.rect.width - padding, game_screen=game_screen)
        self.ball_x, self.ball_y = game_screen.border.center
        self.ball_radius = ball_radius
        self.x_direction = 1
        self.y_direction = 1
        self.left_score = 0
        self.right_score = 0
        self.ball_speed = ball_speed
        self.delta_time = self.game_screen.clock.tick()

    def execute(self):
        pad_speed = self.left_bat.bat_speed
        self.delta_time = self.game_screen.clock.tick()
        screen_width = self.game_screen.width
        screen_height = self.game_screen.height
        font = self.game_screen.font
        screen = self.game_screen.screen
        object_color = self.game_screen.object_color
        border = self.game_screen.border

        moving_speed = self.ball_speed * (self.delta_time / 1000) * self.game_screen.target_fps
        pad_moving_speed = math.ceil(pad_speed * (self.delta_time / 1000) * self.game_screen.target_fps)
        bat_height = self.left_bat.rect.height
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
        next_ball_x = self.ball_x + moving_speed * self.x_direction
        next_ball_y = self.ball_y + moving_speed * self.y_direction
        next_ball_rect = pygame.Rect(
            int(next_ball_x - self.ball_radius),
            int(next_ball_y - self.ball_radius),
            self.ball_radius * 2,
            self.ball_radius * 2
        )

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
        if self.hit_top(next_ball_rect) or self.hit_bottom(next_ball_rect):
            self.y_direction *= -1

        # if self.is_reversed_y:
        self.ball_y += moving_speed * self.y_direction
        left_bat_hit = self.left_bat.ball_hit(next_ball_rect)
        right_bat_hit = self.right_bat.ball_hit(next_ball_rect)
        hit_left_border = self.hit_left()
        hit_right_border = self.hit_right()
        if left_bat_hit or right_bat_hit:
            self.x_direction *= -1
            if left_bat_hit:
                self.ball_x = self.left_bat.rect.right + self.ball_radius
            elif right_bat_hit:
                self.ball_x = self.right_bat.rect.left - self.ball_radius
        elif hit_left_border or hit_right_border:
            self.ball_x, self.ball_y = border.center
            if hit_left_border:
                self.x_direction = -1
                self.right_score += 1
            else:
                self.x_direction = 1
                self.left_score += 1
            self.y_direction = random.choice([-1, 1])
        self.ball_x += moving_speed * self.x_direction
        # if self.left_score >= 5 or self.right_score >= 5:
        #     from end_game_state import EndGameState
        #     return EndGameState(self.game_screen, self.left_score, self.right_score)
        return None

    def hit_bottom(self, ball_rect):
        return ball_rect.bottom >= self.game_screen.border.bottom

    def hit_top(self, ball_rect):
        return ball_rect.top <= self.game_screen.border.top

    def hit_right(self):
        return self.ball_x + self.ball_radius > self.game_screen.border.right

    def hit_left(self):
        return self.ball_x - self.ball_radius < self.game_screen.border.left
