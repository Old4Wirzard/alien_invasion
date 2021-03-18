import sys
import pygame
from bullet import Bullet
from alien import Alien
from star import Star
from raindrop import Raindrop

def check_events(ai_settings, screen, ship, bullets):
	#Watch for keyboard and mouse events.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event, ai_settings, screen, ship, bullets)
			elif event.type == pygame.KEYUP:
				check_keyup_events(event, ship)
def check_keydown_events(event, ai_settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
		# Move the ship to the right
		ship.moving_right = True
		# Move the ship to the left
	elif event.key  == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_SPACE and len(bullets) < ai_settings.bullets_allowed:
		fire_bullet(ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
		sys.exit()
def fire_bullet(ai_settings, screen, ship, bullets):
	#Create a new bullet and add it to the bullets group
		new_bullet = Bullet( ai_settings, screen, ship)
		bullets.add(new_bullet)
def check_keyup_events(event, ship):
	#Stop moving both sides
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False
def create_stars_background(ai_settings, screen, stars):
	while (len(stars) < 300):
		star = Star(ai_settings, screen)
		star.add(stars)
def get_number_aliens_x(ai_settings, alien_width):
	#Determine the number of aliens that fit in a row
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x
def get_number_rows(ai_settings, alien_height, ship_height):
	#Determine the number of rows of aliens that fit on the screen
	available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	#Create an alien and place it in the row
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x  = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	alien.add(aliens)
def create_fleet(ai_settings, screen, ship, aliens):
	#Create a full fleet of aliens
	#Create an alien and find the number of aliens in a row
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows  = get_number_rows(ai_settings, alien.rect.height, ship.rect.height)
	#Create the first row of aliens
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			#Create an alien and place it in the row
			create_alien(ai_settings, screen, aliens, alien_number, row_number)
def update_screen(ai_settings, screen, ship, aliens, bullets, stars, raindrops):
	#Update images on the screen and flip to the new screen
	screen.fill(ai_settings.bg_color)
	stars.draw(screen)
	raindrops.draw(screen)
	aliens.draw(screen)
	ship.blitme()
	#Redraw all bullets behind ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullet()
def update_aliens(ai_settings, aliens):
	#Check if the fleet is at an edge and then update the postions of all aliens in the fleet
	check_fleet_edges(ai_settings, aliens)
	#Update the postions of all aliens in the fleet
	aliens.update()
def update_bullets(bullets):
	bullets.update()
	# Get rid of bullets that have disappeared.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
def check_fleet_edges(ai_settings, aliens):
	#Respond appropriately if any aliens have reached an edge
	for alien in aliens.sprites():
		if alien.check_edge():
			change_fleet_direction(ai_settings, aliens)
			break
def change_fleet_direction(ai_settings, aliens):
	#Drop the entire fleet and change the fleet's direction
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1
def create_raindrop(ai_settings, screen, raindrops):
	for raindrop in range(30):
		raindrop = Raindrop(ai_settings, screen)
		raindrop.add(raindrops)
def update_raindrops(ai_settings, screen, raindrops):
	for raindrop in raindrops:
		raindrop.update()
		if raindrop.check_edge():
			raindrops.empty()
			create_raindrop(ai_settings, screen, raindrops)
