import pygame
import sys


def update_screen(ai_settings, screen):
    screen.fill(ai_settings.bg_color)

    pygame.display.flip()

def check_events(ai_settings, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
