from vpython import *
import numpy as np

def B(): print("The button said this: ", button1.text)
def R(r): print(r.checked) # alternates
def C(r): print(r.checked) # alternates
def S(s): print(s.value)  # affiche la valeur du slider en temps réel
def M(m): print(m.selected, m.index)
def T(s): print(s.text, s.number)


cube = box()

button1 = button( bind=B, text='Button' )  # :bind: methode executé quand le bouton est pressé
scene.append_to_caption('\n\n')  # Ajout en bas du :caption:

button2 = radio(bind=R, text='Run') # text to right of button
scene.append_to_caption('\n\n')

checkbox(bind=C, text='Run') # text to right of checkbox
scene.append_to_caption('\n\n')

slider( bind=S )  # par defaut donne une valeur de 0 a 1
scene.append_to_caption('\n\n')

menu( choices=['cat', 'dog', 'horse'], bind=M )
scene.append_to_caption('\n\n')

winput( bind=T )

s = input('What is your name?')