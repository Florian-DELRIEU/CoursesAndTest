class Voiture:
    __code = "1111"
    def __init__(self):
        self.nom = "Clio"
        self.roues = 4
        self.couleur = "noire"
        self.moteur = 1
        self.masse = 1000
    def __repr__(self):  #Modifie comment on affiche l'objet quand on l'appel
        """
        On peut faire aussi repr(Exemple)
        :return:
        """
        return "Nom de l'objet: {0}, masse: {1}".format(self.nom, self.masse)
    def __str__(self):  #Modifie l'affichage de l'objet quand on l'appel avec print()
        return "L'objet est un {} qui s'appelle {}".format(self.valeur, self.nom)
    def __getattr__(self, attribut):  #Execute si self.attribut n'exsiste pas
        return "L'attribut n'exsiste pas ! Try again !"
    def __setattr__(self, attribut, valeur):  #Ajoute un attribut à l'objet
        print("Attribut {} ajouter".format(attribut))
    def __delattr__(self, attribut):  #Supprime l'attribut
        del object.attribut
    def __del__(self):  #Est appelé lors de la destruction de l'objet
        print("La voiture est détruite")
    def allumer(self):
        code = input("Saisissez le code: ")
        if code == self.__code: print("La voiture demarre")
        else:                   print("Mauvais code")
    def resetCode(self):
        code = input("Saisissez le code: ")
        if code == self.__code:
            newcode = input("Entrez le nouveau code")
            self.__code = newcode
    def showcode(self):
        print(self.__code)
    def combien(cls):  # Methode de classe et pas d'instance
        print("Il y a eu {} voiture crées".format(cls.nbr_objet))
    combien = classmethod(combien)  # Pour que python reconnaisse la méthode de classe

class VoitureSport(Voiture):  # Recupere tous les attributs de :Voiture:
    def __init__(self):
        self.nom = "Ferrari"
    def allumer(self):
        Voiture.allumer(self)
        print("Here we go !!!")



########################################################################################################################
MaVoiture = VoitureSport()
MaVoiture.resetCode()
MaVoiture.showcode()

print(MaVoiture.__dict__)  # Affiche les attribut en dico
