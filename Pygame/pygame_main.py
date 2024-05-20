import pygame
import random

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
class Proie:
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.size = 5

    def draw(self, window):
        pygame.draw.rect(window, GREEN, (self.x, self.y, self.size, self.size))


class Predateur:
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.size = 10

    def draw(self, window):
        pygame.draw.rect(window, RED, (self.x, self.y, self.size, self.size))


# Liste de proies et de prédateurs
proies = [Proie() for _ in range(50)]
predateurs = [Predateur() for _ in range(10)]

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dessiner la fenêtre
    window.fill(WHITE)

    # Dessiner les proies et les prédateurs
    for proie in proies:
        proie.draw(window)
    for predateur in predateurs:
        predateur.draw(window)

    pygame.display.update()

# Quitter Pygame
pygame.quit()
