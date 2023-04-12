class Queue:
    def __init__(self,contents):
        self._hiddenlist = list(contents)

class Voiture():
    def __init__(self):
        self.prix = 1000
        self.roue = 4
        self.porte = 4

    def set_prix(self,prix):
        self.prix = prix

class VoitureLuxe(Voiture):
    def __init__(self):
        self.prix = 2000000

    def print_deLuxe(self):
        print("Cette voiture pèse sa mère")

v1 = Voiture()
v2 = VoitureLuxe()