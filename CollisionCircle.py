import matplotlib.pyplot as plt


class Circle:
	def __init__(self,x,y,rayon,couleur="k"):
		"""
		Créé un cercle
		:param x:
		:param y:
		:param rayon:
		:param couleur:
		"""
		self.x = x # Position x du centre
		self.y = y # Position y du centre
		self.radius = rayon # Rayon du cercle
		self.color = couleur # Couleur
		self.speed = 0
		self.direction = 0 # Angle avec l'axe x de la vitesse

	def position(self,x,y):  #Change la position du cercle
		self.x = x
		self.y = y

	def speed(self,speed):  #Change la vitesse du cercle
		self.speed = speed

	def direction(self,direction):  #Change la direction de la vitesse
		self.direction = direction