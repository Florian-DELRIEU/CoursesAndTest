"""
Tuto apprentissage de tri
"""
#%%
prenoms = ['Jacques', "Laure", "André", "Victoire", "Albert", "Sophie"]

prenoms2 = sorted(prenoms)  # Trie par ordre alpha
prenoms.sort()  # Trie par ordre alpha

etudiants1 = [
    ("Clément", 14, 16),
    ("Charles", 12, 15),
    ("Oriane", 14, 18),
    ("Thomas", 11, 12),
    ("Damien", 12, 15),
]
sorted(etudiants1)  # Trie en fonction de la première colonne (par ordre alpha donc)

sorted(etudiants1, key = lambda col: col[2])  # Trie en fonction de la 3eme colonne (croissant)
from operator import itemgetter
sorted(etudiants1, key = itemgetter(2))  # Ou alors on utilise la fonction itemgetter

class Etudiant:
    def __init__(self,nom,age,moyenne):
        self.nom = nom
        self.age = age
        self.moyenne = moyenne
    def __repr__(self):
        return "{}      age: {} ans        moyenne: {}/20".format(self.nom, self.age, self.moyenne)

etudiants2 = [
    Etudiant("Clément", 14, 16),
    Etudiant("Charles", 12, 15),
    Etudiant("Oriane", 14, 18),
    Etudiant("Thomas", 11, 12),
    Etudiant("Damien", 12, 15),
]

"""
Pour trier cette liste de tuples, on va utiliser la fonction _lt_ (lower than). On peut aussi utiliser l'argument key avec une fonction lambda comme précédemment
"""

sorted(etudiants2, key = lambda etudiants2: etudiants2.moyenne, reverse=True)  # Reverse est un booléen qui permet de trier dans le sens inverse
from operator import attrgetter
sorted(etudiants2, key=attrgetter("age","moyenne"))  # trie par age et par moyenne si meme age
sorted(etudiants2, key=attrgetter("moyenne"))  # meme resultat que avant mais plus clair je trouve

class Inventaire:
    def __init__(self,produit,prix,vente):
        self.produit = produit
        self.prix = prix
        self.vente = vente

    def __repr__(self):
        return "Vente de {}:    {} x {} € ".format(self.produit, self.vente, self.prix)

inventaire = [
    Inventaire("pomme rouge", 1.2, 19),
    Inventaire("orange", 1.4, 24),
    Inventaire("banane", 0.9, 21),
    Inventaire("poire", 1.2, 24),
]
inventaire.sort(key = attrgetter("prix"), reverse=True)
inventaire.sort(key = attrgetter("vente"))
"""
Comme les tries sont persistant cela permet de les cumuler à la suite pour avoir un trie par nombre de vente et par décroissance des prix si les ventes sont les mm
"""