'''
Retourne si l'année est bissextile ou non
'''

annee = input("Entrez une annnée : ")
annee = int(annee)
if annee % 4 == 0:
    print("l'annee ",annee," est bissextile")
else:
    print("L'annee ",annee," n'est pas bissextile")