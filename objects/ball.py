import pygame
from pygame.sprite import Sprite
import time

class Ball(Sprite):

    def __init__(self, settings, screen):
        super(Ball, self).__init__()
        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.rect = pygame.Rect(0, 0,
            settings.ball_diameter, settings.ball_diameter)
        self.center_ball()

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.color = self.settings.ball_color 

        self.initialize_ball_vel()

    def center_ball(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def center_ball_on_paddle(self, paddle):
        # Center the ball on top of the paddle and set speed to 0
        self.vel_y, self.vel_x = 0, 0
        self.rect.centerx = paddle.rect.centerx
        self.x = paddle.rect.centerx
        if paddle.player == 2:
            self.y = paddle.rect.top - self.settings.ball_diameter 
        elif paddle.player == 1:
            self.y = paddle.rect.bottom

    def initialize_ball_vel(self):
        self.vel_x = 0
        self.vel_y = self.settings.ball_speed_magnitude

    def update(self):
        self.y += self.vel_y
        self.x += self.vel_x
        self.rect.y = self.y
        self.rect.x = self.x

    def draw_ball(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
