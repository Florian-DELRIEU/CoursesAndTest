"""
Jeu du Pendu
"""
print("\nCommençons à jouer ...")

import fonctions as fct
from donnees import *

utilisateur = input("Entrez votre nom : ")
mot_cible = fct.choose(ListeMots)  #Choisis un mot dans la liste
mot_cible = mot_cible.upper()  #Ecris le mot en Majuscule
#print("Le mot choisi est {}".format(mot_cible))

nb_erreurs = 0
lettre_trouvees = list()
mot_courant = fct.ecrire_mot(mot_cible,lettre_trouvees)
continuer = True

while continuer == True:
    print("Le mot courant est : {}".format(mot_courant))
    lettre = input("Entrez une lettre :")
    lettre = lettre.upper()
    if lettre in mot_cible:
        lettre_trouvees.append(lettre)
    else:
        nb_erreurs += 1
        print("Erreurs : {}".format(nb_erreurs))
    mot_courant = fct.ecrire_mot(mot_cible, lettre_trouvees)
    if mot_courant == mot_cible:
        print("Vous avez trouvé le bon mot !! : {}".format(mot_cible))
        print("Vous avez fait {} erreurs".format(nb_erreurs))
        continuer = False
    if nb_erreurs == NbChances:
        print("Vous avez perdu ! Le mot était : {}".format(mot_cible))
        continuer = False

score = 3 - nb_erreurs