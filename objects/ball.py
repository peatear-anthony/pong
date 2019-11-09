import pygame
from pygame.math import Vector2
from pygame.sprite import Sprite

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

    def initialize_ball_vel(self):
        self.vel_x = 0
        self.vel_y = 0.5

    def update(self):
        self.y += self.vel_y
        self.x += self.vel_x
        self.rect.y = self.y
        self.rect.x = self.x

    def draw_ball(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
