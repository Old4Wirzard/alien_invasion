class Settings():
	#A class to store all settings for Alien Invasion
	def __init__(self):
	#Initialize the game's settings
	# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (0, 0, 0)
	# Ship settings
		self.ship_speed_factor = 2.5
	#Bullet settings
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (187, 48, 48)
		self.bullets_allowed = 5
		
	
