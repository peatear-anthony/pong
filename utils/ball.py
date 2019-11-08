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
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.y = float(self.rect.y)

        self.color = self.settings.ball_color 

    def update(self):
        self.y += self.settings.ball_speed_magnitude
        self.rect.y = self.y

    def draw_ball(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

