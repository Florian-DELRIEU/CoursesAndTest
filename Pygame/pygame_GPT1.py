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
    def __init__(self,x=None,y=None):
        self.x = random.randint(0, width) if x == None else x
        self.y = random.randint(0, height) if y == None else y
        self.direction = random.randint(0,360)
        self.speed = 1
        self.size = 10
        self.energy = 1

    def draw(self, window):
        pygame.draw.rect(window, RED, (self.x, self.y, self.size, self.size))

    def move(self,model="drunk_man"):
        if model == "drunk_man":
            self.direction = random.randint(0,360)
            self.x += self.speed * np.cos(self.direction)
            self.y += self.speed * np.sin(self.direction)

    def gain_energy(self,amount=1):
        self.energy += amount
        self.size = 0.1*self.energy + 10

    def try_split(self):
        if self.energy > 100:
            Blobs.append(Blob(self.x,self.y))
            self.energy -= 100


# Liste de proies et de prédateurs
Blobs = [Blob(300,400) for _ in range(1)]

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
        blob.gain_energy(0.1)
        blob.try_split()
        blob.draw(window)

    # Dessiner les proies et les prédateurs

    pygame.display.update()

# Quitter Pygame
pygame.quit()
