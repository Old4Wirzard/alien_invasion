import pygame
from settings import Settings
from ship import Ship
import game_functions
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	#Initialize game and create a screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	ship = Ship(ai_settings, screen)
	#Make an alien
	#alien = Alien(ai_settings, screen)
	#Make a group to store bullets, aliens and stars in
	bullets = Group()
	aliens = Group()
	stars = Group()
	raindrops = Group()
	#Display stars
	game_functions.create_stars_background(ai_settings, screen, stars)
	#Display raindrops
	game_functions.create_raindrop(ai_settings, screen, raindrops)
	#Create the fleet of aliens
	game_functions.create_fleet(ai_settings, screen, ship, aliens)
	#Start the main loop for the game
	pygame.display.set_caption("Alien Invasion")
	#Make the Play button
	play_button = Button(ai_settings, screen, 'Play')
	#Create an instance to store game statistics and create a scoreboard
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	#Display First screen
	game_functions.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, stars, raindrops, play_button)
	#Start the main loop for the game.
	while True:
		game_functions.check_events(ai_settings, screen, stats, play_button, sb,ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			game_functions.update_bullets(ai_settings, screen, stats, sb,ship, aliens, bullets)
			game_functions.update_raindrops(ai_settings, screen, raindrops)
			game_functions.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
			game_functions.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, stars, raindrops, play_button)
run_game()
