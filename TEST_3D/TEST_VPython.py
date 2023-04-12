from vpython import *
import time as t
import numpy as np

cube = box(pos=vector(0,0,0))

def slider_value(s): return s.value  # Retourne la valeur du slider
rotation_slider = slider(bind=slider_value,min=0,max=0.1)  #bind renvoie la fonction a executé

while True:
     rate(60)
     cube.rotate(angle=slider_value(rotation_slider)  # récupere la valeur du slider :rotation_slider:
                 ,axis=vector(0,0,1))