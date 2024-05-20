import pygame
import random
import numpy as np

# Initialisation de Pygame
pygame.init()

# Configuration de la fenêtre
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simulation Proie-Prédateur")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Classes pour les proies et les prédateurs
class Blob:
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.direction = random.randint(0,360)
        self.speed = 1
        self.size = 10

    def draw(self, window):
        pygame.draw.rect(window, RED, (self.x, self.y, self.size, self.size))

    def move(self,model="drunk_man"):
        if model == "drunk_man":
            self.direction = random.randint(0,360)
            self.x += self.speed * np.cos(self.direction)
            self.y += self.speed * np.sin(self.direction)


# Liste de proies et de prédateurs
Blobs = [Blob() for _ in range(10)]

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Dessiner la fenêtre
    window.fill(WHITE)
    for blob in Blobs:
        blob.move()
        blob.draw(window)

    # Dessiner les proies et les prédateurs

    pygame.display.update()

# Quitter Pygame
pygame.quit()
