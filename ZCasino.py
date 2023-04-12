import random as rd # Module de Random
import math as m # Module de Maths
        
# Initialisation
nombre_partie = input("Nombre de partie: ")
compte = input("Entrer votre compte de départ: ")
compte = int(compte)
nombre_partie = int(nombre_partie)
N_partie = 0 # Numero de partie

while N_partie < nombre_partie:
    N_partie += 1
    cible = input("Misez un point entre 0 et 49 :")
    mise = input("Rentrer la mise :")
    cible = int(cible)
    mise = int(mise)
    if cible > 0 and cible < 49:
        print("OK !")
    else:
        mise = 0
        print("Mauvaise Cible")
        break
    compte += - mise
    print("Vous avez misé ",mise," euros, il vous reste ",compte,\
          " euros sur votre compte")
    if cible % 2 ==  0:
        couleur_cible = "Noir"
    else:
        couleur_cilbe = "Rouge"
    print("La mise est sur le ",cible," ",couleur_cible)
    bille = rd.randrange(0,49) # rd.randrange random entre 0 et 49
    bille = m.ceil(bille) # m.ceil fait un arrondi
    if bille % 2 == 0:
        couleur_bille = "Noir"
    else:
        couleur_bille = "Rouge"
    if bille == cible:
        gain = 40
        break
    elif couleur_bille == couleur_cible:
        gain = 0.5
    else:
        gain = 0
    compte = compte + (gain * mise)
    print("La bille tombe sur le ",bille," ",couleur_bille)
    print("Vous recevez ",gain * mise," euros. il vous reste donc "\
          ,compte," euros sur votre compte")
        