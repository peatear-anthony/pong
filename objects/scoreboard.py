import pygame.font

class Scoreboard():
    """Scoreboard class for displaying live game information"""

    def __init__(self, settings, screen, stats):
        self.settings = settings
        self.screen = screen
        self.stats =  stats
        self.screen_rect = self.screen.get_rect()

        # Font setting for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image"""
        self.score_str = str(self.stats.player_1_score)+" - " \
        + str(self.stats.player_2_score)
        self.score_image = self.font.render(self.score_str, True,
            self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.center = self.screen_rect.center

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)



