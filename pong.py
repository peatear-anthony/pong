import pygame
import sys
from settings import Settings
from utils import *
import functions as f

def run_game():
    pygame.init()
    settings = Settings() 
    screen = pygame.display.set_mode((settings.width, settings.length))
    pygame.display.set_caption(settings.title)

    # Create two paddles for each player
    paddle1 = Paddle(settings, screen, player = 1)
    paddle2 = Paddle(settings, screen, player = 2)
    paddles = [paddle1, paddle2]

    # Create one ball
    ball = Ball(settings, screen)


    while True:

        f.check_events(settings, screen, paddles, ball)

        for paddle in paddles:
            paddle.update()

        f.update_ball(settings, screen, paddles, ball)

        f.update_screen(settings, screen, paddles, ball)


if __name__ == "__main__":
    run_game()
