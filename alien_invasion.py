import pygame
from settings import Settings
from ship import Ship
import game_functions
from pygame.sprite import Group

def run_game():
	#Initialize game and create a screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	ship = Ship(ai_settings, screen)
	#Make an alien
	#alien = Alien(ai_settings, screen)
	#Make a group to store bullets in
	bullets = Group()
	aliens = Group()
	#Create the fleet of aliens
	game_functions.create_fleet(ai_settings, screen, ship, aliens)
	#Start the main loop for the game
	pygame.display.set_caption("Alien Invasion")
	#Start the main loop for the game.
	while True:
		game_functions.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		game_functions.update_bullets(bullets)
		game_functions.update_screen(ai_settings, screen, ship, aliens, bullets)
		#Make the most recently drawn screen visible.
		pygame.display.flip()
run_game()
