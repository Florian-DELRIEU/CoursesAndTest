import random as rd
CHOIX = ["CISEAUX","FEUILLE","PIERRE"]
choix = str()
choix = input("Choisissez entre PIERRE, CISEAUX et FEUILLE: ")
choix = choix.upper()
print("Vous avez choisi : " + choix)
choixPC = rd.choice(CHOIX)
issue = str()

assert (type(choix) and type(choixPC)) is str

print("Le PC à choisi " + choixPC )

if choix == CHOIX[0]:
    if choixPC == CHOIX[1]:
        issue = "Victoire"
    elif choixPC == CHOIX[2]:
        issue = "Défaite"
    elif choixPC == choix:
        issue = "Egalité"

if choix == CHOIX[1]:
    if choixPC == CHOIX[2]:
        issue = "Victoire"
    elif choixPC == CHOIX[0]:
        issue = "Défaite"
    elif choixPC == choix:
        issue = "Egalité"

if choix == CHOIX[2]:
    if choixPC == CHOIX[0]:
        issue = "Victoire"
    elif choixPC == CHOIX[1]:
        issue = "Défaite"
    elif choixPC == choix:
        issue = "Egalité"

if issue == "Victoire":
    print(" Tu as battu " + choixPC + " avec " + choix)
if issue == "Défaite":
    print("Tu as été battu par " + choixPC)
if issue == "Egalité":
    print("Ouf ! Tu as eu chaud ! Le PC à fait le même choix que toi looooool")
