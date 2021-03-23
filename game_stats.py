class GameStats():
    #Track statistics for Alien Invasion
    def __init__(self, ai_settings):
        #Initialize statistics
        self.ai_settings = ai_settings
        self.reset_stats()
        #Start Alien Invasion in an active state
        self.game_active = False
        #High score should never be reset
        try:
            with open('high_score.txt') as high_score_file:
                self.high_score = int(high_score_file.read())
        except:
            self.high_score = 0
    def reset_stats(self):
        #Initialize statistics that can change during the game
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
