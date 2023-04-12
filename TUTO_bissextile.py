# Ce code permet de verifier si une annee est bissextile ou pas
# Premier tuto de OpenClassRoom.com
annee = input("Saisissez l'annee:")
annee = int(annee)
x = annee/4

if type(x) == int:
    x = annee/100
    if type(x) == int:
        x = annee/400
        if type(x) == int:
            print(annee, " est bissextile" )
else:
    print(annee, " n'est pas bissextile")