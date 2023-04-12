"""
Méthode spéciales dans la création de classe
les methode : __methode__ s'appellent des Magics Methode (a voir !!)
"""

class Exemple:

    def __init__(self,nom):  #Est appelé lors de la création de l'objet
        self.nom = nom
        self.valeur = "Exemple"

        print("L'objet Exemple est crée")

    def __repr__(self):  #Modifie comment on affiche l'objet quand on l'appel
        """
        On peut faire aussi repr(Exemple)
        :return:
        """
        return "Nom de l'objet: {1}, valeur: {0}".format(self.valeur, self.nom)

    def __str__(self):  #Modifie l'affichage de l'objet quand on l'appel avec print()
        return "L'objet est un {} qui s'appelle {}".format(self.valeur, self.nom)

    def __getattr__(self, attribut):  #Execute si self.attribut n'exsiste pas
        return "L'attribut n'exsiste pas ! Try again !"

    def __setattr__(self, attribut, valeur):  #Ajoute un attribut à l'objet
        print("Attribut {} ajouter".format(attribut))

    def __delattr__(self, attribut):  #Supprime l'attribut
        del object.attribut

    def __del__(self):  #Est appelé lors de la destruction de l'objet
        print("L'Exemple est détruis")


class Classeur:
    def __init__(self):
        self.dictionnaire = dict()

    def __contains__(self, item):  #Detecte si item est présent dans une des listes de self.dictionnaire
        for k in self.dictionnaire.keys():
            if item in self.dictionnaire[k]:
                return True
            else:
                return False

    def __setitem__(self, key, value):  #Cette commande permet de stocker des objet comme un dico
        self.dictionnaire[key] = value

    def __getitem__(self, key):
        return self.dictionnaire[key]


class Montre:
    def __init__(self,min=0,sec=0):
        self.min = min
        self.sec = sec

    def set(self,min,sec):
        self.min = min
        self.sec = sec

    def __repr__(self):
        return "{:02}:{:02}".format(self.min,self.sec)

    def __add__(self, sec):  #Ajoute sec secondes (est appellé avec le signe +)
        self.sec += sec
        if self.sec >= 60:
            self.min += self.sec // 60
            self.sec = self.sec - (self.sec // 60)*60

    def __sub__(self, sec):  #Enlève sec secondes (-)
        print("Attention cette opération bug totalement mais ça me saoule donc je verrai demain")
        self.sec -= sec
        if self.sec << 0:
            self.min -= - self.sec // 60 + 1
            self.sec = 60 + self.sec
            if self.sec == 60:
                self.min += 1
                self.sec = 0

    def seconds(self):  #Donne le nombre de secondes total
        return self.min * 60 + self.sec

class Coffre:
    __code = "1111"
    def __init__(self):
        self.fric = 1000
    def showcode(self):
        print(self.__code)
    def enterCode(self,code):
        if code == self.__code:
            print("Le coffre est ouvert")

#########################################

a = Exemple("a")
print(">> a")
a
print(">> repr(a)")
repr(a)
print(">> print(a)")
print(a)

hasattr(a,"lol")  # VRAI si l'attribut a.lol existe. FAUX sinon

print("############################")

b = Classeur()
b.dictionnaire[1] = "lol"
print(b.dictionnaire[1])

b.__setitem__(1,"XD")
print(b.__getitem__(1))

print("############ FIN DU PROGRAMME ################")