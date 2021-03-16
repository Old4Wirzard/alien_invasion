import sys
import pygame
from bullet import Bullet
from alien import Alien

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
	elif event.key == pygame.K_LEFT:
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
def create_fleet(ai_settings, screen, aliens):
	#Create a full fleet of aliens."""
	# Create an alien and find the number of aliens in a row.
	# Spacing between each alien is equal to one alien width
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	#Create the first row of aliens
	for alien_number in range(number_aliens_x):
		#Create an alien and place it in the row
		alien = Alien(ai_settings, screen)
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x  = alien.x
		alien.add(aliens)
def update_screen(ai_settings, screen, ship, aliens, bullets):
	#Update images on the screen and flip to the new screen
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	aliens.draw(screen)
	#Redraw all bullets behind ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullet()
def update_bullets(bullets):
	bullets.update()
	# Get rid of bullets that have disappeared.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
