import pygame
from pygame.sprite import Sprite

class Paddle(Sprite):
    """ A class to represent the player's paddle"""

    def __init__(self, settings, screen, player):
        """Initialize the paddles and set the starting position"""
        super(Paddle, self).__init__()

        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.player = player
        self.moving_right = False
        self.moving_left = False

        # Create the paddle rect and then set correct position.
        self.rect = pygame.Rect(0, 0, settings.paddle_width, 
            settings.paddle_height)
        self.rect.centerx = self.screen_rect.centerx
        
        # Set starting heights repective to player
        if player == 1:
            self.rect.top = 0
        else:
            self.rect.bottom = self.screen_rect.bottom

        # Store the paddle's x value as a float
        self.center = float(self.rect.centerx)
        self.color = self.settings.paddle_color
        self.speed_factor = self.settings.paddle_speed_factor

    def center_paddle(self):
        self.center = self.screen_rect.centerx

    def update(self):
        """ Update the position of the paddle"""
        if self.moving_left and (self.rect.left >= 0):
            self.center -= self.settings.paddle_speed_factor
        if self.moving_right and (self.rect.right <= self.screen_rect.right):
            self.center+= self.settings.paddle_speed_factor

        self.rect.centerx = self.center
    
    def draw_paddle(self):
        pygame.draw.rect(self.screen, self.color, self.rect)




       


