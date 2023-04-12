NbChances = 3  # Nombre d' erreurs avant échec

LettreMin = 2  # Nombre min de lettre dans le mot
LettreMax = 8  # Nombre max de lettre dans le mot

ListeMots = [  # Liste de mots admissibles par le jeu
    "Vélo",
    "Jenny",
    "Test",
    "Tasse",
    "Pelouse",
    "Tina",
    "Sac",
    "Couette",
    "Télévision",
]

for el in ListeMots.copy():  # Supprime les mots trop grands ou trop petits
    if len(el) > LettreMax or len(el) < LettreMin: ListeMots.remove(el)

print("""-------------------------------------------------
Nombre d'erreurs max    : {}
Longueur du mot         : entre {} et {} lettres
-------------------------------------------------""".format(NbChances,LettreMin,LettreMax)
      )