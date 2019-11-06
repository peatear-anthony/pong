import pygame
import sys
from settings import Settings
import functions as f
def run_game():
    pygame.init()
    ai_settings = Settings() 
    screen = pygame.display.set_mode((ai_settings.width, ai_settings.length))
    pygame.display.set_caption(ai_settings.title)

    while True:

        f.check_events(ai_settings, screen)
        f.update_screen(ai_settings, screen)


if __name__ == "__main__":
    run_game()

