Dico = dict()
# list >> []
# tuple >> ()
# dict ou set(pas de clé) >> {}

Dico["pseudo"] = "Viper"
Dico["Prenom / Nom"] = "Florian Delrieu"
Dico["pseudo"] = "Zeviper" # Remplace le précédent pseudo
Dico[1] = "Viper"
Dico[29] = "C'est mon pseudo"

print(" --------------------------------------------------- ")
print(" --------------------------------------------------- ")

plateau = {("A",1,):"Tour" , ("A",2,):"Pion" , ("B",1,):"Roi" , 
           ("B",2,):"Reine"}
assert type(plateau) is dict
plateau["lol"] = "TEST"
del plateau["lol"] # == plateau.pop("lol")
print(plateau)

print(" --------------------------------------------------- ")
print(" --------------------------------------------------- ")

del Dico
Dico = dict()
Dico["set1"] = [1,2,3]
Dico[(1,2)] = ["chaine",1 ,2]
Dico[1,2] = ["lol"]
print(Dico)
chaine = Dico[1,2]

del Dico
Dico = {2:"a" , "3":1} #Dico déjà rempli
Set = {"lol" , "c'est le lol"} # Pas de clé c'est donc un set
print(Dico)
print(Set)

print(" --------------------------------------------------- ")
print(" --------------------------------------------------- ")

Fruits = { "pommes":2 , "oranges":1 , "fraise":0}
for cle in Fruits:
    print(cle)
for cle in Fruits.keys():
    print(cle)
for valeur in Fruits.values():
    print(valeur)
if 2 in Fruits.values():
    print("Un des articles est en double")
for cle,valeur in Fruits.items():
    print("Il y a {} {}.".format(valeur,cle))
    
print(" --------------------------------------------------- ")
print(" --------------------------------------------------- ")

def function_dico(**parametres):
    print("Voici les paramètres que j'ai reçu: {}".format(parametres))
function_dico( a=2 , b=1 )
