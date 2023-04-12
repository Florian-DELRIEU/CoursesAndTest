def tronc(flottant):
    assert type(flottant) == float

    chaine = str(flottant)
    liste = chaine.split(".")
    decimal = liste[1]
    entier = liste[0]
    liste = list()
    for lettre in decimal:
        liste += [lettre]
    decim_tronc = liste[0:2]
    liste2 = [entier,decim_tronc]
    flottant_tronc = ".".join(liste2)
    print(flottant_tronc)