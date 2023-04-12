"""
Programme regroupant toutes les fonctions du jeu
"""
def choose(ListeMots):  # Choisis un mot au hasard parmis une liste prédéfinie
    import random as rd
    mot = rd.choice(ListeMots)
    return mot

def ecrire_mot(mot_cible,lettres_trouvees):
    mot = ""
    for l in mot_cible:
        if l in lettres_trouvees:
            mot += l
        else:
            mot += "_"

    return mot