import pygame

class Ship:
	def __init__(self,ai_settings, screen):
		#Initialize the ship and set its starting position
		self.screen = screen
		self.settings = ai_settings
		self.image = pygame.image.load('images/ship_2.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		# Start each new ship at the bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		# Store a decimal value for the ship's center.
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		# Movement flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
	def update(self):
		if self.moving_right or self.moving_left:
			#Update the ship's position based on the movement flag
			if self.moving_right and self.rect.right < self.screen_rect.right:
				self.centerx += self.settings.ship_speed_factor
			if self.moving_left and self.rect.left > 0:
				self.centerx -= self.settings.ship_speed_factor
			# Update rect object from self.center
			self.rect.centerx = self.centerx
		elif self.moving_up or self.moving_down:
			if self.moving_up and self.rect.top > 0:
				self.centery -= self.settings.ship_speed_factor
			if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
				self.centery += self.settings.ship_speed_factor
			#Update rect object from self.center
			self.rect.centery = self.centery

	def blitme(self):
		#Draw the ship at its current location
		self.screen.blit(self.image, self.rect)
	def center_ship(self):
		#Center the ship on the screen
		self.center = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
