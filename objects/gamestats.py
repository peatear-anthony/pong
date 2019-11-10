class GameStats():
    """ Track game stats during the game"""
    def __init__ (self, settings):
        self.settings = settings
        self.game_active = True
        self.reset_stats()

    def reset_stats(self):
        self.player_1_score = 0
        self.player_2_score = 0

