import sys
import pygame
from settings import Settings
from objects import *
import functions as f

def run_game():
    pygame.init()
    settings = Settings() 
    screen = pygame.display.set_mode((settings.width, settings.length))
    pygame.display.set_caption(settings.title)

    # Init Game stats
    stats = GameStats(settings)

    # Init Scoreboard
    scoreboard = Scoreboard(settings, screen, stats)
    scoreboard.prep_score()

    # Init paddle for each player
    paddle1 = Paddle(settings, screen, stats, player = 1)
    paddle2 = Paddle(settings, screen, stats,  player = 2)
    paddles = [paddle1, paddle2]

    # Init  ball
    ball = Ball(settings, screen)

    while True:
        f.check_events(settings, stats, screen, paddles, ball)
        for paddle in paddles:
            paddle.update()
        f.update_ball(settings, stats, screen, scoreboard, paddles, ball)
        f.update_screen(settings,stats, screen, scoreboard, 
            paddles, ball)

if __name__ == "__main__":
    run_game()
